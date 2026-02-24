#40. String containing all vowels

s = input("Enter string: ")
vowels = set("aeiou")

if vowels.issubset(set(s.lower())):
    print("Contains all vowels")
else:
    print("Does not contain all vowels")