# %%
import os
from openai import OpenAI
import json
from instruction_template import INSTRUCTION_APPS, genres


# 입력/출력 파일 경로
input_jsonl_path = "/home/work/users/PIL_ghj/LLM/datasets/apps_benchmark/data/train_in_lcb_format_200.jsonl"

output_path = "/home/work/users/PIL_ghj/LLM/datasets/ChatGPT/APPS"
os.makedirs(output_path, exist_ok=True)

output_jsonl_path = os.path.join(output_path, "apps_narrative_by_gpt_test.jsonl")

# JSONL 로드
def load_nth_sample(jsonl_path, n):
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == n:
                return json.loads(line)
    raise IndexError(f"Not found {n}-th index.")

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
        model="gpt-4.1-2025-04-14",
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

# 메인 실행
if __name__ == "__main__":
    client = OpenAI()
    index = 1  # 처리할 인덱스
    sample = load_nth_sample(input_jsonl_path, index)
    qid = sample.get("question_id")

    # 중복 체크
    existing_ids = load_existing_question_ids(output_jsonl_path)
    if qid in existing_ids:
        print(f"[SKIP] Question ID '{qid}' already processed.")
    else:
        prompt = INSTRUCTION_APPS.replace("{GENRE}", genres[0]) + sample["question_content"]
        print(prompt)
        gpt_response = call_gpt(client, prompt)

        print("\n------------------------- GPT Response -------------------------\n")
        print(gpt_response)

        sample["question_content"] = gpt_response

        # 결과 이어서 저장
        with open(output_jsonl_path, "a", encoding="utf-8") as out_f:
            out_f.write(json.dumps(sample, ensure_ascii=False) + "\n")
        print(f"[SAVED] Question ID '{qid}' added.")

# %%
