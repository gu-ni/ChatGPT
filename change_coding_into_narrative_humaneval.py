import os
import time
from openai import OpenAI
import json
from instruction_template import INSTRUCTION_HUMANEVAL, genres


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

# GPT 호출
def call_gpt(client, prompt):
    response = client.responses.create(
        model="gpt-4.1-mini-2025-04-14",
        input=[
            {
                "role": "developer", 
                "content": "You are an imaginative storyteller who follows instructions well."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        temperature=1.0,
    )
    return response.output_text.strip()


if __name__ == "__main__":
    
    # 입력/출력 파일 경로
    input_jsonl_path = "/home/work/users/PIL_ghj/LLM/datasets/human-eval/data/HumanEval_in_lcb_format_io_filtered.jsonl"
    output_path = "/home/work/users/PIL_ghj/LLM/datasets/ChatGPT/HumanEval"
    os.makedirs(output_path, exist_ok=True)
    output_jsonl_path = os.path.join(output_path, "humaneval_filtered_narrative_by_gpt.jsonl")
    
    client = OpenAI()
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
                
                new_content = call_gpt(client, input_prompt)
                print("\n------------------------- GPT Response -------------------------\n")
                print(new_content)
                print("\n----------------------------------------------------------------\n")
                problem["question_content"] = new_content
                outfile.write(json.dumps(problem, ensure_ascii=False) + "\n")
                existing_ids.add(qid)

            except Exception as e:
                print(f"Error processing a problem: {e}")
                continue
            
            time.sleep(1)
