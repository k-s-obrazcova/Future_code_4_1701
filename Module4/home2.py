from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


square = Square(10)
circle = Circle(3)
triangle = Triangle(3, 4, 5)

print(f"Площадь квадрата: {square.area()}")
print(f"Периметр квадрата: {square.perimeter()}")


print(f"Площадь круга: {circle.area()}")
print(f"Периметр круга: {circle.perimeter()}")

print(f"Площадь треугольника: {triangle.area()}")
print(f"Периметр треугольника: {triangle.perimeter()}")