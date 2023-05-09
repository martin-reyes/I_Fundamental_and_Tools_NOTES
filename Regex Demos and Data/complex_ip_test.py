"""Lab02_ipv4_alt.py

Use basic regex expressions to parse the IPv4 addresses in a simulated log
file.  Do this operation two different ways.
"""

from pprint import pprint
import re

fin = open('c:/pydata/ipaddress.txt', 'rt')
log = fin.read()
#print(log)
fin.close()
# Use a complex pattern to isolate valid IP addresses.
ip = re.findall(r"""\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
                (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
                (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
                (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"""                
                , log, re.VERBOSE)
pprint(ip)
