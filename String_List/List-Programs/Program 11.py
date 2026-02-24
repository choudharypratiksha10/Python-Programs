#11. Count number of items in a list

lst = input("Enter elements: ").split()
count = 0

for _ in lst:
    count += 1

print("Number of items:", count)