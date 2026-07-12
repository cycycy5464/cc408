# coding: utf-8
import re

for n in ['012','013','014','015','016','017','018','019','020','021','022']:
    with open(f'content/question/2015-co-{n}.md', encoding='utf-8') as f:
        co_text = f.read()
    with open(f'content/question/2015-ds-{n}.md', encoding='utf-8') as f:
        ds_text = f.read()
    
    co_opts = len(re.findall(r'^[A-D][.\\\\]', co_text, re.MULTILINE))
    ds_opts = len(re.findall(r'^[A-D][.\\\\]', ds_text, re.MULTILINE))
    tag_co = co_text.count('[tag_link]')
    tag_ds = ds_text.count('[tag_link]')
    
    print(f'co-{n}: {co_opts} opts, tag={tag_co} | ds-{n}: {ds_opts} opts, tag={tag_ds}')
