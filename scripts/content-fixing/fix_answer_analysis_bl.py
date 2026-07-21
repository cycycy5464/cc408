#!/usr/bin/env python3
"""
Fix: Add blank line between 正确答案：X line and following analysis text.
Without blank line, Goldmark merges them into one <p>, hiding analysis.
"""
import glob, re, os, sys

os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))

years = sys.argv[1:] if len(sys.argv) > 1 else ['2011']
total_fixed = 0

for year in years:
    files = sorted(glob.glob(f'content/question/{year}-*.md'))
    for fpath in files:
        with open(fpath, encoding='utf-8') as f:
            text = f.read()
        
        # Normalize CRLF
        text = re.sub(r'\r\n?', '\n', text)
        
        # Fix: 正确答案：X line followed directly by analysis (no blank line)
        new_text = re.sub(
            r'^(正确答案[：:]\s*[A-E]?)\n([^\n\[<#].+)',
            r'\1\n\n\2',
            text,
            flags=re.MULTILINE
        )
        
        if new_text != text:
            fname = os.path.basename(fpath)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_text)
            print(f"  {fname}: fixed 正确答案→analysis spacing")
            total_fixed += 1

print(f"\nTotal fixed: {total_fixed} files in {years}")
