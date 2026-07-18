import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
PROJECT_ROOT = BASE_DIR.parent

load_dotenv(PROJECT_ROOT / ".env")

client = OpenAI()

KB_DIR = BASE_DIR / "kb"
CATALOG_FILE = BASE_DIR / "catalog.json"

SYSTEM_PROMPT = """
You are helping build a catalog for an airline knowledge base.

Given a markdown document, return ONLY valid JSON in this format:

{
  "title": "...",
  "summary": "..."
}

Rules:
- title: one descriptive line (5-12 words).
- summary: one sentence (maximum 20 words).
- Do NOT mention the filename.
- The title should clearly describe the document's topic.
- The summary should describe what customer questions this document answers.
"""

catalog = []

doc_id = 1

for md_file in sorted(KB_DIR.glob("*.md")):

    print(f"Processing {md_file.name}...")

    # The first few thousand characters are usually enough
    contents = md_file.read_text(encoding="utf-8")[:4000]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": contents
            }
        ]
    )

    metadata = json.loads(response.choices[0].message.content)

    catalog.append({
        "id": doc_id,
        "file": md_file.name,
        "title": metadata["title"],
        "summary": metadata["summary"]
    })

    doc_id += 1

with open(CATALOG_FILE, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2)

print(f"\nCatalog written to {CATALOG_FILE}")