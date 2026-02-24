#9. Filter odd and even numbers from a list

lst = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even:", even)
print("Odd:", odd)