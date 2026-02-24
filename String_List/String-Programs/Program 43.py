#43. Words greater than given length k

s = input("Enter string: ")
k = int(input("Enter length k: "))

for word in s.split():
    if len(word) > k:
        print(word)