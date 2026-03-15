#4. Modify Student attributes

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s = Student(name, marks)

print("Original Values")
print("Name:", s.student_name)
print("Marks:", s.marks)

s.student_name = input("Enter new name: ")
s.marks = int(input("Enter new marks: "))

print("Modified Values")
print("Name:", s.student_name)
print("Marks:", s.marks)