#28. Remove spaces from dictionary keys

d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

new_d = {}
for k, v in d.items():
    new_d[k.replace(" ", "")] = v

print(new_d)