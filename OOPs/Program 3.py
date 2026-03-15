#3. Function student_data()

def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)

    if student_name is not None:
        print("Student Name:", student_name)

    if student_class is not None:
        print("Student Class:", student_class)

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name (press enter if none): ")
student_class = input("Enter Student Class (press enter if none): ")

if student_name == "":
    student_name = None

if student_class == "":
    student_class = None

student_data(student_id, student_name, student_class)