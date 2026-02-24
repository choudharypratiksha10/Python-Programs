#16. Insert a new element at a specific position

lst = list(map(int, input("Enter list elements: ").split()))
pos = int(input("Enter position (index): "))
val = int(input("Enter value to insert: "))

lst.insert(pos, val)
print("Updated list:", lst)