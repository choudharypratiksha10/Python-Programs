#24. Print dictionary in table format

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

print("Key\tValue")
for k, v in d.items():
    print(k, "\t", v)
    