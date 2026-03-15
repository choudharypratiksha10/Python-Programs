#3. Count characters in data.txt

file = open("data.txt", "r")

text = file.read()
count = len(text)

print("Number of characters:", count)

file.close()