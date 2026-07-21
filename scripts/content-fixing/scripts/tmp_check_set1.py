import glob, re, os

files = sorted(glob.glob('content/question/simulate-1-*.md'))
print('=== 含“图”且未引用图片的 set-1 文件 / 题号映射 ===')
for f in files:
    t = open(f, encoding='utf-8').read()
    m = re.search(r'(\d+)\s*（', t[:400])
    qn = m.group(1) if m else '?'
    has_img = '![' in t
    mentions_fig = ('图' in t)
    if mentions_fig and not has_img:
        print('%-28s 题号=%s  提及图但无图引用' % (os.path.basename(f), qn))

print()
print('=== 搜索 Qx svg 是否被任何 md 引用 ===')
qx = sorted(glob.glob('static/images/questions/simulate/simulate_1/Qx_*.svg'))
allmd = glob.glob('content/**/*.md', recursive=True)
for q in qx:
    base = os.path.basename(q)
    hits = []
    for cf in allmd:
        if base in open(cf, encoding='utf-8', errors='ignore').read():
            hits.append(os.path.basename(cf))
    print('%-12s 被引用: %s' % (base, hits if hits else '无'))

print()
print('=== set-1 各文件题号提取（前若干） ===')
for f in files[:6]:
    t = open(f, encoding='utf-8').read()
    m = re.search(r'(\d+)\s*（', t[:400])
    print(os.path.basename(f), '->', m.group(1) if m else '?')
