# Program 12: Check Palindrome

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

word = input("Enter a string: ")

if is_palindrome(word):
    print("It is Palindrome")
else:
    print("It is Not Palindrome")