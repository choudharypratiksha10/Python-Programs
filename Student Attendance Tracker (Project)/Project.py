# Student Attendance Tracker with Roll Numbers

attendance = {}  # Dictionary to store student data with roll numbers

def add_student():
    roll = input("Enter student roll number: ")
    if roll in attendance:
        print("Roll number already exists!")
    else:
        name = input("Enter student name: ")
        attendance[roll] = {"name": name, "records": []}
        print("Student added successfully!")

def mark_attendance():
    roll = input("Enter student roll number: ")
    if roll in attendance:
        status = input("Enter status (P for Present / A for Absent): ").upper()
        if status == "P":
            attendance[roll]["records"].append("Present")
            print("Marked Present")
        elif status == "A":
            attendance[roll]["records"].append("Absent")
            print("Marked Absent")
        else:
            print("Invalid input!")
    else:
        print("Student not found!")

def generate_report():
    print("\nAttendance Report")
    print("-" * 90)
    
    # Table Header
    print(f"{'Roll Number':<15}{'Name':<25}{'Total Classes':<15}{'Present':<10}{'Absent':<10}{'Percentage':<15}")
    print("-" * 90)

    for roll, info in attendance.items():
        name = info["name"]
        records = info["records"]
        total_classes = len(records)
        present_count = records.count("Present")
        absent_count = records.count("Absent")

        percentage = (present_count / total_classes) * 100 if total_classes > 0 else 0

        # Table Row
        print(f"{roll:<15}{name:<25}{total_classes:<15}{present_count:<10}{absent_count:<10}{percentage:.2f}%")

    print("-" * 90)

def menu():
    while True:
        print("\n--- Student Attendance Tracker ---")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
menu()