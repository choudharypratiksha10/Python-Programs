#5. Employee and Manager (process 10 managers)

class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

class Manager(Employee):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)
        print()

managers = []

for i in range(10):
    print("\nEnter details for Manager", i+1)
    m = Manager()
    m.get_data()
    managers.append(m)

print("\nManager Details")
for m in managers:
    m.display()