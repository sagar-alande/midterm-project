"""Calculation class with Addition, Multiplication, and Subtraction Classes """
#from calculator.oprations import Addition as Add, Subtraction as Sub, Multiplication as Mult


class Calculation:
    """ calculation abstract base class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, tuple_list: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """ factory method"""
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """ standardize values to list of floats"""

        list_values_float = []
        for item in tuple_list:
            list_values_float.append(float(item))
        return tuple(list_values_float)


class Addition(Calculation):
    """ calculation addition class"""

    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values


class Multiplication(Calculation):
    """multiplication calculation object"""

    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = value * result
        return result


class Subtraction(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """get the subtraction results"""
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values = difference_of_values - value
        return difference_of_values
