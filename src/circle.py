"""
description for figure Circle
"""
from math import pi
from figure import Figure


class Circle(Figure):
    """class for figure Circle"""

    def __init__(self, radius: int):
        """initialization method"""
        super().__init__(name=__class__.__name__)
        if radius <= 0:
            raise ValueError("Circle radius can't be less than zero")
        self.rad = radius

    def get_perimeter(self):
        """correcting parent method for specify figure - Circle"""
        return 2 * self.rad * pi

    def get_area(self):
        """correcting parent method for specify figure - Circle"""
        return pi*(self.rad**2)
