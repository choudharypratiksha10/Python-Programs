#14. Count all substrings

s = input("Enter string: ")
n = len(s)
count = n * (n + 1) // 2
print("Total substrings:", count)