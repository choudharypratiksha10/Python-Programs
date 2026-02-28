#26. Convert a list into a nested dictionary of keys

lst = input("Enter list elements: ").split()

d = {}
for item in reversed(lst):
    d = {item: d}

print(d)