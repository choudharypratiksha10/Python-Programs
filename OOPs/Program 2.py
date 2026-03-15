#2. Child class Bus inheriting Vehicle

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

max_speed = int(input("Enter bus max speed: "))
mileage = int(input("Enter bus mileage: "))

b = Bus(max_speed, mileage)

print("Bus Max Speed:", b.max_speed)
print("Bus Mileage:", b.mileage)