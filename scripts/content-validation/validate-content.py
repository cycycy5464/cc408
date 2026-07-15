#!/usr/bin/env python3
"""Validate cc408 content frontmatter - pure Python (no PyYAML)"""
import os, re, sys

CONTENT = 'content'
ALLOWED_SUBJECTS = {'data-structure', 'computer-org', 'os', 'network'}

issues = []

def parse_fm(text):
    """Simple frontmatter parser for Hugo YAML subset."""
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().split('\n'):
        m = re.match(r'^(\w+):\s*(.+)$', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip().strip('"\'')
            if val.startswith('[') and val.endswith(']'):
                inner = val[1:-1].strip()
                val = [v.strip().strip('"\'').strip(',') for v in inner.split(',') if v.strip()] if inner else []
            fm[key] = val
    return fm

for root, dirs, files in os.walk(CONTENT):
    for fname in files:
        if not fname.endswith('.md') or fname == '_index.md':
            continue
        path = os.path.join(root, fname)
        rel = os.path.relpath(path, CONTENT)
        with open(path, 'r', encoding='utf-8') as f:
            fm = parse_fm(f.read())

        # Check docs subject
        if rel.startswith('docs/'):
            s = fm.get('subject')
            if type(s) == str and s not in ALLOWED_SUBJECTS:
                issues.append(f'  Invalid subject "{s}" in {rel}')

        # Check exam subject
        if rel.startswith('exam/'):
            s = fm.get('subject')
            if type(s) == str and s not in ALLOWED_SUBJECTS and s != '408':
                issues.append(f'  Invalid subject "{s}" in exam {rel}')
            # Check quiz/sim have exam_collection type
            if rel.startswith('exam/408quiz') or rel.startswith('exam/simulate'):
                if fm.get('type') != 'exam_collection':
                    issues.append(f'  {rel} should have type=exam_collection, got {fm.get("type")}')

if issues:
    print(f'\nFound {len(issues)} issue(s):')
    for i in issues:
        print(i)
    sys.exit(1)
else:
    print('All content files passed validation OK')
