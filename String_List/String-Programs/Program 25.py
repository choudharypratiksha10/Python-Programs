#25. Extract mobile number from string

import re
s = input("Enter string: ")
mobile = re.findall(r'\d{10}', s)
print("Mobile number:", mobile)