#23. Create dictionary from string (count letters)

s = "SBJAIN"
d = {}

for ch in s:
    d[ch] = d.get(ch, 0) + 1

print(d)