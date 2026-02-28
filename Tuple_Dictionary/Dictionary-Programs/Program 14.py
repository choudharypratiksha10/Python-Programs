#14. Get maximum and minimum values of dictionary

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    d[k] = v

print("Max:", max(d.values()))
print("Min:", min(d.values()))