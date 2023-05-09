"""begin-end.py

This program reads a virtual file of server names and finds those
that begin with two digits and ends with a digit or a capital O.
The caret (^) anchors the search to the beginning of the record.
The dollar sign ($) anchors the search to the end of the record.
This accounts for the entire record.  Ususally, you will just use
one or the other.  Online, you see both of these used frequently in
sample solutions.
"""

import re
# Each entry contains a newline character to simulate file records
srvrs = ['OKCUC120\n', '37SQFSRU6\n', '22LONOLRZ\n',
         '345SQR-OC2\n', '1115BZQBO\n', 'ZC49OLR2\n']

for rec in srvrs:
    fnd = re.findall(r'^\d{2}\w+[\dO]$', rec)
    if fnd:
        print(fnd)

