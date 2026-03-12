# Program 11: Check Perfect Number

def is_perfect(n):
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div == n

number = int(input("Enter number: "))

if is_perfect(number):
    print("Number is Perfect")
else:
    print("Number is Not Perfect")