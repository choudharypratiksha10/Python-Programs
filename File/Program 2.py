#2. Read names.txt and print names

file = open("names.txt", "r")

for line in file:
    print(line.strip())

file.close()