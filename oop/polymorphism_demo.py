# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must override area()")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
