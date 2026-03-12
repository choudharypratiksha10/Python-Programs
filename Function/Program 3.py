# Program 3: Multiply all numbers in a list

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

sample_list = [8, 2, 3, -1, 7]

print("Multiplication of list:", multiply_list(sample_list))