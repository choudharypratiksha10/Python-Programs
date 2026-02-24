#47. Uncommon words from two strings

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

set1 = set(s1.split())
set2 = set(s2.split())

uncommon = set1.symmetric_difference(set2)
print("Uncommon words:", uncommon)