import math_operation


def test_add_function():
    assert math_operation.add(2, 3) == 5
    assert math_operation.add(-1, 1) == 0
    assert math_operation.add(0, 0) == 0


if __name__ == "__main__":
    test_add_function()
    print("trexei")
