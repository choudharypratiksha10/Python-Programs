#37. Search pattern in string

import re
s = input("Enter string: ")
pat = input("Enter pattern: ")

if re.search(pat, s):
    print("Pattern found")
else:
    print("Not found")