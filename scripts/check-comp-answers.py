#!/usr/bin/env python3
"""Check why comprehensive answers are not found"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import zipfile
import xml.etree.ElementTree as ET
import re

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
docx_path = r"D:\BaiduSyncdisk\考研相关\ppt\os27\os\os章节\第3章_内存管理.docx"

paragraphs = []
with zipfile.ZipFile(docx_path) as z:
    xml_content = z.read("word/document.xml")
root = ET.fromstring(xml_content)
for p in root.findall(".//w:p", NS):
    texts = []
    for r in p.findall(".//w:r", NS):
        for t in r.findall("w:t", NS):
            if t.text:
                texts.append(t.text)
    line = "".join(texts).strip()
    if line:
        paragraphs.append(line)

# Check the range 3249-3585
print("=== Checking range 3249-3585 ===")
choice_count = 0
comp_count = 0
in_comp = False

pattern = r"^(\d{1,2})[.．]\s*【(解答|解)】"

for i in range(3249, 3585):
    line = paragraphs[i]
    if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
        choice_count += 1
        in_comp = False
    elif re.match(pattern, line):
        in_comp = True
        comp_count += 1
        print(f"  [{i}] MATCH: {repr(line[:50])}")
    elif in_comp:
        comp_count += 1
    else:
        in_comp = False

print(f"\nTotal choice: {choice_count}, comprehensive: {comp_count}")

# Also check what the actual lines look like
print("\n=== Actual lines around 3249 ===")
for i in range(3248, 3260):
    line = paragraphs[i]
    if line:
        m = re.match(pattern, line)
        print(f"  [{i}] match={m is not None} repr={repr(line[:80])}")
