"""
descriptions of classes for testing figure circle
"""
import pytest
from src.circle import Circle


@pytest.mark.smoke
@pytest.mark.otus
def test_circle_positive(circle_data):
    """positive test #1 for circle"""

    radius, area = circle_data
    c = Circle(radius)
    assert c.get_area() == area, f"Circle area should be {c.get_area()}"


@pytest.mark.otus
@pytest.mark.parametrize("radius",
                         [
                             (-3),
                             (-5.5),
                             0],
                         ids=["below zero int", "below zero float",
                              "zero rad",])
def test_circle_negative(radius):
    """negative test #1 for circle"""

    with pytest.raises(ValueError):
        Circle(radius)
