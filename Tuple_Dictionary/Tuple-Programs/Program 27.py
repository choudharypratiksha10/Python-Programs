#27. Remove an item from a tuple

t = tuple(input("Enter elements: ").split())
item = input("Enter element to remove: ")
lst = list(t)
lst.remove(item)
t = tuple(lst)
print(t)