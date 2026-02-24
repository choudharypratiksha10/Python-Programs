#38. Remove i-th character

s = input("Enter string: ")
i = int(input("Enter index: "))
print(s[:i] + s[i+1:])