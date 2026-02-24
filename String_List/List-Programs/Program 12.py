#12. Reverse list without built-in (using indexing)

lst = list(input("Enter characters: "))
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Reversed list:", rev)