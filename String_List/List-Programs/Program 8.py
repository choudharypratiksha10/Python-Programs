#8. Append second list to first list

list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

list1.extend(list2)
print("Result:", list1)