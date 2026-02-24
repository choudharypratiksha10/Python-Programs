#46. Check if string is binary

s = input("Enter string: ")

if all(ch in "01" for ch in s):
    print("Binary string")
else:
    print("Not a binary string")