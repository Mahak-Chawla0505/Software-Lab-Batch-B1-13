import pytest

from factorial import factorial


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_positive_number():
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative_number_raises_value_error():
    with pytest.raises(ValueError, match="Number cannot be negative"):
        factorial(-1)
