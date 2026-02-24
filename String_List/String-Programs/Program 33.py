#33. Count letters & digits

s = input("Enter string: ")
letters = digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)