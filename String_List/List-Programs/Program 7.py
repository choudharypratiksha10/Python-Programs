#7. Remove repetitive items from list

lst = list(map(int, input("Enter numbers: ").split()))
result = list(dict.fromkeys(lst))
print("Result:", result)