#16. Remove duplicates from dictionary (by values)

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

new = {}
for k, v in d.items():
    if v not in new.values():
        new[k] = v

print(new)