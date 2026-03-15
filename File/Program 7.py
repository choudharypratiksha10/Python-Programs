#7. Count word "the" in words.txt

file = open("words.txt", "r")

text = file.read().lower()
words = text.split()

count = words.count("the")

print("The word 'the' appears", count, "times")

file.close()