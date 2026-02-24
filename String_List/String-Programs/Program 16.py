#16. Reverse using stack & reversed()

s = input("Enter string: ")
stack = list(s)
rev = ""

while stack:
    rev += stack.pop()

print(rev)
print("".join(reversed(s)))