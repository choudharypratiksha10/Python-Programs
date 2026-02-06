#Reverse copy of array (10 integers)

arr = []

print("Enter 10 integers:")
for i in range(10):
    x = int(input())
    arr.append(x)

rev_arr = arr[::-1]

print()
print("Original array:", arr)
print("Reversed array:", rev_arr)