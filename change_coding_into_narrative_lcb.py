import os
import time
from openai import OpenAI
import json
from instruction_template import INSTRUCTION_LCB


def rewrite_question_content(client, prompt: str) -> str:
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
    input_jsonl_path = "/home/work/users/PIL_ghj/LLM/datasets/live-code-bench/test6.jsonl"
    output_path = "/home/work/users/PIL_ghj/LLM/datasets/ChatGPT/LiveCodeBench"
    os.makedirs(output_path, exist_ok=True)
    output_jsonl_path = os.path.join(output_path, "test6_narrative_by_gpt.jsonl")
    
    client = OpenAI()
    
    # 이미 처리된 question_id 목록을 set으로 불러오기
    existing_ids = set()
    if os.path.exists(output_jsonl_path):
        with open(output_jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    if "question_id" in obj:
                        existing_ids.add(obj["question_id"])
                except json.JSONDecodeError:
                    continue

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
                
                input_prompt = INSTRUCTION_LCB + problem["question_content"]
                
                new_content = rewrite_question_content(client, input_prompt)
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
            