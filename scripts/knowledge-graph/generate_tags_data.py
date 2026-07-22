#!/usr/bin/env python3
"""
Generate static/data/tags-data.json from content/question/*.md files.

Only includes REAL 408 exam questions (source: "408真题" or pattern {year}-{subj}-{num}.md).
Excludes simulate questions (source: "模拟题" or simulate-* files).
"""
import json, os, re, sys, glob

QUESTIONS_DIR = "content/question"
OUTPUT_PATH = "static/data/tags-data.json"

SUBJECT_NAMES = ["数据结构", "组成原理", "操作系统", "计算机网络"]
SUBJECT_MAP = {"ds": "数据结构", "co": "组成原理", "os": "操作系统", "cn": "计算机网络"}

def parse_years(years_val):
    """Parse the years frontmatter field - returns a list of integer years."""
    if isinstance(years_val, list):
        result = []
        for y in years_val:
            try:
                result.append(int(y))
            except (ValueError, TypeError):
                pass  # skip string years like "模拟卷"
        return result
    return []

def is_real_exam_file(filename, frontmatter):
    """Check if a file represents a real 408 exam question."""
    # Check source field
    source = frontmatter.get("source", "")
    if source == "模拟题":
        return False
    if source == "408真题":
        return True

    # Fallback: check file pattern
    if re.match(r"\d{4}-[a-z]{2}-\d{2,3}\.md$", filename):
        return True

    return False

def parse_frontmatter(content):
    """Parse YAML-like frontmatter from markdown content."""
    fm = {}
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return fm

    yaml_text = m.group(1)
    current_key = None
    current_list = []

    for line in yaml_text.split("\n"):
        # List item
        list_m = re.match(r"^\s+-\s+\"?([^\"]+)\"?\s*$", line)
        if list_m and current_key:
            current_list.append(list_m.group(1))
            continue

        # Key-value
        kv_m = re.match(r"^(\w+):\s*(.*)", line)
        if kv_m:
            # Save previous list if any
            if current_key and current_list:
                fm[current_key] = current_list

            key, val = kv_m.group(1), kv_m.group(2).strip()
            current_key = key
            current_list = []

            if val == "":
                continue  # Next lines should be list items
            elif val.startswith("[") and val.endswith("]"):
                # Inline list
                items = [v.strip().strip("\"'") for v in val[1:-1].split(",") if v.strip()]
                fm[key] = items
            else:
                # Scalar
                val = val.strip("\"'")
                if val.isdigit():
                    fm[key] = int(val)
                else:
                    fm[key] = val

    # Save last list
    if current_key and current_list:
        fm[current_key] = current_list

    return fm

def build_question_type(question_type_val):
    """Convert question_type to display string."""
    if isinstance(question_type_val, str):
        if question_type_val in ("choice",):
            return "选择题"
        if question_type_val in ("comprehensive",):
            return "综合题"
    return str(question_type_val) if question_type_val else "选择题"

def main():
    tag_data = {s: {} for s in SUBJECT_NAMES}
    total_questions = 0
    total_with_kp = 0

    # Walk through all question files
    for root, dirs, files in os.walk(QUESTIONS_DIR):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue

            fpath = os.path.join(root, fname)

            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            fm = parse_frontmatter(content)

            # Skip non-real-exam files
            if not is_real_exam_file(fname, fm):
                continue

            # Get years (integer years only)
            years = parse_years(fm.get("years", []))
            if not years:
                continue

            year = years[0]  # Use first year
            subjects = fm.get("subjects", [])
            knowledge_points = fm.get("knowledge_points", [])
            question_type = build_question_type(fm.get("question_type", ""))
            number = fm.get("number", 0)

            total_questions += 1

            if not knowledge_points:
                continue

            total_with_kp += 1

            for subj in subjects:
                if subj not in tag_data:
                    continue

                for kp in knowledge_points:
                    if kp not in tag_data[subj]:
                        tag_data[subj][kp] = []

                    # Create entry
                    entry = {
                        "quiz_type": question_type,
                        "subject": subj,
                        "title": f"{year} 年 408 真题第 {number} 题",
                        "link": f"/study_methods/408quiz/{year}/#{number}",
                        "year": year
                    }

                    # Avoid duplicates
                    if entry not in tag_data[subj][kp]:
                        tag_data[subj][kp].append(entry)

    # Sort entries within each knowledge point by year then number
    for subj in tag_data:
        for kp in tag_data[subj]:
            tag_data[subj][kp].sort(key=lambda x: (x["year"], x["title"]))

    output = {"tagData": tag_data}

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Stats
    kp_count = sum(len(kps) for kps in tag_data.values())
    entry_count = sum(len(items) for kps in tag_data.values() for items in kps.values())
    print(f"✅ tags-data.json generated successfully!")
    print(f"   Real exam questions with KP: {total_with_kp}/{total_questions}")
    print(f"   Subjects: {len(tag_data)}")
    print(f"   Knowledge points: {kp_count}")
    print(f"   Tag entries (questions × KPs): {entry_count}")

    # Print years
    all_years = set()
    for subj, kps in tag_data.items():
        for kp, items in kps.items():
            for item in items:
                all_years.add(item["year"])
    print(f"   Years: {sorted(all_years)}")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
