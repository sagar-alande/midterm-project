"""Testing the Calculator"""
from calculator import Calculator


def tuple_list():
    """AAA test data arrange"""
    return 8, 2


def test_add():

    """Testing the addition method from calculator"""

    result = Calculator.add(tuple_list())

    assert result == 10


def test_sub():
    """Testing the subtraction method from calculator"""
    result = Calculator.subtract(tuple_list())
    assert result == -6


def test_multiply():
    """Testing the Multiplication method from calculator"""
    result = Calculator.multiply(tuple_list())
    assert result == 16
