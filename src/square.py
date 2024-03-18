"""
description for figure Square
"""
from rectangle import Rectangle


class Square(Rectangle):
    """class for figure Square"""

    def __init__(self, width):
        """Initialization method"""
        if width <= 0:
            raise ValueError("Side can't be less than zero")
        super().__init__(width, width)
        self.name = __class__.__name__
