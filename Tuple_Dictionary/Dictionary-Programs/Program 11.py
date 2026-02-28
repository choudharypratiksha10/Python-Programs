#11. Remove a key from a dictionary

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

key = input("Enter key to remove: ")
del d[key]
print(d)