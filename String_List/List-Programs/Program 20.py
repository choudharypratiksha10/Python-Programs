#20. Sum of elements at odd indices

lst = list(map(int, input("Enter list elements: ").split()))

total = 0
for i in range(len(lst)):
    if i % 2 != 0:
        total += lst[i]

print("Sum at odd indices:", total)