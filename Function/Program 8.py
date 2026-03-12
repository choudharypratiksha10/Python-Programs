# Program 8: Unique Elements from List

def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

sample_list = [1,2,3,3,3,3,4,5]

print("Unique List:", unique_list(sample_list))