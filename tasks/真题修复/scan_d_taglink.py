#!/usr/bin/env python3
"""DEBUG: scan D → [tag_link] pattern in 2011 files"""
import glob, re, os

os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))

for fpath in sorted(glob.glob('content/question/2011-*.md')):
    with open(fpath, encoding='utf-8') as f:
        text = f.read()
    
    # Find [tag_link] position
    if '[tag_link]' not in text:
        continue
    
    idx = text.index('[tag_link]')
    # Show 80 chars before [tag_link]
    before = text[max(0, idx-80):idx]
    lines_before = before.split('\n')
    last_line = lines_before[-1] if lines_before else ''
    
    fname = os.path.basename(fpath)
    print(f"{fname}:")
    print(f"  Last line before [tag_link]: |{last_line}|")
    
    # Check if starts with D or D\.
    if last_line.startswith('D') or last_line.startswith('D\\'):
        print(f"  ❌ D-option not separated from [tag_link]!")
        # Show full context
        ctx = text[max(0, idx-200):idx+50]
        print(f"  Context: {repr(ctx)}")
    print()
