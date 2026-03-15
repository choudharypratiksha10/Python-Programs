#6. Sum numbers from numbers.txt

file = open("numbers.txt", "r")

total = 0

for line in file:
    num = int(line.strip())
    total += num

print("Sum of numbers:", total)

file.close()