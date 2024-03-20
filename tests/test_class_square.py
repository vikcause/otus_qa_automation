"""
descriptions of classes for testing figure square
"""
from datetime import datetime
import pytest
from src.square import Square


class TestSquare:
    """Test class for square"""

    @pytest.mark.otus
    @pytest.mark.smoke
    @pytest.mark.parametrize(("width", "area"),
                             [
                                 (3, 9),
                                 (4.1, 16.81)
                             ],
                             ids=["integer check", "float check"])
    def test_square_positive(self, width, area):
        """positive test #1 for square"""

        s = Square(width)
        assert s.get_area() == area, \
            f"Calculated square area should be equal {width ** 2}"

    @pytest.mark.otus
    @pytest.mark.skipif(condition=datetime.weekday(datetime.now()) == 1,
                        reason="Not working at Tuesday")
    @pytest.mark.parametrize("width",
                             [
                                 (-2),
                                 (-2.5),
                                 0
                             ],
                             ids=["below zero int", "below zero float",
                                  "zero"])
    def test_square_negative(self, width):
        """negative test #1 for rectangle"""

        with pytest.raises(ValueError):
            Square(width)
