# coding: utf-8
import os

YEAR = 2016
CONTENT_DIR = 'content/question'

for fn in sorted(os.listdir(CONTENT_DIR)):
    if not fn.startswith(str(YEAR) + '-'):
        continue
    num = int(fn.split('-')[2].replace('.md', ''))
    if num < 41:
        continue
    fp = os.path.join(CONTENT_DIR, fn)
    with open(fp, encoding='utf-8') as fh:
        text = fh.read()
    if '[tag_link]' in text:
        continue
    
    # Find answer section start
    ans_pos = text.find('正确答案')
    if ans_pos < 0:
        # Search for analysis section keywords
        keywords = ['【解析】', '【解答】', '参考', '本题考查', '本题考察']
        ans_pos = -1
        for kw in keywords:
            p = text.find(kw)
            if p > 0:
                ans_pos = p
                break
    
    if ans_pos < 0:
        # Insert before the last non-empty section
        lines = text.split('\n')
        # Find the --- after frontmatter
        fm_count = 0
        insert_pos = 0
        for i, l in enumerate(lines):
            if l.strip() == '---':
                fm_count += 1
                if fm_count == 2:
                    insert_pos = i + 1
                    break
        # Then find a blank line after first few content lines
        for i in range(insert_pos, len(lines)):
            if not lines[i].strip() and i+1 < len(lines) and lines[i+1].strip():
                # Insert [tag_link] here
                lines.insert(i, '[tag_link]')
                text = '\n'.join(lines)
                with open(fp, 'w', encoding='utf-8') as fh:
                    fh.write(text)
                print('{}: inserted [tag_link] at line {}'.format(fn, i+1))
                break
        continue
    
    # Insert before answer
    before = text[:ans_pos].rstrip()
    after = text[ans_pos:]
    new_text = before + '\n\n[tag_link]\n\n' + after
    with open(fp, 'w', encoding='utf-8') as fh:
        fh.write(new_text)
    print('{}: inserted [tag_link] before answer'.format(fn))
