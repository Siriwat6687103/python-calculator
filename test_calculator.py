import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(9, 6), 3)

    def test_sub_nagative(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)

    def test_multiply_nagative(self):
        self.assertEqual(self.calc.multiply(2, -5), -10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_add(self):
        self.assertEqual(self.calc.divide(20, 10), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(11, 3), 2)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(20, 10), 0)    


if __name__ == '__main__':
    unittest.main()