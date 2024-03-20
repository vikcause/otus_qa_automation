"""
description for figure Rectangle
"""
from src.figure import Figure


class Rectangle(Figure):
    """class for figure Rectangle"""

    def __init__(self, width: int, height: int):
        """initialization method"""
        super().__init__(name=__class__.__name__)
        if width <= 0 or height <= 0:
            raise ValueError("Noone side can't be less than zero")
        self.width = width
        self.height = height

    def get_perimeter(self):
        """correcting parent method for specify figure - rectangle"""
        return 2 * (self.height + self.width)

    def get_area(self):
        """correcting parent method for specify figure - rectangle"""
        return self.height * self.width
