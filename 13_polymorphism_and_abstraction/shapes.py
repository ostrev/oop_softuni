import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.__radius
        return perimeter

    def calculate_area(self):
        area = math.pi * self.__radius ** 2
        return area


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_perimeter(self):
        return 2 * self.__height + 2 * self.__width

    def calculate_area(self):
        return self.__height * self.__width


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())