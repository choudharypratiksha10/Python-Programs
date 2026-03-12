# Program 9: Check Prime Number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter number: "))

if is_prime(number):
    print("Number is Prime")
else:
    print("Number is Not Prime")