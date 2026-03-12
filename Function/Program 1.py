# Program 1: Maximum of Three Numbers

def max_of_three(a, b, c):
    return max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum number is:", max_of_three(a, b, c))