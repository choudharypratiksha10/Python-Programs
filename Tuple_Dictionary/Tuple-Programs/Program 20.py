#20. Add an item to a tuple

t = tuple(input("Enter tuple elements: ").split())
item = input("Enter item to add: ")
t = t + (item,)
print(t)