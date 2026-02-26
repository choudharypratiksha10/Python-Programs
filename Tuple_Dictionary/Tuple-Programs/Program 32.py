#32. Unzip a list of tuples into individual lists

n = int(input("Enter number of tuples: "))
lst = []
for i in range(n):
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    lst.append((a, b))

x, y = zip(*lst)
print(list(x))
print(list(y))