#34. Convert list of tuples into a dictionary

n = int(input("Enter number of tuples: "))
lst = []
for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    lst.append((k, v))

d = dict(lst)
print(d)