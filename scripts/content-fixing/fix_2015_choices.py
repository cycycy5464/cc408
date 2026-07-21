#!/usr/bin/env python3
"""修复 2015 年真题：从爬虫数据恢复选择题选项"""

import glob, os, re, json

content_dir = 'content/question'
crawl_file = 'tasks/408-crawler/crawled_data/2015.json'

# 加载爬虫数据
with open(crawl_file, encoding='utf-8') as f:
    crawl = json.load(f)

questions = crawl.get('questions', {})
explanations = crawl.get('explanations', {})
solutions = crawl.get('solutions', {})

files = sorted(glob.glob(os.path.join(content_dir, '2015-*.md')))
print(f'找到 {len(files)} 个文件')

fixed = []
for f in files:
    bn = os.path.basename(f)
    num = int(bn.split('-')[2].replace('.md',''))
    if num > 40:
        continue  # 跳过综合题
    num_str = str(num)
    
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    
    # 检查是否有 4 个选项
    body = text.split('---', 2)[-1] if text.count('---') >= 2 else text
    existing_opts = re.findall(r'^([A-D])\\.\s+(.*)', body, re.MULTILINE)
    if not existing_opts:
        existing_opts = re.findall(r'^([A-D])\.\s+(.*)', body, re.MULTILINE)
    existing_opts = [o for o in existing_opts if o[1].strip()]
    
    if len(existing_opts) == 4:
        continue  # 已 OK
    
    # 从爬虫数据恢复
    q = questions.get(num_str)
    if not q:
        print(f'  ⚠ {bn}: 爬虫无数据')
        continue
    
    opts = q.get('options', {})
    if not opts or len(opts) < 4:
        print(f'  ⚠ {bn}: 爬虫选项不足')
        continue
    
    # 构造选项行
    opt_lines = []
    for letter in ['A', 'B', 'C', 'D']:
        txt = opts.get(letter, '')
        opt_lines.append(f'{letter}\\. {txt}')
    
    # 找到插入位置：在题干之后、[tag_link] 之前
    tag_pos = text.find('[tag_link]')
    if tag_pos == -1:
        print(f'  ⚠ {bn}: 无 [tag_link]，跳过')
        continue
    
    # 删除所有旧的选项行（A.xxx / A\.xxx）
    lines = text.split('\n')
    new_lines = []
    in_options = False
    for line in lines:
        s = line.strip()
        if re.match(r'^[A-D][\\\.]\s', s):
            in_options = True
            continue
        elif s == '' and in_options:
            # 跳过空行直到非空
            continue
        else:
            if in_options and not re.match(r'^[A-D]', s):
                in_options = False
            new_lines.append(line)
    
    if in_options:
        in_options = False
    
    # 重新组装，在 [tag_link] 前插入新选项
    result = '\n'.join(new_lines)
    
    # 找 [tag_link] 在 result 中的位置
    tag_pos2 = result.find('[tag_link]')
    
    # 获取 tag_link 前的行，看是否需要空行
    before = result[:tag_pos2].rstrip()
    new_opts_text = '\n'.join(opt_lines)
    
    # 确保选项前有空行（不紧接题干）
    if before.endswith('\n') and not before.rstrip('\n').endswith('\n\n'):
        new_body = before + '\n' + new_opts_text + '\n\n' + result[tag_pos2:]
    else:
        new_body = before + '\n\n' + new_opts_text + '\n\n' + result[tag_pos2:]
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(new_body)
    
    # 验证
    body2 = new_body.split('---', 2)[-1] if new_body.count('---') >= 2 else new_body
    final_opts = re.findall(r'^([A-D])\\.\s+(.*)', body2, re.MULTILINE)
    final_n = len(final_opts)
    if final_n == 4:
        fixed.append((bn, 'OK'))
    else:
        fixed.append((bn, f'{final_n} options'))

print(f'\n修复结果:')
for bn, status in fixed:
    print(f'  {bn}: {status}')
print(f'\n共修复 {len(fixed)} 个文件')
