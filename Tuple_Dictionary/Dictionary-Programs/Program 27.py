#27. Sort a list alphabetically in a dictionary

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter values separated by space: ").split()
    d[key] = value

for k in d:
    d[k].sort()

print(d)