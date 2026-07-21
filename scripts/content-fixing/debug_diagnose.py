# coding: utf-8
import os

YEAR = 2016
CONTENT_DIR = 'content/question'

for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    num_str = fn.split('-')[2].replace('.md', '')
    if int(num_str) > 40:
        continue
    with open(os.path.join(CONTENT_DIR, fn), encoding='utf-8') as fh:
        text = fh.read()
    lines = text.split('\n')
    
    # Check for backslash-option lines
    has_bs = False
    for l in lines:
        ls = l.strip()
        if ls[:2] in ['A.', 'B.', 'C.', 'D.']:
            has_bs = True
            break
    
    if has_bs:
        continue
    
    # Show what's in the body around tag_link
    if '[tag_link]' not in text:
        print(fn + ': no tag_link at all!')
        continue
    
    parts = text.split('---', 2)
    if len(parts) < 3:
        print(fn + ': no frontmatter?')
        continue
    body = parts[-1]
    tag_pos = body.find('[tag_link]')
    
    # Show 200 chars before [tag_link]
    start = max(0, tag_pos - 200)
    before = body[start:tag_pos]
    print(fn)
    print('  Before tag_link:', repr(before[-100:]))
    
    # Check crawl data for options
    import json
    with open('tasks/408-crawler/crawled_data/2016.json', encoding='utf-8') as fj:
        data = json.load(fj)
    q = data.get('questions', {}).get(num_str, {})
    opts = q.get('options', {}) if isinstance(q, dict) else {}
    if opts:
        print('  Crawl opts:', {k: v[:30] for k, v in opts.items()})
    else:
        print('  NO crawl opts!')
    print()
