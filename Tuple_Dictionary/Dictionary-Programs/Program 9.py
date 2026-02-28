#9. Sum all items in a dictionary

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

print("Sum:", sum(d.values()))