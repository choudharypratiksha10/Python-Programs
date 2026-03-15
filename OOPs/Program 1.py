#1. Vehicle class with max_speed and mileage

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

max_speed = int(input("Enter max speed: "))
mileage = int(input("Enter mileage: "))

v = Vehicle(max_speed, mileage)

print("Max Speed:", v.max_speed)
print("Mileage:", v.mileage)