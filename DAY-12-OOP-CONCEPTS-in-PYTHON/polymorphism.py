from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
#instances of both subclasses

circle = Circle(5)
rectangle = Rectangle(3,4)

#call their area methods
print("Area of the circle:", circle.area())
print("Area of the rectangle:", rectangle.area())