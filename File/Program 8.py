#8. Create passed.txt for students with grade A or B

file = open("grades.txt", "r")
passed = open("passed.txt", "w")

for line in file:
    name, grade = line.split()
    
    if grade == "A" or grade == "B":
        passed.write(name + "\n")

file.close()
passed.close()

print("Passed students saved in passed.txt")