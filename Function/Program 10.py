# Program 10: Print Even Numbers from List

def even_numbers(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result

sample_list = [1,2,3,4,5,6,7,8,9]

print("Even numbers:", even_numbers(sample_list))