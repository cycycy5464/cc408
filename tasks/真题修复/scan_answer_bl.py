#!/usr/bin/env python3
"""Scan 2011 files for [tag_link]-正确答案 blank line issues"""
import glob, os

os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))

issues = []
for fpath in sorted(glob.glob('content/question/2011-*.md')):
    bn = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        text = f.read()
    text_norm = text.replace('\r\n', '\n')
    lines = text_norm.split('\n')
    
    for i, line in enumerate(lines):
        # [tag_link] followed directly by non-blank (except 正确答案)
        if line.strip() == '[tag_link]' and i+1 < len(lines):
            nxt = lines[i+1].strip()
            if nxt and not nxt.startswith('正确答案'):
                pass  # Other content after tag is OK
        
        if line.strip() == '[tag_link]' and i+1 < len(lines):
            nxt = lines[i+1].strip()
            if nxt.startswith('正确答案'):
                pass  # Has blank line (nxt is on its own line after [tag_link])
            elif nxt:
                # nxt is not blank and not 正确答案
                # Check if there's a blank line before [tag_link]
                pass
        
        # Check: consecutive non-blank lines after [tag_link] area
        if line.strip() == '正确答案：' or line.strip().startswith('正确答案'):
            if i+1 < len(lines):
                nxt = lines[i+1].strip()
                if nxt and not nxt.startswith(('```', '', '#')):
                    # Analysis starts right after 正确答案 - need blank line for Goldmark
                    if nxt.startswith(('1）', '2）', '3）', '4）', '（1）', '（2）', '【', '本题')):
                        issues.append(f"{bn}: 正确答案→sub-question no blank line: L{i}→{nxt[:30]}")
                    elif len(nxt) > 5:
                        issues.append(f"{bn}: 正确答案→analysis no blank line: L{i}→{nxt[:40]}")

for iss in sorted(issues):
    print(f"  {iss}")
if not issues:
    print("No issues found.")
