import unittest

from src.calculator import sum, subtract, multiply, divide

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5
    
    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_multiply(self):
        assert multiply(3, 5) == 15

    def test_divide(self):
        result = divide(0, 2)
        expected = 0
        assert result == expected

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Division not permited"):
            divide(15, 0)