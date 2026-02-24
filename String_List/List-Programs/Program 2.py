#2. Remove even numbers from list

lst = list(map(int, input("Enter numbers: ").split()))
result = [x for x in lst if x % 2 != 0]
print("After removing even numbers:", result)