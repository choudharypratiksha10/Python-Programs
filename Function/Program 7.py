# Program 7:Count Upper and Lower Case Letters

def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

sample_string = "The quick Brow Fox"

u, l = count_case(sample_string)

print("No. of Upper case characters:", u)
print("No. of Lower case characters:", l)