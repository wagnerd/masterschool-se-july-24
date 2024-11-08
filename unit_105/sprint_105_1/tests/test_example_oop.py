import pytest

from unit_105.sprint_105_1.example_oop import MyClass1, MyClass2


@pytest.fixture()
def fixture_class1():
    return MyClass1()


@pytest.fixture()
def fixture_class2(var1, var2):
    return MyClass2(var1, var2)


def test_myclass1():
    class1 = MyClass1()
    assert class1.var1 == "test"


def test_myclass1_2(fixture_class1):
    assert fixture_class1.var1 == "test"
    fixture_class1.run()
    assert fixture_class1.var1 == "run"


def test_myclass4():
    myclass = MyClass2(1, 2)
    assert myclass.var1 == 1
    assert myclass.var2 == 2
    assert not myclass.same


@pytest.mark.parametrize("var1, var2, expected_output", [
    (1, 1, [1, 1, True]),
    (1, 2, [1, 2, False]),
])
def test_myclass2(fixture_class2, expected_output):
    assert fixture_class2.var1 == expected_output[0]
    assert fixture_class2.var2 == expected_output[1]
    assert fixture_class2.same == expected_output[2]
