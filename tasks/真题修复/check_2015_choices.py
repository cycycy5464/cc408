import glob, re, os

content_dir = 'content/question'
files = sorted(glob.glob(os.path.join(content_dir, '2015-*.md')))
print(f'总文件数: {len(files)}')

choice_ok = 0
fail = []
for f in files:
    bn = os.path.basename(f)
    num = int(bn.split('-')[2].replace('.md',''))
    if num > 40:
        continue
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    parts = text.split('---', 2)
    body = parts[-1] if len(parts) >= 3 else text

    # 匹配 A\. xxx 或 A. xxx
    pattern = r'^([A-D])\\\.\s+(.*)'  # A\. 格式
    opts = re.findall(pattern, body, re.MULTILINE)
    if not opts:
        pattern = r'^([A-D])\.\s+(.*)'  # A. 格式
        opts = re.findall(pattern, body, re.MULTILINE)

    opts = [o for o in opts if o[1].strip()]
    n = len(opts)
    if n == 4:
        choice_ok += 1
    else:
        fail.append((bn, n, opts))

print(f'\n选择题4选项: {choice_ok}/{choice_ok+len(fail)}')
for bn, n, opts in fail:
    print(f'  {bn}: {n}个选项')
    for o in opts:
        print(f'    {o[0]}. {o[1][:50]}')
