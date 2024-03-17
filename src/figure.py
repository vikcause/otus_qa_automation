"""
main class Figure
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """main class functions"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        """parent function to calculate figure area"""
        pass

    @abstractmethod
    def get_perimeter(self):
        """parent function to calculate figure perimeter"""
        pass

    def add_area(self, another_figure):
        """parent function to calculate area of 2 figures"""
        if not isinstance(another_figure, Figure):
            raise ValueError("Need Figure class or it's child")
        return self.get_area() + another_figure.get_area()
