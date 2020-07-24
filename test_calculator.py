"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 5 == calculator.divide(10, 2)


class TestAddition:

    def test_addition_0(self):
        assert 0 == calculator.add(0, 0)

    def test_addition_0_1(self):
        assert 1 == calculator.add(0, 1)

    def test_addition_1_1(self):
        assert 2 == calculator.add(1, 1)

    def test_addition_hughe(self):
        assert 1000000000000 == calculator.add(1, 999999999999)


class TestSubtraction:

    def test_subtraction_0(self):
        assert 0 == calculator.subtract(0, 0)

    def test_subtraction_1_0(self):
        assert 1 == calculator.subtract(1, 0)

    def test_subtraction_1_1(self):
        assert 0 == calculator.subtract(1, 1)

    def test_subtraction_2_1(self):
        assert 1 == calculator.subtract(2, 1)

    def test_subtraction_minus(self):
        assert 2 == calculator.subtract(1, -1)

    def test_substraction_negative(self):
        assert -1 == calculator.subtract(1, 2)

    def test_substraction_hughe(self):
        assert 999999999999 == calculator.subtract(1000000000000, 1)
