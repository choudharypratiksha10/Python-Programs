#4. Iterate over dictionary using for loop

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

for key in d:
    print(key, ":", d[key])