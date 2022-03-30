"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Addition as Add, Subtraction as Sub, Multiplication as Multiply


def tuple_list():
    """Arranging Data for AAA Testing"""
    return 5, 2


def test_addition_instance():
    """Testing the Calculator Subtract"""

    calculation = Add.create(tuple_list())
    # unit testing to check whether an Add is an instance of a given class or not
    assert isinstance(calculation, Add)


def test_subtraction_instance():
    """Testing the Calculator Subtract"""
    calculation = Sub.create(tuple_list())
    # unit testing to check whether a sub is an instance of a given class or not
    assert isinstance(calculation, Sub)


def test_multiplication_instance():
    """Testing the Calculator Subtract"""
    calculation = Multiply.create(tuple_list())
    # unit testing to check whether Multiply is an instance of a given class or not
    assert isinstance(calculation, Multiply)


def test_add_get_result_method():
    """Testing the Calculator"""

    calculation = Add.create(tuple_list())
    result = calculation.get_result()
    assert result == 7


def test_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    calculation = Sub.create(tuple_list())
    result = calculation.get_result()
    assert result == -3


def test_multiply_get_result_method():
    """Testing the Calculator Subtract"""
    calculation = Multiply.create(tuple_list())
    result = calculation.get_result()
    assert result == 10
