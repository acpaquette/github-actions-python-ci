import unittest

from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 4), 1)
        self.assertEqual(subtract(3, 12), -9)
        self.assertEqual(subtract(5, 0), 5)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(3, 4), 0.75)
        self.assertEqual(divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main() 
