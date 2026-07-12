# coding: utf-8
import re
fns = ['2015-ds-013.md', '2015-ds-015.md', '2015-ds-016.md', '2015-ds-018.md']
for fn in fns:
    with open('content/question/' + fn, encoding='utf-8') as f:
        text = f.read()
    # Count each letter's occurrences at line start with A. or A\. format
    opts_a = len(re.findall(r'^A[.\\\\]', text, re.MULTILINE))
    opts_b = len(re.findall(r'^B[.\\\\]', text, re.MULTILINE))
    opts_c = len(re.findall(r'^C[.\\\\]', text, re.MULTILINE))
    opts_d = len(re.findall(r'^D[.\\\\]', text, re.MULTILINE))
    total = opts_a + opts_b + opts_c + opts_d
    print(f'{fn}: A={opts_a} B={opts_b} C={opts_c} D={opts_d} total={total}')
