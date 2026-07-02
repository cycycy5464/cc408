#!/usr/bin/env python3
"""Restore exam content to exact csgraduates format (no folding, preserve tags)"""
import os, re

QUIZ_SRC = r'D:\内容整理\csgraduates-main\study_methods\408quiz'
QUIZ_DST = 'content/exam/408quiz'

for fname in os.listdir(QUIZ_SRC):
    if not os.path.isdir(os.path.join(QUIZ_SRC, fname)) or not fname.isdigit():
        continue
    src_file = os.path.join(QUIZ_SRC, fname, 'content.md')
    if not os.path.exists(src_file):
        continue

    with open(src_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove Source line
    text = re.sub(r'^> Source:.*\n?', '', text, flags=re.MULTILINE)
    # Remove B站 video link
    text = re.sub(r'^- \[.*精讲.*\]\(.*bilibili.*\)\s*\n?', '', text, flags=re.MULTILINE)

    # Keep the rest EXACTLY as csgraduates (answers visible, tags preserved)
    # Just remove the first "# Title" line since we add frontmatter
    text = re.sub(r'^# .+\n?', '', text, count=1)

    fm = f'''---
title: "{fname}年408真题"
date: 2026-07-01
type: exam_collection
subject: "408"
source: "408真题"
year: {fname}
difficulty: 3
tags: [真题, 408]
---

'''
    dst_file = os.path.join(QUIZ_DST, f'{fname}.md')
    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(fm + text.strip() + '\n')
    print(f'  OK {fname}')

print('\nDone')
