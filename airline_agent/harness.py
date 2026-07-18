import io
import json
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
from contextlib import redirect_stdout

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

KB_DIR = Path("kb")

BASE_DIR = Path(__file__).parent
PROJECT_ROOT = BASE_DIR.parent

load_dotenv(PROJECT_ROOT / ".env")

client = OpenAI()

SYSTEM_PROMPT = """
You are the reasoning component of an airline support agent.

You solve user requests by selecting exactly one action at a time, observing the result, and continuing until you can answer.

IMPORTANT

You do NOT possess airline knowledge.

The ONLY source of airline information is the content returned by LOAD_DOCUMENT.

If the required information has not been loaded, assume you do not know it.

Never state any airline fact unless it appears in one or more loaded documents.

------------------------------------------

Available Actions

1.

{
    "action":"ANSWER",
    "answer":"..."
}

2.

{
    "action":"ASK_USER",
    "question":"..."
}

Use ASK_USER only when the user's question cannot be answered without information that only the user can provide.

Ask only the minimum information required.

3.

{
    "action":"LIST_DOCUMENTS"
}

4.

{
    "action":"LOAD_DOCUMENT",
    "documents":[
        "file1.md",
        "file2.md"
    ]
}

5.

{
    "action":"EXECUTE_CODE",
    "code":"..."
}

------------------------------------------

Reasoning Policy

1. Decide what information is needed.

2. If you do not know which document contains it, use LIST_DOCUMENTS.

3. Load only the documents you need. Prefer loading the smallest set of documents likely to answer the question.

4. If the loaded documents contain enough information to answer the user's question, return ANSWER immediately.

5. Only use ASK_USER when the answer depends on information that only the user can provide.

6. If calculations are required, use EXECUTE_CODE.

7. Perform exactly one action per response.

------------------------------------------

Rules

• Answer exactly the question the user asked.
• Keep answers concise.
• Include only the information necessary to answer the user's question.
• Do not include exceptions, pricing, procedures or country-specific rules unless the user asks for them or they are necessary to answer the question.
• Do not assume the user wants a personalised assessment unless they explicitly ask for one.
• Never invent document contents.
• Never invent airline policies.
• Never answer from memory.
• Return ONLY valid JSON.
"""

# ---------------------------------------------------------
# Replace this with OpenAI call
# ---------------------------------------------------------

def call_llm(messages):

    response = client.chat.completions.create(
        model="gpt-5",
        messages=messages,
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content

# ---------------------------------------------------------
# TOOLS
# ---------------------------------------------------------

def list_documents():

    files = []

    for file in sorted(KB_DIR.glob("*.md")):
        files.append(file.name)

    return {
        "status": "SUCCESS",
        "documents": files
    }


def load_document(files):

    contents = {}

    for file in files:

        path = KB_DIR / file

        if not path.exists():

            contents[file] = "ERROR : File not found."

        else:

            contents[file] = path.read_text(
                encoding="utf-8"
            )

    return {
        "status": "SUCCESS",
        "documents": contents
    }


def execute_code(code):

    stdout = io.StringIO()

    globals_dict = {}
    locals_dict = {}

    try:

        with redirect_stdout(stdout):
            exec(code, globals_dict, locals_dict)

        return {

            "status": "SUCCESS",

            "stdout": stdout.getvalue(),

            "locals": {
                k: str(v)
                for k, v in locals_dict.items()
            }

        }

    except Exception as e:

        return {

            "status": "ERROR",

            "error": str(e)

        }


# ---------------------------------------------------------
# REASONING LOOP
# ---------------------------------------------------------

def run_reasoning_loop(messages):

    iteration = 1

    MAX_ITERATIONS = 10

    while iteration <= MAX_ITERATIONS:

        print()
        print("=" * 70)
        print(f"Reasoning Step {iteration}")
        print("=" * 70)

        response = call_llm(messages)
        messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        action = json.loads(response)

        print("\nLLM Decision\n")
        print(json.dumps(action, indent=4))

        action_name = action["action"]

        # -------------------------------------------------

        if action_name == "ANSWER":

            print("\n✓ Agent has enough information.\n")

            return action["answer"]

        # -------------------------------------------------

        elif action_name == "ASK_USER":

            print("\nExecuting Tool : ASK_USER")

            reply = input(action["question"] + "\n> ")

            messages.append(
                {
                    "role": "user",
                    "content":
                        "Tool Observation (ASK_USER):\n\n"
                        f"User replied: {reply}"
                }
            )

        # -------------------------------------------------

        elif action_name == "LIST_DOCUMENTS":

            print("\nExecuting Tool : LIST_DOCUMENTS")

            observation = list_documents()

            print("\nObservation\n")

            print(
                json.dumps(
                    observation,
                    indent=4
                )
            )
            
            messages.append(
                {
                    "role": "user",
                    "content":
                        "Tool Observation (LIST_DOCUMENTS):\n\n"
                        + json.dumps(observation, indent=2)
                }
            )

        # -------------------------------------------------

        elif action_name == "LOAD_DOCUMENT":

            print("\nExecuting Tool : LOAD_DOCUMENT")

            observation = load_document(
                action["documents"]
            )
            
            print("\nLoaded Documents\n")

            for file in observation["documents"]:
                print("✓", file)

            messages.append(
                {
                    "role": "user",
                    "content":
                        "Tool Observation (LOAD_DOCUMENT):\n\n"
                        + json.dumps(observation, indent=2)
                }
            )

        # -------------------------------------------------

        elif action_name == "EXECUTE_CODE":

            print("\nExecuting Tool : EXECUTE_CODE")

            print("\nGenerated Python\n")
            print(action["code"])

            observation = execute_code(
                action["code"]
            )

            print("\nExecution Result\n")

            print(
                json.dumps(
                    observation,
                    indent=4
                )
            )
            
            messages.append(
                {
                    "role": "user",
                    "content":
                        "Tool Observation (EXECUTE_CODE):\n\n"
                        + json.dumps(observation, indent=2)
                }
            )

        # -------------------------------------------------

        else:

            print("\nUnknown action returned by LLM.\n")
            
            messages.append(
                {
                    "role": "user",
                    "content":
                        f"Tool Observation (ERROR): Unknown action {action_name}"
                }
            )
        iteration += 1


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\nAirline Agent\n")

    question = input("You: ")

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": question
        }

    ]

    answer = run_reasoning_loop(messages)

    print("\n" + "=" * 70)
    print("FINAL ANSWER")
    print("=" * 70)

    print(answer)


if __name__ == "__main__":
    main()