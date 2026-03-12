# Program 2: Sum of all numbers in a list

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [8, 2, 3, 0, 7]

print("Sum of list:", sum_list(sample_list))