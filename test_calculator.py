"""Unit tests for the calculator library."""

import calculator


class TestCalculator:
    """General Tests."""

    def test_addition(self):
        """Test."""
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        """Test."""
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        """Test."""
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        """Test."""
        assert 5 == calculator.divide(10, 2)


class TestAddition:
    """Addition Tests."""

    def test_addition_0(self):
        """Test."""
        assert 0 == calculator.add(0, 0)

    def test_addition_0_1(self):
        """Test."""
        assert 1 == calculator.add(0, 1)

    def test_addition_1_1(self):
        """Test."""
        assert 2 == calculator.add(1, 1)

    def test_addition_hughe(self):
        """Test."""
        assert 1000000000000 == calculator.add(1, 999999999999)


class TestSubtraction:
    """Subtraction Tests."""

    def test_subtraction_0(self):
        """Test."""
        assert 0 == calculator.subtract(0, 0)

    def test_subtraction_1_0(self):
        """Test."""
        assert 1 == calculator.subtract(1, 0)

    def test_subtraction_1_1(self):
        """Test."""
        assert 0 == calculator.subtract(1, 1)

    def test_subtraction_2_1(self):
        """Test."""
        assert 1 == calculator.subtract(2, 1)

    def test_subtraction_minus(self):
        """Test."""
        assert 2 == calculator.subtract(1, -1)

    def test_substraction_negative(self):
        """Test."""
        assert -1 == calculator.subtract(1, 2)

    def test_substraction_hughe(self):
        """Test."""
        assert 999999999999 == calculator.subtract(1000000000000, 1)


class TestMultiply:
    """Multiply Tests."""

    def test_multiply_0(self):
        """Test."""
        assert 0 == calculator.multiply(0, 0)
        assert 0 == calculator.multiply(0, 1)


class TestSquare:
    """Square Tests."""

    def test_square_0(self):
        """Test."""
        assert -1 == calculator.square(1, 0)
        assert 1 == calculator.square(1, 1)
        assert 9 == calculator.square(3, 2)
