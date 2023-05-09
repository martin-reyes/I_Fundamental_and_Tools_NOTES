""" grouping.py

This program demonstrates grouping using the finditer function.
The phone numbers presented are in various states to simulate real
data.  The first example uses group numbers to access the results.
The second example supplies names which can be used in place of
index numbers.  The final example simply compiles the second example.
It shows how there is a corresponding finditer method.  All of the
RE functions have a method counterpart.
"""

import re

print('**Phone numbers by numbered groups')
ph = '+1-800-555-5555, 800.222.2222, 1800 333 3333, -800-444-4444'
fnd = re.finditer(r'(\d)?[-. ]?(\d{3})[-. ](\d{3})[-. ](\d{4})', ph)
for mat in fnd:
    print(mat.group(0), ',lastindex =', mat.lastindex)  
    print(mat.group(1), mat.group(2),
          mat.group(3), mat.group(4))

print('\n**Phone numbers by named groups')
fnd = re.finditer(r"""
                  (?P<cntry>\d)?[-. ]?   # Extract country code
                  (?P<area>\d{3})[-. ]   # Extract area code
                  (?P<prefix>\d{3})[-. ] # Extract prefix
                  (?P<line>\d{4})        # Extract line number
                  """,ph, re.VERBOSE)
for mat in fnd:
    print(mat.group())  # or print(mat.group(0))
    print(mat.group('cntry'), mat.group('area'),
          mat.group('prefix'), mat.group('line'))

print('\n**Compiled pattern and flag')
cpattern = re.compile(r"""
                  (?P<cntry>\d)?[-. ]?   # Extract country code
                  (?P<area>\d{3})[-. ]   # Extract area code
                  (?P<prefix>\d{3})[-. ] # Extract prefix
                  (?P<line>\d{4})        # Extract line number
                  """, re.VERBOSE)
fnd = cpattern.finditer(ph)  # Example of finditer as a method
for mat in fnd:
    print(mat.group())  # or print(mat.group(0))
    print(mat.group('cntry'), mat.group('area'),
          mat.group('prefix'), mat.group('line'))
