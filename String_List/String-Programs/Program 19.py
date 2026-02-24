#19. Repeat M chars N times

s = input("Enter string: ")
M = int(input("Enter M: "))
N = int(input("Enter N: "))

part = s[:M]
print(part * N)