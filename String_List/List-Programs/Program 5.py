#5. Remove empty element from list

lst = input("Enter elements: ").split()
result = [x for x in lst if x != ""]
print("Result:", result)