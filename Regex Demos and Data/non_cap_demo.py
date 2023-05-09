"""Non-Capturing Groups Demo

This program demonstrates several different ways a non-capturing
group can be used to simplify/shorten patterns as well as make them
more capable.
"""

import re
#  Allows an "or" operation in the middle of a pattern
# In this case, find words ending in st or in
print(re.findall(r'\b\w+(?:st|in)\b',
                 'cost akin more run against'))

#  Redo the zipcode example without using an "or" operation
print(re.findall(r'\d{5}(?:-\d{4})?',
                 '90210 90210-1234'))

#  The non-capturing group can be repeated
print(re.findall('\d+(?:\.\d+){3}',
                 '192.168.0.1 192.168.1.12'))
#  Or this way
print(re.findall('(?:\d+\.){3}\d+',
                 '192.168.0.1 192.168.1.12'))







