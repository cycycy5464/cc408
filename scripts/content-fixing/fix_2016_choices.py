# coding: utf-8
import json, os

YEAR = 2016
CONTENT_DIR = 'content/question'
CRAWL_FILE = f'tasks/408-crawler/crawled_data/{YEAR}.json'

with open(CRAWL_FILE, encoding='utf-8') as f:
    data = json.load(f)

questions = data.get('questions', {})

fixed = 0
for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    num_str = fn.split('-')[2].replace('.md', '')
    num_int = int(num_str)
    if num_int > 40:
        continue
    
    fp = os.path.join(CONTENT_DIR, fn)
    with open(fp, encoding='utf-8') as fh:
        text = fh.read()
    
    # Check if option lines already exist (A. B. C. D. at start of line)
    lines = text.split('\n')
    has_opts = any(l.strip()[:2] in ['A.', 'B.', 'C.', 'D.'] for l in lines)
    if has_opts:
        continue
    
    q = questions.get(str(num_int), {})
    opts = q.get('options', {}) if isinstance(q, dict) else {}
    if not opts or not isinstance(opts, dict):
        continue
    if not all(k in opts for k in 'ABCD'):
        continue
    
    # Find [tag_link] - simple text search
    tag_idx = text.find('[tag_link]')
    if tag_idx < 0:
        continue
    
    # Build options block
    opt_lines = ''
    for letter in 'ABCD':
        opt_text = opts[letter]
        opt_lines += letter + '\\. ' + opt_text + '\n'
    
    # Find the start of the line containing [tag_link]
    # Go backwards from tag_idx to find the start of the line
    line_start = text.rfind('\n', 0, tag_idx)
    if line_start < 0:
        line_start = 0
    else:
        line_start += 1  # skip the newline
    
    # The part before [tag_link] line
    before_tag = text[:line_start].rstrip()
    after_tag = text[tag_idx:]  # includes [tag_link]
    
    new_text = before_tag + '\n\n' + opt_lines + '\n' + after_tag
    
    with open(fp, 'w', encoding='utf-8') as fh:
        fh.write(new_text)
    fixed += 1
    print(f'Fixed {fn}: {list(opts.values())}')

print(f'\nTotal: {fixed} files fixed')
