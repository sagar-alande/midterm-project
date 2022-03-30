""" This is the Calculator Class"""
from calculator.calculations import Addition as Add, Subtraction as Subtract, Multiplication as Multiply


class Calculator:
    """ This is the default result property"""
    result=0

    @staticmethod
    def add(self, tuple_list):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Add.create(tuple_list)
        self.result = calculation.get_result()
        return self.result

    @staticmethod
    def subtract(self, tuple_list):
        """ This is the subtract method"""
        calculation = Subtract.create(tuple_list)
        # Call the static method to return the subtraction and set it to the calculator result property
        self.result = calculation.get_result()
        return self.result

    @staticmethod
    def multiply(self, tuple_list):
        """ This is the subtract method"""
        calculation = Multiply.create(tuple_list)
        # Call the static method to return the multiplication and set it to the calculator result property
        self.result = calculation.get_result()
        return self.result
