#4. Square each element of list

lst = list(map(int, input("Enter numbers: ").split()))
result = [x*x for x in lst]
print("Squared list:", result)