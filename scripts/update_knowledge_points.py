#!/usr/bin/env python3
"""
Update question files with proper knowledge_points tags from tags_data.json
Usage: python update_knowledge_points.py
"""
import json, re, os, glob

TAGS_PATH = r"C:\Users\cheny\xwechat_files\wxid_6qkyv7hwvvx129_6c57\msg\file\2026-07\408标签分析\tags_data.json"
QUESTIONS_DIR = r"E:\programcc408\cc408\content\question"

with open(TAGS_PATH, 'r', encoding='utf-8') as f:
    tag_data = json.load(f)

question_tags = {}
subject_kp = {}

for subject, kps in tag_data.items():
    if subject not in subject_kp:
        subject_kp[subject] = set()
    for kp_name, questions in kps.items():
        subject_kp[subject].add(kp_name)
        for q in questions:
            key = (q["year"], q["question"])
            if key not in question_tags:
                question_tags[key] = set()
            question_tags[key].add(kp_name)

SUBJECT_MAP = {
    "数据结构": "ds",
    "计算机组成原理": "co",
    "组成原理": "co",
    "操作系统": "os",
    "计算机网络": "cn"
}

stats = {"updated": 0, "skipped": 0, "not_found": 0}

for filepath in sorted(glob.glob(os.path.join(QUESTIONS_DIR, "*.md"))):
    filename = os.path.basename(filepath)

    m = re.match(r'(\d{4})-([a-z]{2})-(\d{2,3})\.md', filename)
    if not m:
        print(f"Skip: cannot parse {filename}")
        stats["skipped"] += 1
        continue

    year = int(m.group(1))
    num = int(m.group(3))

    key = (year, num)
    tags = question_tags.get(key, set())

    if not tags:
        print(f"No tags for {year} #{num} ({filename})")
        stats["not_found"] += 1
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    existing_match = re.search(r'knowledge_points:\n((?:\s+- "[^"]+"\n)*)', content)
    if existing_match:
        existing_kps = re.findall(r'"([^"]+)"', existing_match.group(1))
        if len(existing_kps) >= 2:
            print(f"Already tagged {filename}: {existing_kps}")
            stats["skipped"] += 1
            continue

    tags_list = sorted(tags)
    tags_yaml = '\n'.join(f'  - "{t}"' for t in tags_list)

    if 'knowledge_points:' in content:
        new_content = re.sub(
            r'knowledge_points:\n(?:  - "[^"]*"\n)*',
            f'knowledge_points:\n{tags_yaml}\n',
            content
        )
    else:
        new_content = re.sub(
            r'(subjects:\n(?:  - "[^"]*"\n)*)',
            f'\\1knowledge_points:\n{tags_yaml}\n',
            content
        )

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"OK {filename}: {', '.join(list(tags_list)[:4])}")
        stats["updated"] += 1
    else:
        stats["skipped"] += 1

print(f"Done: {stats['updated']} updated, {stats['skipped']} skipped, {stats['not_found']} not_found")
