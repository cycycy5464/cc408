#!/usr/bin/env python3
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Check encoding of backup and question files
files = [
    'content/exam/408quiz/backup/2010-content.md',
    'content/exam/408quiz/backup/2018-content.md',
    'content/exam/408quiz/backup/2020-content.md',
    'content/exam/408quiz/backup/2025-content.md',
    'content/question/2009-ds-001.md',
]

for fpath in files:
    if not os.path.exists(fpath):
        print(f'{fpath}: NOT FOUND')
        continue
    with open(fpath, 'rb') as f:
        raw = f.read()
    
    # Try different encodings
    for enc in ['utf-8', 'gbk', 'gb2312', 'gb18030', 'utf-16']:
        try:
            text = raw.decode(enc)
            # Check if it has recognizable Chinese
            has_chinese = any('\u4e00' <= c <= '\u9fff' for c in text)
            if has_chinese:
                # Show sample
                sample = text[200:400]
                print(f'{fpath}: valid {enc}, has Chinese chars')
                print(f'  Sample: {sample[:100]}...')
                break
        except:
            continue
    else:
        print(f'{fpath}: could not decode with any encoding')
        print(f'  First 40 bytes: {raw[:40].hex(" ")}')
    
    print()
