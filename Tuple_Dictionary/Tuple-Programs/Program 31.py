#31. Convert a tuple to a dictionary

n = int(input("Enter number of key-value pairs: "))
lst = []
for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    lst.append((k, v))
t = tuple(lst)
d = dict(t)
print(d)