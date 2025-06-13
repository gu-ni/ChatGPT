import os
import time
from openai import OpenAI
import json

# Instruction 템플릿
INSTRUCTION = """Please transform the coding problem into a narrative story format using the following guidelines.

### Guidelines for Narrative Conversion:

- You may use alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.**
- Build the story in **any genre or setting**—such as fantasy, sci-fi, historical, modern, dystopian, mystery, or slice-of-life—and express each mathematical rule through **world-specific logic** such as social norms, systems, behaviors, or relationships.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
- You **must present the input and output format** as part of the story's narrative.
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.

The story should be structured into **six paragraphs at most**, and follow this flow:

**Background → Rules and Problem Setting → Task Explanation → Examples and Closing**

The coding problem is as follows:

"""


def rewrite_question_content(client, prompt: str) -> str:
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
        temperature=0.8,
    )
    return response.output_text.strip()


if __name__ == "__main__":
    
    # 입력/출력 파일 경로
    input_jsonl_path = "/home/work/users/PIL_ghj/LLM/datasets/live-code-bench/test6.jsonl"
    output_path = "/home/work/users/PIL_ghj/LLM/datasets/ChatGPT"
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
                
                input_prompt = INSTRUCTION + problem["question_content"]
                
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
            