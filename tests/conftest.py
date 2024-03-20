"""
Place for fixture
"""
import pytest


@pytest.fixture(scope="session", autouse=True)
def run_stop_db():
    """fixture for running / stopping DB """

    print("\n Running DB")

    yield

    print("\n Stopping DB")


@pytest.fixture()
def work_with_api(run_stop_db):
    """fixture for working with API """

    print("\n Api iteractions started")

    yield

    print("\n Api iteractions stopped")


@pytest.fixture()
def triangle_data():
    """fixture with data for triangle"""

    catet_1, catet_2, gipotenuza, area = 3, 4, 5, 6

    yield catet_1, catet_2, gipotenuza, area

    print("\n Down")
    catet_1, catet_2, gipotenuza, area = 3, 4, 5, 6


@pytest.fixture(params=[(1, 3.141592653589793), (2, 12.566370614359172),
                        (3, 28.274333882308138), (10, 314.1592653589793)])
def circle_data(request):
    """fixture with data for circle"""
    radius, area = request.param

    yield radius, area


@pytest.fixture()
def rectangle_data():
    """fixture with data for rectangle with wrapper"""

    def _wrapper(data: str):
        if data == "integer":
            return 3, 5, 15
        if data == "float":
            return 3.5, 5.7, 19.95

    yield _wrapper

    print("\n wrapper used")
