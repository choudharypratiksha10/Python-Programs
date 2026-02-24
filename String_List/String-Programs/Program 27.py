#27. ASCII value of each character

s = input("Enter string: ")
for ch in s:
    print(ch, "=", ord(ch))