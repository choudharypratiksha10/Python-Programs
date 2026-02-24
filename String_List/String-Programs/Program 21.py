#21. Remove character from specified index

s = input("Enter string: ")
i = int(input("Enter index: "))
print(s[:i] + s[i+1:])