import os
import time
import json
from instruction_template import INSTRUCTION_HUMANEVAL, genres

from transformers import AutoTokenizer, AutoModelForCausalLM
import gc
import torch

model_id = "google/gemma-2-27b-it"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cuda",
    torch_dtype=torch.bfloat16,
)

def call_model(prompt):
    chat = [
        {
            "role": "user", 
            "content": f"You are an imaginative storyteller who follows instructions well.\n\n{prompt}"
        },
    ]
    
    # Chat template 적용
    prompt_text = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    
    # 토크나이징
    input_ids = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt").to(model.device)
    input_len = input_ids.shape[1]
    
    # 생성
    outputs = model.generate(
        input_ids=input_ids,
        temperature=1.0,
        do_sample=True,
        max_new_tokens=1000
    )
    
    # 프롬프트 이후의 토큰만 디코딩
    generated_tokens = outputs[0][input_len:]
    return tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()



# 기존 출력 파일에서 이미 처리한 ID 수집
def load_existing_question_ids(path):
    if not os.path.exists(path):
        return set()
    existing_ids = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
                qid = obj.get("question_id")
                if qid:
                    existing_ids.add(qid)
            except Exception:
                continue
    return existing_ids


if __name__ == "__main__":
    
    input_jsonl_path_list = [
        # "/home/work/users/PIL_ghj/LLM/datasets/human-eval/data/HumanEval_in_lcb_format_io_filtered.jsonl",
        "/home/work/users/PIL_ghj/LLM/datasets/live-code-bench/test6.jsonl",
        "/home/work/users/PIL_ghj/LLM/datasets/codeforces/codeforces_in_lcb_format.jsonl",
        "/home/work/users/PIL_ghj/LLM/datasets/codeforces/codeforces_mid_in_lcb_format.jsonl",
        "/home/work/users/PIL_ghj/LLM/datasets/codeforces/codeforces_challenging_in_lcb_format.jsonl",
    ]
    
    output_path_list = [
        # "/home/work/users/PIL_ghj/LLM/datasets/Ablation/diff_quality/HumanEval",
        "/home/work/users/PIL_ghj/LLM/datasets/Ablation/diff_quality/LiveCodeBench",
        "/home/work/users/PIL_ghj/LLM/datasets/Ablation/diff_quality/CodeForces",
        "/home/work/users/PIL_ghj/LLM/datasets/Ablation/diff_quality/CodeForces",
        "/home/work/users/PIL_ghj/LLM/datasets/Ablation/diff_quality/CodeForces",
    ]
    
    output_jsonl_name_list = [
        # "humaneval_filtered_narrative_by_gemma-2-27b-it.jsonl",
        "test6_narrative_by_gemma-2-27b-it.jsonl",
        "codeforces_narrative_by_gemma-2-27b-it.jsonl",
        "codeforces_mid_narrative_by_gemma-2-27b-it.jsonl",
        "codeforces_challenging_narrative_by_gemma-2-27b-it.jsonl",
    ]
    
    for input_jsonl_path, output_path, output_jsonl_name in zip(input_jsonl_path_list, output_path_list, output_jsonl_name_list):
        try:
            # 입력/출력 파일 경로
            os.makedirs(output_path, exist_ok=True)
            output_jsonl_path = os.path.join(output_path, output_jsonl_name)
            
            existing_ids = load_existing_question_ids(output_jsonl_path)
            
            # 입력 파일 처리
            with open(input_jsonl_path, "r", encoding="utf-8") as infile, \
                open(output_jsonl_path, "a", encoding="utf-8") as outfile:  # append 모드로 열기
                
                for i, line in enumerate(infile):
                    try:
                        problem = json.loads(line)
                        qid = problem.get("question_id")
                        print(f"\n[Logging] Starting {i}-th Problem ({qid})...")
                        if qid in existing_ids:
                            print(f"[Logging] Skipping already processed question_id: {qid}")
                            continue
                        
                        genre = genres[int(i % len(genres))]
                        problem["genre"] = genre
                        instruction = INSTRUCTION_HUMANEVAL
                        instruction = instruction.replace("{GENRE}", genre)
                        input_prompt = instruction + problem["question_content"]
                        
                        new_content = call_model(input_prompt)
                        print("\n------------------------- Model Response -------------------------\n")
                        print(new_content)
                        print("\n----------------------------------------------------------------\n")
                        problem["question_content"] = new_content
                        outfile.write(json.dumps(problem, ensure_ascii=False) + "\n")
                        existing_ids.add(qid)

                    except Exception as e:
                        print(f"Error processing a problem: {e}")
                        continue
                    
                    # time.sleep(1)
        except:
            pass
        
        gc.collect()
        torch.cuda.empty_cache()