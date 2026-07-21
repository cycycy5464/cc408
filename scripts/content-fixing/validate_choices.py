"""
验证选择题选项完整性：检查选项数是否为 4 且内容非空
用法：python validate_choices.py [年份...]
      python validate_choices.py 2014 2015
      python validate_choices.py --all
"""
import re, os, sys, glob, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(BASE, 'content', 'question')

YEARS = sys.argv[1:] if len(sys.argv) > 1 else ['2014']

check_all = '--all' in YEARS
if check_all:
    YEARS.remove('--all')
    YEARS = [str(y) for y in range(2009, 2027)]

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

for Y in YEARS:
    files = sorted(glob.glob(os.path.join(CONTENT_DIR, f'{Y}-*.md')))
    if not files:
        continue
    year_errors = 0
    for f in files:
        bn = os.path.basename(f)
        num = int(bn.split('-')[2].replace('.md',''))
        if num > 40:
            continue
        
        with open(f, encoding='utf-8') as fh:
            lines = fh.read().split('
')
        
        opt_lines = [l for l in lines if re.match(r'^[A-D]\.', l.strip()) or re.match(r'^[A-D]\.\.', l.strip())]
        
        if len(opt_lines) != 4:
            print(f"  [行数] {Y} {bn}: {len(opt_lines)} 个选项")
            year_errors += 1
            continue
        
        for l in opt_lines:
            after = l.split('.', 1)[1].strip() if '.' in l else ''
            if not after:
                print(f"  [空] {Y} {bn}: {l[0]}. 空内容")
                year_errors += 1
            elif 'katex' in after and BeautifulSoup:
                plain = BeautifulSoup(after, 'html.parser').get_text(separator=' ').strip()
                if not plain:
                    print(f"  [KaTeX空] {Y} {bn}: {l[0]}. 空")
                    year_errors += 1
    
    if year_errors == 0:
        print(f"  {Y}: ✅")
    else:
        print(f"  {Y}: {year_errors} 个问题")

if check_all:
    print("
全局检查完成")