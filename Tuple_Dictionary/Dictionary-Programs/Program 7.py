#7. Merge two dictionaries

d1 = {}
d2 = {}

n1 = int(input("Enter number of items in first dictionary: "))
for i in range(n1):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d1[k] = v

n2 = int(input("Enter number of items in second dictionary: "))
for i in range(n2):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d2[k] = v

d1.update(d2)
print(d1)