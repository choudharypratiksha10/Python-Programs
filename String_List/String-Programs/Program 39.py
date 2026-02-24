#39. Length of string (different ways) 

s = input("Enter string: ")

print(len(s))

count = 0
for _ in s:
    count += 1
print(count)

print(s.__len__())