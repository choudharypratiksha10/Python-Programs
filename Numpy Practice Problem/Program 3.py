#Max and Min difference in integer array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)
print()

max_diff = max(arr) - min(arr)
min_diff = min(arr) - max(arr)

print("Maximum difference:", max_diff)
print("Minimum difference:", min_diff)