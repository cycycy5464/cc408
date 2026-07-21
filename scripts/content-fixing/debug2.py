# coding: utf-8
import json, os

YEAR = 2016
CONTENT_DIR = 'content/question'
CRAWL_FILE = f'tasks/408-crawler/crawled_data/{YEAR}.json'

with open(CRAWL_FILE, encoding='utf-8') as f:
    data = json.load(f)

questions = data.get('questions', {})

# Test for 2016-ds-001
fn = '2016-ds-001.md'
# option check
with open(os.path.join(CONTENT_DIR, fn), encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
has_opts = any(l.strip()[:2] in ['A.', 'B.', 'C.', 'D.'] for l in lines)
print(f'{fn}: has_opts = {has_opts}')

num_str = '001'
num_int = int(num_str)
key = str(num_int)
print(f'num_int={num_int}, key="{key}"')
print(f'questions has key? {key in questions}')
q = questions.get(key, 'NONE')
print(f'Q[key] type = {type(q)}')
opts = q.get('options', {}) if isinstance(q, dict) else {}
print(f'opts = {opts}')
print("opts keys:", list(opts.keys()) if isinstance(opts, dict) else 'NOT_DICT')

# Check all files
print('\n--- All files check ---')
for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    num_str = fn.split('-')[2].replace('.md', '')
    num_int = int(num_str)
    if num_int > 40:
        continue
    with open(os.path.join(CONTENT_DIR, fn), encoding='utf-8') as f:
        text = f.read()
    has_opts = any(l.strip()[:2] in ['A.', 'B.', 'C.', 'D.'] for l in text.split('\n'))
    key = str(num_int)
    q = questions.get(key, None)
    has_opts_in_json = False
    if q and isinstance(q, dict):
        opts = q.get('options', {})
        has_opts_in_json = bool(opts and isinstance(opts, dict))
    if not has_opts and not has_opts_in_json:
        print(f'  {fn}: no opts in file, no opts in JSON either!')
    elif not has_opts:
        print(f'  {fn}: no opts in file BUT has opts in JSON ({[opts.get(k,"")[:20] for k in "ABCD"] if isinstance(opts,dict) else "?"})')
