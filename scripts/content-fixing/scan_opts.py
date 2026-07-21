"""检测选择题选项行数（含 A. 和 A\. 两种格式）"""
import re, os, glob

BASE = 'D:/projet/cc408/cc408'
CONTENT = os.path.join(BASE, 'content', 'question')

for year in ['2014']:
    files = sorted(glob.glob(os.path.join(CONTENT, f'{year}-*.md')))
    for f in files:
        bn = os.path.basename(f)
        num = int(bn.split('-')[2].replace('.md',''))
        if num > 40: 
            continue
        
        with open(f, encoding='utf-8') as fh:
            raw = fh.read()
        lines = raw.split('\n')
        
        # 检测所有以 A/B/C/D 开头且第二个字符是 . 或 \. 的行
        opt_lines = []
        for i, l in enumerate(lines):
            s = l.strip()
            if len(s) < 2:
                continue
            # A. 或 A\.
            if s[0] in 'ABCD' and s[1] == '.':
                opt_lines.append((i, s))
            elif len(s) >= 3 and s[0] in 'ABCD' and s[1] == '\\' and s[2] == '.':
                opt_lines.append((i, s))
        
        if len(opt_lines) != 4:
            info = f"  >>> {year} {bn}: {len(opt_lines)} 行"
            for i, l in opt_lines:
                info += f"\n      行{i+1}: |{l[:60]}|"
            print(info)
        # 显示前十道题供确认
        elif num <= 5:
            texts = [l.split('.', 1)[1].strip()[:25] if '.' in l else '?' for _, l in opt_lines]
            print(f"  OK {year} {bn}: {texts}")
    
    print(f"\n{year} 扫描完成")
