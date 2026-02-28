#13. Sort a dictionary by key

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

print(dict(sorted(d.items())))