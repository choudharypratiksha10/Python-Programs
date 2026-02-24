#42. Split and join a string

s = input("Enter string: ")

words = s.split()          # split
new_string = "-".join(words)   # join with -

print("After split:", words)
print("After join:", new_string)