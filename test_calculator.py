import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive(self):
        self.assertEqual(self.calc.add(3, 7), 10)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-5, -8), -13)

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-3, -10), 7)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # Test cases for divide()
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_non_divisible(self):
        self.assertEqual(self.calc.divide(9, 2), 4)  # Integer division expected

    # Test cases for modulo()
    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_divisible(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

if __name__ == '__main__':
    unittest.main()
