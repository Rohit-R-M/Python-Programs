"""
4.Write a Python program to create a class that represents a shape. Include methods to calculate 
its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
"""

class Shape:
    pass

class Circle(Shape):
    def __init__(self,x):
        self.r=x
    def area(self):
        return 3.14*(self.r**2)
    def peri(self):
        return 3.14*self.r*2

class Triangle(Shape): 
    def __init__(self,x,y,z):
        self.l=x
        self.b=y
        self.h=z
    def area(self):
        return 0.5*self.l*self.b
    def peri(self):
        return self.l+self.b+self.h

class Square(Shape):
    def __init__(self,x):
        self.a=x
    def area(self):
        return self.a*self.a
    def peri(self):
        return self.a*4  

sq=Square(int(input("Enter side of square : ")))
tri=Triangle(int(input("Enter length of triangle : ")),int(input("Enter breadth of triangle : ")),int(input("Enter hypotonuese of triangle : ")))
circ=Circle(int(input("Enter radius of circle : ")))
print("Square area  : ",sq.area(),"Square perimeter : ",sq.peri())
print("Triangle area  : ",tri.area(),"Triangle perimeter : ",tri.peri())
print("Circle area  : ",circ.area(),"Circle perimeter : ",circ.peri())
