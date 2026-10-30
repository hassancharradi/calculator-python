
import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(5, "+", 3), 8)

    def test_subtraction(self):
        self.assertEqual(calculate(5, "-", 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculate(5, "*", 3), 15)

    def test_division(self):
        self.assertEqual(calculate(6, "/", 3), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(5, "/", 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(5, "%", 3)


if __name__ == "__main__":
    unittest.main()
