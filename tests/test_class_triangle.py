"""
descriptions of classes for testing figure triangle
"""
import pytest
from src.triangle import Triangle


class TestTriangle:
    """Test class for triangle"""

    @pytest.mark.otus
    @pytest.mark.smoke
    def test_triangle_positive(self, triangle_data):
        """positive test #1 for triangle"""

        catet_1, catet_2, gipotenuza, area = triangle_data
        catet_1 += 1
        gipotenuza -= 1
        area = 6.928203230275509
        t = Triangle(catet_1, catet_2, gipotenuza)
        assert t.get_area() == area, f"Area shoud be {t.get_area()}"

    @pytest.mark.otus
    @pytest.mark.parametrize(("catet_1", "catet_2", "gipotenuza"),
                             [
                                 (-3, 4, 5),
                                 (6, -7, 8),
                                 (7, 8, -9),
                                 (3, 4, 0),
                                 (1, 2, 10),
                                 (8, 80, 1),
                                 (10, 12, 25)
                             ],
                             ids=["below zero int cat_1",
                                  "below zero int cat_2",
                                  "below zero int gipot", "one side zero",
                                  "incorrect sides 1",
                                  "incorrect sides 2",
                                  "incorrect sides 3"])
    def test_triangle_negative(self, catet_1, catet_2, gipotenuza):
        """positive test #1 for triangle"""

        with pytest.raises(ValueError):
            Triangle(catet_1, catet_2, gipotenuza)
