#15. Get dictionary from an object's fields

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter name: ")
age = input("Enter age: ")

s = Student(name, age)
print(s.__dict__)