#29. Convert to camelCase

s = input("Enter string: ")
words = s.split()
camel = words[0].lower() + "".join(w.capitalize() for w in words[1:])
print(camel)