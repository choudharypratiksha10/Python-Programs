#23. Find matched characters in two strings

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

matched = set(s1) & set(s2)
print("Matched characters:", matched)