#24. Find repeated items in a tuple

t = tuple(input("Enter elements: ").split())
rep = []
for i in t:
    if t.count(i) > 1 and i not in rep:
        rep.append(i)
print(tuple(rep))