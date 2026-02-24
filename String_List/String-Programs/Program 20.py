#20. Swap characters

s = input("Enter string: ")
i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

lst = list(s)
lst[i], lst[j] = lst[j], lst[i]
print("".join(lst))