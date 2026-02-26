#3. Check whether a key exists in a dictionary

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

key = input("Enter key to check: ")

if key in d:
    print("Key exists")
else:
    print("Key does not exist")