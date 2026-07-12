"""Fix question files for given years according to rendering rules.

Rules applied:
1. Choice: [tag_link] --blank--> 正确答案 --blank--> analysis
2. Comprehensive: insert [tag_link] before analysis (numbered answer)
"""
import glob, re, sys, os

question_dir = os.path.join(os.path.dirname(__file__), '..', 'content', 'question')
years = sys.argv[1:] if len(sys.argv) > 1 else ['2011','2012']

for year in years:
    files = sorted(glob.glob(os.path.join(question_dir, f'{year}-*.md')))
    fixed = {'choice': 0, 'comp': 0}
    
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            text = f.read()
        
        original = text
        fname = os.path.basename(fp)
        is_comprehensive = 'question_type: "comprehensive"' in text
        
        kind = None
        if not is_comprehensive:
            text = re.sub(
                r'(\[tag_link\])\n(正确答案[：:])',
                r'\1\n\n\2',
                text
            )
            text = re.sub(
                r'(正确答案[：:]\s*[ABCDabcd])\n(?!\n)',
                r'\1\n\n',
                text,
                flags=re.MULTILINE
            )
            if text != original:
                kind = 'choice'
        else:
            if '[tag_link]' not in text:
                parts = text.split('---', 2)
                if len(parts) == 3:
                    body = parts[2]
                    # Find last tag link, insert [tag_link] after it before the answer
                    last_tag = body.rfind('/study_methods/tags/408quiz/')
                    if last_tag >= 0:
                        eol = body.find('\n', last_tag)
                        if eol >= 0:
                            after_tags = body[eol:]
                            for marker in ['\n(1)', '\n1）', '\n1)']:
                                idx = after_tags.find(marker)
                                if idx >= 0:
                                    body = body[:eol] + '\n\n[tag_link]' + after_tags[:idx] + after_tags[idx:]
                                    text = '---'.join(parts[:2]) + '---' + body
                                    kind = 'comp'
                                    break

        if kind:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(text)
            fixed[kind] += 1
            print(f'  [{kind}] {fname}')
    
    total = fixed['choice'] + fixed['comp']
    print(f'{year}: {fixed["choice"]} choice + {fixed["comp"]} comprehensive = {total}')
