#!/usr/bin/env python3
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

years_to_check = ['2010', '2018', '2020', '2025']
subjects_to_check = {
    '2010': [('操作系统', 45), ('计算机网络', 47)],
    '2018': [('计算机网络', 47)],
    '2020': [('计算机网络', 47)],
    '2025': [('计算机组成原理', 44), ('数据结构', 42)],
}

for year in years_to_check:
    with open(f'content/exam/408quiz/backup/{year}-content.md', 'rb') as f:
        t = f.read().decode('utf-8')
    
    print(f'\n=== {year} ===')
    
    # Find all #### headings (comprehensive question subjects)
    for m in re.finditer(r'^#### (.+)$', t, re.MULTILINE):
        section_start = m.start()
        section_name = m.group(1)
        
        # Find all questions in this section
        section_text = t[section_start:]
        for qm in re.finditer(r'^##### (\d+)$', section_text, re.MULTILINE):
            qnum = int(qm.group(1))
            print(f'  {section_name} section -> Question #{qnum}')
