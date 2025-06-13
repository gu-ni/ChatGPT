# %%
import os
from openai import OpenAI
import json

# Instruction 템플릿
instruction = """Please transform the coding problem into a narrative story format using the following guidelines.

### Guidelines for Narrative Conversion:

- You may use alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.**
- Express **each mathematical rule** through elements of the story world. These can include:
    - societal rules or norms
    - roles, relationships, or responsibilities among entities
    - operational principles of systems or organizations
    - constraints based on context, environment, or design, etc.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
- If there are exceptions to the rules, describe them as special conditions that align with the world’s internal logic.
- You **must present the input and output format** as part of the story's narrative.
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.
- Don't say anything else.

The story should be structured into **six paragraphs at most**, and follow this flow:

**Background → Rules → Problem Setting → Task Explanation → World Examples and Closing**

The coding problem is as follows:

"""


# 입력/출력 파일 경로
input_jsonl_path = "/home/work/users/PIL_ghj/LLM/datasets/live-code-bench/test6.jsonl"

output_path = "/home/work/users/PIL_ghj/LLM/datasets/ChatGPT"
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
    prompt = instruction + sample["question_content"]
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
