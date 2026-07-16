#!/usr/bin/env python3
"""Check answer extraction in the script's ranges"""
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

# Check range 522-1741 (for answer 3.2)
print("=== Range 522-1741 (answer 3.2) ===")
choice_32 = []
comp_32 = []
in_comp = False
pattern = r"^(\d{1,2})[.．]\s*【(解答|解)】"

for i in range(522, 1741):
    line = paragraphs[i]
    if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
        choice_32.append((i, line))
        in_comp = False
    elif re.match(pattern, line):
        in_comp = True
        comp_32.append((i, line))
    elif in_comp:
        comp_32.append((i, line))
    else:
        in_comp = False

print(f"Choice answers: {len(choice_32)}")
print(f"Comprehensive answers: {len(comp_32)}")

# Show first few
print("\nFirst 5 choice answers:")
for idx, line in choice_32[:5]:
    print(f"  [{idx}] {line}")

print("\nFirst 5 comp answers:")
for idx, line in comp_32[:5]:
    print(f"  [{idx}] {line}")

# Check range 2220-3585 (for answer 3.1)
print("\n=== Range 2220-3585 (answer 3.1) ===")
choice_31 = []
comp_31 = []
in_comp = False

for i in range(2220, 3585):
    line = paragraphs[i]
    if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
        choice_31.append((i, line))
        in_comp = False
    elif re.match(pattern, line):
        in_comp = True
        comp_31.append((i, line))
    elif in_comp:
        comp_31.append((i, line))
    else:
        in_comp = False

print(f"Choice answers: {len(choice_31)}")
print(f"Comprehensive answers: {len(comp_31)}")

# Show first few
print("\nFirst 5 choice answers:")
for idx, line in choice_31[:5]:
    print(f"  [{idx}] {line}")

print("\nFirst 5 comp answers:")
for idx, line in comp_31[:5]:
    print(f"  [{idx}] {line}")
