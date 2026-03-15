#5. Append "David" to names.txt

file = open("names.txt", "a")

file.write("David\n")

file.close()

print("David added to file.")