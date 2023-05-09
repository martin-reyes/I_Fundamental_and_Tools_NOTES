"""Greedy Operators

From the Python documentation:
The '*', '+', and '?' quantifiers are all greedy; they match as much
text as possible. Sometimes this behaviour isn’t desired; if the RE <.*>
is matched against '<a> b <c>', it will match the entire string, and
not just '<a>'. Adding ? after the quantifier makes it perform the match
in non-greedy or lazy fashion; as few characters as possible will be
matched. Using the RE <.*?> will match only '<a>' and '<c>'.

In the example below, we are trying to isolate each html tag. The dot
special character  is particularly susceptible to problems when used
in conjunction with a greedy operator.  The example domonstrates how
to avoid these problems using the ? operator.

The second example presents a subtler version of the same type of
problem.  Also, Python 3.11 gives you a way to prevent backtracking.
"""

import re

html = "<ul><li>The basics</li><li>Intercepting errors</li></ul>"
print(re.findall(r'<.*>', html))  # Greedy matching
print(re.findall(r'<.*?>', html)) # Lazy matching

txt = 'The bananas are 25 cents and the apples are 46 cents'
print(re.findall('(bananas)[\w\s]+([0-9]{2,3})', txt))  # Greedy matching
print(re.findall('(bananas)[\w\s]+?([0-9]{2,3})', txt)) # Lazy matching
# Preventing backtracking requires Python 3.11
print(re.findall('(bananas)[\w\s]++([0-9]{2,3})', txt)) # No backtracking

