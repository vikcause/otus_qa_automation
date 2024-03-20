"""
descriptions of classes for testing figure rectangle
"""
from datetime import datetime
import pytest
from src.rectangle import Rectangle


class TestRectangle:
    """Test class for rectangle"""

    @pytest.mark.smoke
    @pytest.mark.otus
    @pytest.mark.parametrize(("width", "height", "area"),
                             [
                                 (3, 5, 15),
                                 (3.5, 5.7, 19.95)
                             ],
                             ids=["integer check", "float check"])
    @pytest.mark.skipif(condition=datetime.now().day == 18,
                        reason="Not working at 18 day for each month")
    def test_rectangle_area_positive(self, width, height, area, work_with_api):
        """positive test #1 for rectangle with int and float"""

        r = Rectangle(width, height)
        assert r.get_area() == area, \
            f"Calculated rectangle area should be equal {width * height}"

    @pytest.mark.smoke
    @pytest.mark.otus
    @pytest.mark.skipif(condition=datetime.now().day == 18,
                        reason="Not working at 18 day for each month")
    @pytest.mark.parametrize("rectangle_params", ["integer", "float"])
    def test_rectangle_area_positive_data_from_fixture(self, rectangle_data,
                                                       rectangle_params):
        """positive test #2 for rectangle with int and float"""

        width, height, area = rectangle_data(data=rectangle_params)
        r = Rectangle(width, height)
        assert r.get_area() == area, \
            f"Calculated rectangle area should be equal {width * height}"

    @pytest.mark.skip(reason="Reason - https://jira-url.com/ticket-1")
    @pytest.mark.parametrize(("width", "height"),
                             [
                                 (-2, 5),
                                 (2.5, -5.7),
                                 (0, 1)
                             ],
                             ids=["below zero width int", "below zero "
                                                          "height float",
                                  "one side zero"])
    @pytest.mark.otus
    def test_rectangle_negative(self, width, height):
        """negative test #1 for rectangle"""

        with pytest.raises(ValueError):
            Rectangle(width, height)
