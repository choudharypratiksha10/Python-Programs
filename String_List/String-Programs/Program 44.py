#44. Check if string contains special characters

import re

s = input("Enter string: ")

if re.search(r'[^a-zA-Z0-9 ]', s):
    print("Contains special characters")
else:
    print("Does not contain special characters")