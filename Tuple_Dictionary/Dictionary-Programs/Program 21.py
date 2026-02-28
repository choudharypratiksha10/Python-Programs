#21. Highest 3 values of corresponding keys

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

values = sorted(d.values(), reverse=True)[:3]
print("Highest 3 values:", values)