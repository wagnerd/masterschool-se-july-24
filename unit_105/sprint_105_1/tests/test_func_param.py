import pytest


def func1(param1):
    return param1 % 2 == 0


@pytest.mark.parametrize("param1, expected", [
    (2, True),
    (3, False),
    (4, True),
    (101, False),
])
def test_func1(param1, expected):
    assert func1(param1) == expected

