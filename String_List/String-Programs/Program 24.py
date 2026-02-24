#24. Frequency of each character

s = input("Enter string: ")
for ch in set(s):
    print(ch, ":", s.count(ch))