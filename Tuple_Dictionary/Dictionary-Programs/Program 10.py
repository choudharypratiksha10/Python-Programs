#10. Multiply all items in a dictionary

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

mul = 1
for v in d.values():
    mul *= v

print("Multiplication:", mul)