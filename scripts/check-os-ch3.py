#!/usr/bin/env python3
"""Check OS Ch3 answer extraction quality"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import zipfile
import xml.etree.ElementTree as ET
import re
from collections import defaultdict

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

print(f"Total paragraphs: {len(paragraphs)}")

markers = []
for i, line in enumerate(paragraphs):
    if "本节习题精选" in line or "本节试题精选" in line:
        m = re.match(r"\*?(\d+\.\d+)", line)
        markers.append((i, "exercise", m.group(1) if m else ""))
    elif "答案与解析" in line:
        m = re.match(r"\*?(\d+\.\d+)", line)
        markers.append((i, "answer", m.group(1) if m else ""))

print("\n=== Markers ===")
for idx, (start, sec_type, sec_num) in enumerate(markers):
    print(f"  [{idx}] line {start}: {sec_type} {sec_num}")

# Count questions and answers per section
print("\n=== Per-section analysis ===")
for sec_idx in range(0, len(markers), 2):
    ex_idx = sec_idx
    an_idx = sec_idx + 1
    if ex_idx >= len(markers):
        break
    ex_start = markers[ex_idx][0]
    ex_sec = markers[ex_idx][2]
    if an_idx < len(markers):
        an_start = markers[an_idx][0]
    else:
        an_start = len(paragraphs)

    # Count exercise lines
    ex_lines = paragraphs[ex_start+1:an_start]

    # Count questions
    q_count = 0
    for line in ex_lines:
        if re.match(r"^(\d{1,2})[.．]\s*(.*)", line):
            q_count += 1

    print(f"\n  Section {ex_sec}:")
    print(f"    Exercise lines: {ex_start+1} to {an_start} ({len(ex_lines)} lines)")
    print(f"    Questions found: {q_count}")

    # Answer section
    if an_idx < len(markers):
        an_sec = markers[an_idx][2]
        if an_idx + 1 < len(markers):
            an_end = markers[an_idx + 1][0]
        else:
            an_end = len(paragraphs)
        an_lines = paragraphs[an_start+1:an_end]
        print(f"    Answer lines: {an_start+1} to {an_end} ({len(an_lines)} lines)")

        # Count choice and comp answers
        choice = 0
        comp = 0
        for line in an_lines:
            if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
                choice += 1
            elif re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line):
                comp += 1
        print(f"    Choice answers: {choice}, Comprehensive answers: {comp}")
