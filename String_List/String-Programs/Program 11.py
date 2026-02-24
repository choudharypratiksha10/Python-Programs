#11. Hexadecimal values in string

s = input("Enter hex string (like \\x48\\x65): ")
print(s.encode().decode("unicode_escape"))