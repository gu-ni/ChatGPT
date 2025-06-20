# %%
import os
from openai import OpenAI
import json
from instruction_template import INSTRUCTION_LCB



# 입력/출력 파일 경로
input_jsonl_path = "/home/work/users/PIL_ghj/LLM/datasets/live-code-bench/codeforces_in_lcb_format.jsonl"

output_path = "/home/work/users/PIL_ghj/LLM/datasets/ChatGPT/LiveCodeBench"
os.makedirs(output_path, exist_ok=True)

output_jsonl_path = os.path.join(output_path, "test6_narrative_by_gpt_test.jsonl")

# n번째 JSONL 항목 로드
def load_nth_sample(jsonl_path, n):
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == n:
                return json.loads(line)
    raise IndexError(f"Not found {n}-th index.")

# GPT 호출
def call_gpt(client, prompt):
    response = client.responses.create(
        model="gpt-4.1-2025-04-14",  # 또는 gpt-4.1 mini 등
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
        temperature=0.6,
    )
    return response.output_text.strip()

# 실행
if __name__ == "__main__":
    client = OpenAI()
    
    index = 1  # 예: 세 번째 항목
    sample = load_nth_sample(input_jsonl_path, index)
    prompt = INSTRUCTION_LCB + sample["question_content"]
    print(prompt)
    gpt_response = call_gpt(client, prompt)

    # 출력 확인
    print("\n------------------------- GPT Response -------------------------\n")
    print(gpt_response)

    # 결과 저장
    sample["question_content"] = gpt_response
    with open(output_jsonl_path, "w", encoding="utf-8") as out_f:
        json.dump(sample, out_f, ensure_ascii=False)
        out_f.write("\n")

# %%
