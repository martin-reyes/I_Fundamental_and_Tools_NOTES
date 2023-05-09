"""context2.py

This program demonstrates the usefulness of both negative and positive
lookahead/lookbehind to determine whether the object being inspected is a
six-digit number without extra digits on either side or is surrounded by
whitespace.  The program performs the operation first without context
checking just to show what an unchecked solution looks like.  Both of
the context solutions are shown with and without VERBOSE.

All of the solutions work with the original data.  Replace that data
with the folowing string and rerun the program:
xstr = "1023422 102376a 123 434355z 123456789 12bb23"
If I am still looking for six consecutive digits not surrounded by other
digits, only one of these solutions produces a valid result.  It's
important to understand your data and exactly what it is you are trying
to find.
"""

import re
xstr = "1023422 102376 123 434355 123456789 12bb23"
#  This regex picks out every non-overlapping series of six digits
# regardless of context
print(re.findall(r'\d{6}', xstr))
#  result - ['102342', '102376', '434355', '123456']


# The following regex checks for six digits surrounded by whitespace
print(re.findall(r'(?<=\s)\d{6}(?=\s)', xstr))
print(re.findall(r"""
                 (?<=\s) # Selection must be preceded by whitespace
                 \d{6}   # Select six consecutive digits
                 (?=\s)  # Selection must be followed by whitespace
                 """, xstr, re.VERBOSE))
# result - ['102376', '434355']

# The following regex checks for no following or leading digits
print(re.findall(r'(?<!\d)\d{6}(?!\d)', xstr))
print(re.findall(r"""
                 (?<!\d) # Selection must not be preceded by a digit
                 \d{6}   # Select six consecutive digits
                 (?!\d)  # Selection must not be followed by a digit
                 """, xstr, re.VERBOSE))
# result - ['102376', '434355']

# The following regex checks for six digits surrounded by non-alphanumerics
# It works in this case but is not as demanding as the examples above.  Can
#  you see why that is?
print(re.findall(r'\b\d{6}\b', xstr))
# result - ['102376', '434355']
