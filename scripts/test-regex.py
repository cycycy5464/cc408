#!/usr/bin/env python3
"""Test regex for comprehensive answers"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

# Test lines
test_lines = [
    '11.【解答】',
    '10. 【解答】',
    '09. 【解答】',
    '8.【解】',
    '7. 【解】',
]

pattern = r"^(\d{1,2})[.．]\s*【(解答|解)】"

for line in test_lines:
    m = re.match(pattern, line)
    if m:
        print(f"  MATCH: {repr(line)} -> num={m.group(1)}, type={m.group(2)}")
    else:
        print(f"  NO MATCH: {repr(line)}")
