#18. Second smallest element in a list

lst = list(map(int, input("Enter list elements: ").split()))

unique = list(set(lst))
unique.sort()

if len(unique) >= 2:
    print("Second smallest:", unique[1])
else:
    print("Not enough elements")