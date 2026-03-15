#1. Create names.txt and write given names

file = open("names.txt", "w")

file.write("Alice\n")
file.write("Bob\n")
file.write("Charlie\n")

file.close()

print("File created and names written.")