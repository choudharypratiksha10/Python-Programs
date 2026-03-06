# Student Attendance Tracker

attendance = {}

def add_student():
    name = input("Enter student name: ")
    if name in attendance:
        print("Student already exists!")
    else:
        attendance[name] = []
        print("Student added successfully!")

def mark_attendance():
    name = input("Enter student name: ")
    if name in attendance:
        status = input("Enter status (P for Present / A for Absent): ").upper()
        if status == "P":
            attendance[name].append("Present")
            print("Marked Present")
        elif status == "A":
            attendance[name].append("Absent")
            print("Marked Absent")
        else:
            print("Invalid input!")
    else:
        print("Student not found!")

def generate_report():
    print("\nAttendance Report")
    print("-" * 78)
    
    # Table Header
    print(f"{'Name':<20}{'Total Classes':<15}{'Present':<10}{'Absent':<10}{'Percentage':<15}")
    print("-" * 78)

    for name, records in attendance.items():
        total_classes = len(records)
        present_count = records.count("Present")
        absent_count = records.count("Absent")

        if total_classes > 0:
            percentage = (present_count / total_classes) * 100
        else:
            percentage = 0

        # Table Row
        print(f"{name:<20}{total_classes:<15}{present_count:<10}{absent_count:<10}{percentage:.2f}%")

    print("-" * 78)

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