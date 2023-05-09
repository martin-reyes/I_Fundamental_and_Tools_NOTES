"""lab01.contractions.py

This program finds all contractions while omitting those words with
leading or trailing apostrphes. 
"""

import re
txt = ("I've been thinkin' that we couldn't have "
         "done more in our effort to beat 'em.")

matches = re.findall("[a-zA-Z]+'[a-zA-z]+", txt)
# re.IGNORECASE would let us use [a-z] over [a-zA-Z]

print(matches)




