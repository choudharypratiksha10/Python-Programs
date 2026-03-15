#10. Polar coordinate addition using operator overloading

import math

class Polar:

    def __init__(self, r, a):
        self.r = r
        self.a = a

    def __add__(self, other):

        x1 = self.r * math.cos(self.a)
        y1 = self.r * math.sin(self.a)

        x2 = other.r * math.cos(other.a)
        y2 = other.r * math.sin(other.a)

        x = x1 + x2
        y = y1 + y2

        r = math.sqrt(x*x + y*y)
        a = math.atan(y/x)

        return Polar(r, a)

    def display(self):
        print("r =", self.r)
        print("angle =", self.a)

r1 = float(input("Enter r1: "))
a1 = float(input("Enter angle1: "))

r2 = float(input("Enter r2: "))
a2 = float(input("Enter angle2: "))

p1 = Polar(r1, a1)
p2 = Polar(r2, a2)

p3 = p1 + p2

p3.display()