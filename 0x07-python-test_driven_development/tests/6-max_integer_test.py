#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for Max integer"""

    def test_max_integer(self):
        """Cases"""
        self.assertEqual(max_integer([10, 7, 12]), 12)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([11, -1, -3, -8]), 11)
        self.assertEqual(max_integer([646980, 10756, -96]), 646980)
        self.assertEqual(max_integer([10, 24, -7]), 24)
        self.assertEqual(max_integer([-12, -9, -22]), -9)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([13]), 13)
        self.assertEqual(max_integer([2, 26, 9]), 26)

if __name__ == '__main__':
    unittest.main()
