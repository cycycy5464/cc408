"""Validate question file completeness for given years."""
import glob, re, sys, os

script_dir = os.path.dirname(os.path.abspath(__file__))
question_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..', 'content', 'question'))
years = sys.argv[1:] if len(sys.argv) > 1 else ['2011','2012']

for year in years:
    files = sorted(glob.glob(os.path.join(question_dir, f'{year}-*.md')))
    print(f'=== {year}: {len(files)} files ===')
    
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            text = f.read()
        fname = os.path.basename(fp)
        body_start = text.find('---', text.find('---') + 3)
        body = text[body_start+3:] if body_start > 0 else text
        issues = []
        
        is_choice = 'question_type: "choice"' in text
        is_comp = 'question_type: "comprehensive"' in text
        
        # Check frontmatter fields
        for field in ['title:', 'type:', 'years:', 'subjects:', 'question_type:', 'number:']:
            if field not in text.split('---')[1] if '---' in text else '':
                issues.append(f'missing frontmatter: {field}')
        
        if is_choice:
            # Check for 正确答案
            if not re.search(r'正确答案[：:]\s*[ABCDabcd]', text):
                issues.append('MISSING 正确答案')
            else:
                # Check 解析 is non-empty (content after 正确答案 line)
                m = re.search(r'正确答案[：:]\s*[ABCDabcd]', text)
                after_answer = text[m.end():].strip()
                if not after_answer or len(after_answer) < 5:
                    issues.append('EMPTY 解析')
            
            # Count options (A/B/C/D lines)
            option_lines = re.findall(r'^[A-D]\\?\.', text, re.MULTILINE)
            opt_count = len(set(option_lines))
            if opt_count < 4:
                issues.append(f'options count: {opt_count}/4')
            
            # Check empty option text
            empty_opts = re.findall(r'^[A-D]\\\.\s*$', text, re.MULTILINE)
            if empty_opts:
                issues.append(f'{len(empty_opts)} empty option(s)')
            
            # Check body not empty
            body_text = body.strip()
            if not body_text or len(body_text) < 20:
                issues.append('EMPTY body')
                
        elif is_comp:
            # Check for [tag_link]
            if '[tag_link]' not in text:
                issues.append('MISSING [tag_link]')
            else:
                # Check 解析 after [tag_link] is non-empty
                idx = text.rfind('[tag_link]')
                after = text[idx + len('[tag_link]'):].strip()
                if not after or len(after) < 10:
                    issues.append('EMPTY 解析')
            
            # Check body not empty
            body_text = body.strip()
            if not body_text or len(body_text) < 20:
                issues.append('EMPTY body')
        
        if issues:
            print(f'  {fname}:')
            for iss in issues:
                print(f'    - {iss}')
