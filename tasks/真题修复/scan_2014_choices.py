"""正确扫描 2014 选择题选项"""
import re, os, glob

base = 'D:/projet/cc408/cc408'
content_dir = os.path.join(base, 'content', 'question')

print("=== 2014 选择题扫描 ===")
files = sorted(glob.glob(os.path.join(content_dir, '2014-*.md')))
total = 0
problems = []
for f in files:
    bn = os.path.basename(f)
    num = int(bn.split('-')[2].replace('.md',''))
    if num > 40: continue
    total += 1
    
    with open(f, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    
    # 匹配 A\. 格式（带反斜杠）
    opts = [l.strip() for l in lines if re.match(r'^[A-D]\\.', l.strip())]
    
    if len(opts) != 4:
        problems.append((bn, len(opts), opts))
    elif len(set(o[0] for o in opts)) != 4:
        letters = [o[0] for o in opts]
        problems.append((bn, letters, opts))

if problems:
    print(f"\n⚠️ {len(problems)} 个问题文件:")
    for bn, detail, opts in problems:
        print(f"  {bn}: {detail}")
        for o in opts:
            print(f"    {o[:60]}")
else:
    print(f"✅ {total}/{total} 均正常（4个不同字母选项）")
