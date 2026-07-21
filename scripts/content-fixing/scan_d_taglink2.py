#!/usr/bin/env python3
"""Deep scan: check D-option and [tag_link] formatting in choice questions"""
import glob, re, os

os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))

for fpath in sorted(glob.glob('content/question/2011-*.md')):
    with open(fpath, encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    fname = os.path.basename(fpath)
    
    # Find [tag_link] lines
    for i, line in enumerate(lines):
        if '[tag_link]' in line:
            # Check what's 1-2 lines before
            prev1 = lines[i-1].strip() if i > 0 else ''
            prev2 = lines[i-2].strip() if i > 1 else ''
            
            if prev1.startswith('D') or prev1.startswith('D\\') or prev1.startswith('D.'):
                print(f"❌ {fname}: D + [tag_link] adjacent!")
                print(f"   Line {i-1}: {prev1[:80]}")
                print(f"   Line {i}:   {line[:80]}")
            elif prev1 == '' and (prev2.startswith('D') or prev2.startswith('D\\') or prev2.startswith('D.')):
                # Already has blank line - OK
                pass
            elif prev1 == '' and (prev2 == '' or prev2 == ''):
                # Double blank line - OK
                pass
            
            # Show first 3 matches context
            check_around = lines[max(0,i-4):i+2]
            for ci, cl in enumerate(check_around):
                if 'D.' in cl or 'D\\' in cl or '[tag_link]' in cl:
                    print(f"   [{i-4+ci}] {cl[:70]}")
            break
