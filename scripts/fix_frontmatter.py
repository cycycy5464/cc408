#!/usr/bin/env python3
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

SUBJECT_MAP = {'ds': '数据结构', 'co': '计算机组成原理', 'os': '操作系统', 'cn': '计算机网络'}

base = 'content/question'
fixed = 0

for fname in sorted(os.listdir(base)):
    if not fname.endswith('.md'):
        continue
    m = re.match(r'(\d{4})-([a-z]+)-(\d+)\.md', fname)
    if not m:
        continue
    year_str = m.group(1)
    subj_code = m.group(2)
    subject = SUBJECT_MAP.get(subj_code)
    if not subject:
        print('  SKIP (unknown subj): ' + fname)
        continue

    fp = os.path.join(base, fname)
    with open(fp, 'rb') as fh:
        raw = fh.read().decode('utf-8', errors='replace')

    # Parse frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---', raw, re.DOTALL)
    if not fm_match:
        print('  SKIP (no fm): ' + fname)
        continue

    fm_text = fm_match.group(1)
    body = raw[fm_match.end():]
    changes = []

    # Fix years
    years_re = re.search(r'years:\s*\[(.*?)\]', fm_text)
    if years_re:
        existing_years = [y.strip().strip('"\'') for y in years_re.group(1).split(',') if y.strip()]
        if year_str not in existing_years:
            all_years = existing_years + [year_str]
            quoted = ', '.join('"' + y + '"' for y in all_years)
            fm_text = fm_text.replace(years_re.group(0), 'years: [' + quoted + ']')
            changes.append('years: added ' + year_str)
    else:
        changes.append('NO years field found')
        print('  ISSUE: ' + fname + ' has no years field')

    # Fix subjects
    subj_re = re.search(r'subjects:\s*\[(.*?)\]', fm_text)
    if subj_re:
        existing_subjs = [s.strip().strip('"\'') for s in subj_re.group(1).split(',') if s.strip()]
        if subject not in existing_subjs:
            all_subjs = existing_subjs + [subject]
            quoted = ', '.join('"' + s + '"' for s in all_subjs)
            fm_text = fm_text.replace(subj_re.group(0), 'subjects: [' + quoted + ']')
            changes.append('subjects: added ' + subject)
    else:
        changes.append('NO subjects field found')
        print('  ISSUE: ' + fname + ' has no subjects field')

    if changes:
        new_content = '---\n' + fm_text + '\n---' + body
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1
        if fixed <= 5 or '2010' in fname:
            print('  FIXED ' + fname + ': ' + '; '.join(changes))

print('\nTotal fixed: ' + str(fixed))
