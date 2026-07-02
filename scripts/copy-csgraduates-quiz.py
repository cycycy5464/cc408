#!/usr/bin/env python3
"""Copy csgraduates quiz content, strip Source lines, preserve everything else"""
import os, re

SRC = r'D:\内容整理\csgraduates-main\study_methods\408quiz'
DST = 'content/exam/408quiz'

count = 0
for d in sorted(os.listdir(SRC)):
    if not d.isdigit():
        continue
    src_file = os.path.join(SRC, d, 'content.md')
    if not os.path.exists(src_file):
        continue
    with open(src_file, 'r', encoding='utf-8') as f:
        text = f.read()
    # Remove Source line
    text = re.sub(r'^> Source:.*\n?', '', text, flags=re.MULTILINE)
    # Remove B站 video link
    text = re.sub(r'^- \[.*精讲.*\]\(.*bilibili.*\)\s*\n?', '', text, flags=re.MULTILINE)
    # Keep original csgraduates format completely: tags, answers, everything
    # Just remove the first # Title since frontmatter provides it
    title_match = re.search(r'^# (.+)', text)
    title = title_match.group(1).strip() if title_match else f'{d}年408真题'
    text = re.sub(r'^# .+\n?', '', text, count=1)

    fm = f'''---
title: "{title}"
date: 2026-07-02
type: exam_collection
subject: "408"
source: "408真题"
year: {d}
difficulty: 3
tags: [真题, 408]
---

'''
    dst = os.path.join(DST, f'{d}.md')
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(fm + text.strip() + '\n')
    count += 1
    print(f'  OK {d}')

print(f'\nCopied {count} years')
