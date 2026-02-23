#15. Reverse string (5 ways)

s = input("Enter string: ")

print(s[::-1])
print("".join(reversed(s)))

rev = ""
for ch in s:
    rev = ch + rev
print(rev)

rev = ""
for i in range(len(s)-1, -1, -1):
    rev += s[i]
print(rev)

print("".join(list(s)[::-1]))