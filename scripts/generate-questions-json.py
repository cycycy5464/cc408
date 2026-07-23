#!/usr/bin/env python3
"""
Generate static/data/questions-all.json — a searchable index of all questions.
Run after content changes: python scripts/generate-questions-json.py
"""
import json, os, re, sys

QUESTIONS_DIR = "content/question"
OUTPUT_PATH = "static/data/questions-all.json"

def parse_frontmatter(content):
    fm = {}
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return fm
    yaml_text = m.group(1)
    current_key = None
    current_list = []
    for line in yaml_text.split("\n"):
        list_m = re.match(r"^\s+-\s+\"?([^\"]+)\"?\s*$", line)
        if list_m and current_key:
            current_list.append(list_m.group(1))
            continue
        kv_m = re.match(r"^(\w+):\s*(.*)", line)
        if kv_m:
            if current_key and current_list:
                fm[current_key] = current_list
            key, val = kv_m.group(1), kv_m.group(2).strip()
            current_key = key
            current_list = []
            if val == "":
                continue
            elif val.startswith("[") and val.endswith("]"):
                items = [v.strip().strip("\"'") for v in val[1:-1].split(",") if v.strip()]
                fm[key] = items
            else:
                val = val.strip("\"'")
                if val.isdigit():
                    fm[key] = int(val)
                else:
                    fm[key] = val
    if current_key and current_list:
        fm[current_key] = current_list
    return fm

def main():
    questions = []
    for root, dirs, files in os.walk(QUESTIONS_DIR):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            fm = parse_frontmatter(content)
            if not fm.get("title"):
                continue
            plain = re.sub(r"(?s)\[tag_link\].*$", "", content)
            plain = re.sub(r"(?s)\n\s*[A-D][.、．].*$", "", plain)
            plain = plain.strip().split("---")[-1].strip()[:200]
            questions.append({
                "id": fname.replace(".md", ""),
                "title": fm.get("title", ""),
                "url": f"/question/{fname.replace('.md', '')}/",
                "source": fm.get("source", ""),
                "year": (fm.get("years") or [None])[0],
                "subject": (fm.get("subjects") or [""])[0],
                "type": fm.get("question_type", ""),
                "number": fm.get("number", 0),
                "difficulty": fm.get("difficulty", 1),
                "knowledge_points": fm.get("knowledge_points", []),
                "stem": plain[:120],
            })

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated {OUTPUT_PATH} ({len(questions)} questions, {os.path.getsize(OUTPUT_PATH)} bytes)")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
