# Program 16: Squares Between 1 and 30

def squares_list():
    result = []
    for i in range(1, 31):
        result.append(i * i)
    return result

print("Squares list:", squares_list())