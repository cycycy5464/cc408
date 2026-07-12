"""Debug regex matching for A\. format"""
import re

# Test string: A\.O(log2n) - backslash+dot
test = 'A\\.O(log2n)'
print(f"test string: {repr(test)}")
print(f"test bytes: {test.encode('utf-8').hex()}")

# Pattern: match A-D then do
# I need regex: ^[A-D]\\.
# Where \\ in regex = one literal backslash
# and . in regex = any char

# To create the STRING that regex interprets as ^[A-D]\\.
# I need: ^ [ A - D ] \ \ .
# That's 9 characters

# Method 1: use chr(92) for backslash
p1 = '^[A-D]' + chr(92) + chr(92) + '.'
print(f"\np1: {repr(p1)}")
print(f"p1 bytes: {p1.encode('utf-8').hex()}")
print(f"p1 match: {bool(re.match(p1, test))}")

# Method 2: use raw string with explicit double backslash
# In raw string r'\\' produces TWO backslash chars
p2 = r'^[A-D]' + r'\\' + '.'
print(f"\np2: {repr(p2)}")
print(f"p2 bytes: {p2.encode('utf-8').hex()}")
print(f"p2 match: {bool(re.match(p2, test))}")

# Method 3: use r'\\\.'
# r'\\.' = backslash + backslash + dot = 3 chars
p3 = r'^[A-D]\\.'
print(f"\np3 (r'^[A-D]\\\\.'): {repr(p3)}")
print(f"p3 bytes: {p3.encode('utf-8').hex()}")
print(f"p3 len: {len(p3)}")
print(f"p3 match: {bool(re.match(p3, test))}")

# Method 4: r'^[A-D][\\].'
p4 = r'^[A-D][\\].'
print(f"\np4 (r'^[A-D][\\\\].'): {repr(p4)}")
print(f"p4 match: {bool(re.match(p4, test))}")

# Method 5: non-raw '\\\\\\.'
p5 = '^[A-D]\\\\\\.'
print(f"\np5 ('^[A-D]\\\\\\\\\\\\.'): {repr(p5)}")
print(f"p5 bytes: {p5.encode('utf-8').hex()}")
print(f"p5 match: {bool(re.match(p5, test))}")
