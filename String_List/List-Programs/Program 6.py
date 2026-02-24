#6. Display items divisible by 5

lst = list(map(int, input("Enter numbers: ").split()))
for x in lst:
    if x % 5 == 0:
        print(x)