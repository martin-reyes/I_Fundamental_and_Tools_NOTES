"""context1.py

This program demonstrates the capbility of both positive lookahead
and lookbehind. A lookahead must follow the pattern being sought
while a lookbehind must precede the pattern.
"""

import re

x = '1159486012539756033136578961237439760'

# Find all 6's followed by a zero.
print(re.findall(r'6(?=0)', x))
# Find all 6's not followed by a zero.
print(re.findall(r'6(?!0)', x))
# Find all 6's preceded by a 7 or 8.
print(re.findall(r'(?<=[78])6', x))
# Find all 6's preceded by a 1,2,3 or 4 and followed by a 5.
print(re.findall(r'(?<=[1-4])6(?=5)', x))

# Find the number of 6's followed by a zero.
print(len(re.findall(r'6(?=0)', x)))



