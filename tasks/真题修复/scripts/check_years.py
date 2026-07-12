"""Check formatting issues for exam year question files."""
import glob, re, sys

years = sys.argv[1:] if len(sys.argv) > 1 else ['2011','2012']

for year in years:
    files = sorted(glob.glob(f'content/question/{year}-*.md'))
    if not files:
        print(f'=== {year}: no files found ===')
        continue
    print(f'=== {year}: {len(files)} files ===')
    
    found_issues = False
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            text = f.read()
        fname = fp.split('\\')[-1]
        issues = []
        
        is_comprehensive = 'question_type: "comprehensive"' in text
        
        if not is_comprehensive:
            if re.search(r'\[tag_link\]\n正确答案', text):
                issues.append('NO blank line: [tag_link]-正确答案')
            if re.search(r'正确答案[：:]\s*[ABCDabcd]\n(?!\n)', text, re.MULTILINE):
                issues.append('NO blank line after 正确答案')
            # Check if 4 options in one paragraph (no blank lines between them)
            if re.search(r'^[A-D]\\. .*\n[A-D]\\. ', text, re.MULTILINE):
                pass  # Good - multi-option in single p
            elif re.search(r'^[A-D]\\. .*\n\n[A-D]\\. ', text, re.MULTILINE):
                issues.append('blank lines between options')
        else:
            if '[tag_link]' not in text:
                issues.append('MISSING [tag_link]')
            elif not re.search(r'\[tag_link\]\n\n', text):
                issues.append('NO blank line after [tag_link]')
        
        if issues:
            found_issues = True
            print(f'  {fname}: {" | ".join(issues)}')
    
    if not found_issues:
        print('  (all clean)')
