#8. Area of 2D Shapes (function overloading concept)

import math

class Area:

    def calculate(self, a, b=None, c=None):

        if b is None and c is None:
            print("Square Area:", a*a)

        elif c is None:
            print("Rectangle Area:", a*b)

        else:
            s = (a+b+c)/2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Triangle Area:", area)

A = Area()

side = float(input("Enter side of square: "))
A.calculate(side)

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
A.calculate(l, w)

a = float(input("Enter side1 of triangle: "))
b = float(input("Enter side2 of triangle: "))
c = float(input("Enter side3 of triangle: "))
A.calculate(a, b, c)