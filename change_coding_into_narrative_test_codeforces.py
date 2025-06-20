import os
from openai import OpenAI
import json
from instruction_template import INSTRUCTION_LCB, INSTRUCTION_HUMANEVAL, INSTRUCTION_CODEFORCES, genres


# 입력 파일 경로
input_jsonl_path = "/home/work/users/PIL_ghj/LLM/datasets/codeforces/codeforces_in_lcb_format.jsonl"
# "/home/work/users/PIL_ghj/LLM/datasets/human-eval/data/HumanEval_in_lcb_format.jsonl"
# "/home/work/users/PIL_ghj/LLM/datasets/live-code-bench/test6.jsonl"

# 출력 파일 경로
output_path_name = "CodeForces"  # HumanEval LiveCodeBench CodeForces

# 파일명
file_name = "codeforces_narrative_by_gpt_test.jsonl" # humaneval_narrative_by_gpt_test.jsonl test6_narrative_by_gpt_test.jsonl


instruction_dict = {
    "HumanEval": INSTRUCTION_HUMANEVAL,
    "LiveCodeBench": INSTRUCTION_LCB,
    "CodeForces": INSTRUCTION_CODEFORCES,
}

output_path = f"/home/work/users/PIL_ghj/LLM/datasets/ChatGPT/{output_path_name}"
os.makedirs(output_path, exist_ok=True)

output_jsonl_path = os.path.join(output_path, file_name)

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

# 메인 실행
if __name__ == "__main__":
    client = OpenAI()
    index = 34  # 처리할 인덱스
    genre_index = 21
    sample = load_nth_sample(input_jsonl_path, index)
    qid = sample.get("question_id")
    instruction = instruction_dict[output_path_name]
    if output_path_name == "CodeForces":
        instruction = instruction.replace("{GENRE}", genres[genre_index])

    # 중복 체크
    existing_ids = load_existing_question_ids(output_jsonl_path)
    if qid in existing_ids and False:
        print(f"[SKIP] Question ID '{qid}' already processed.")
    else:
        prompt = instruction + sample["question_content"]
        "\n------------------------- Prompt -------------------------\n"
        print(prompt)
        gpt_response = call_gpt(client, prompt)

        print("\n------------------------- GPT Response -------------------------\n")
        print(gpt_response)

        sample["question_content"] = gpt_response

        # 결과 이어서 저장
        with open(output_jsonl_path, "a", encoding="utf-8") as out_f:
            out_f.write(json.dumps(sample, ensure_ascii=False) + "\n")
        print(f"[SAVED] Question ID '{qid}' added.")

