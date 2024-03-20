"""
description for figure Triangle
"""
import math
from src.figure import Figure


class Triangle(Figure):
    """class for figure Triangle"""

    def __init__(self, catet_1: int, catet_2: int, gipotenuza: int):
        """initialization method"""
        super().__init__(name=__class__.__name__)
        if catet_1 <= 0 or catet_2 <= 0 or gipotenuza <= 0:
            raise ValueError("Noone side can't be less than zero")
        if (((catet_1 + catet_2) <= gipotenuza) or
                ((catet_1 + gipotenuza) <= catet_2) or
                ((catet_2 + gipotenuza) <= catet_1)):
            raise ValueError("Triangle with this sides doesn't exist")
        self.catet_1 = catet_1
        self.catet_2 = catet_2
        self.gipotenuza = gipotenuza

    def get_perimeter(self):
        """correcting parent method for specify figure - triangle"""
        return self.catet_1 + self.catet_2 + self.gipotenuza

    def get_area(self):
        """correcting parent method for specify figure - triangle"""
        p = 0.5 * self.get_perimeter()
        return math.sqrt(p * (p - self.catet_1) *
                         (p - self.catet_2) * (p - self.gipotenuza))
