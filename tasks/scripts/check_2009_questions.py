#!/usr/bin/env python3
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')
base = 'content/question'
files = sorted(f for f in os.listdir(base) if f.startswith('2009-') and f.endswith('.md'))
print(f'Total 2009 files: {len(files)}')
for f in files:
    fp = os.path.join(base, f)
    with open(fp, 'rb') as fh:
        raw = fh.read().decode('utf-8', errors='replace')
    # Extract frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---', raw, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        # Parse YAML manually (no yaml module available)
        import json
        years = re.search(r'years:\s*\[(.*?)\]', fm_text)
        years_val = [y.strip().strip('"\'') for y in years.group(1).split(',')] if years else []
        subjects = re.search(r'subjects:\s*\[(.*?)\]', fm_text)
        subj_val = [s.strip().strip('"\'') for s in subjects.group(1).split(',')] if subjects else []
        number = re.search(r'number:\s*(\d+)', fm_text)
        num_val = number.group(1) if number else '?'
        print(f'  {f}: years={years_val} num={num_val} subj={subj_val}')
