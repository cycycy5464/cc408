#!/usr/bin/env python3
"""Scan for missing blank lines between sections in 2011 files"""
import glob, re, os

os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
found = 0

for fpath in sorted(glob.glob('content/question/2011-*.md')):
    with open(fpath, encoding='utf-8') as f:
        text = f.read()
    text_norm = text.replace('\r\n', '\n')
    lines = text_norm.split('\n')
    
    issues = []
    
    for i, line in enumerate(lines):
        # Check 1: [tag_link] followed by 正确答案 without blank line
        if line.strip() == '[tag_link]':
            nxt = lines[i+1] if i+1 < len(lines) else ''
            if nxt.strip() and not nxt.startswith('['):
                # Next line is non-blank and not another tag
                if '正确' not in nxt:
                    # Wait for 正确答案; skip if next line is content
                    pass
            continue
        
        # Check 2: 正确答案 line followed by analysis without blank line
        if '正确答案' in line:
            nxt = lines[i+1] if i+1 < len(lines) else ''
            if nxt.strip() and nxt.strip().startswith(('1）', '2）', '3）', '4）', '5）')):
                issues.append(f"L{i}: 正确答案 + sub-question without blank line: {nxt.strip()[:40]}")
            elif nxt.strip() and nxt.strip() not in ['[tag_link]', ''] and not nxt.strip().startswith('#') and not nxt.strip().startswith('['):
                # Could be analysis content directly
                pass
        
        # Check 3: option line D followed by analysis (not [tag_link])
        if line.startswith('D\\'):
            nxt = lines[i+1] if i+1 < len(lines) else ''
            if nxt.strip() and not nxt.strip() == '[tag_link]':
                issues.append(f"L{i}: D-option + non-[tag_link] without blank line: {nxt.strip()[:40]}")
    
    if issues:
        found += 1
        fname = os.path.basename(fpath)
        for iss in issues:
            print(f"  {fname}: {iss}")

print(f"\nTotal files with issues: {found}")
