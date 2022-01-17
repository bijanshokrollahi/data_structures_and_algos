"""
copyright bijan shokrollahi
01.14.2022

"""

import unittest
from circle_ci_assessment import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix = [
            [1, 0, 2, 1, 1, 1, 1],
            [1, 2, 2, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 2, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 2, 1],
            [1, 0, 0, 1, 1, 1, 0]
        ]
        max_len = max_diagonal_match(matrix)
        self.assertEqual(7, max_len)

    def test_something2(self):
        matrix = [
            [1, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        max_len = max_diagonal_match(matrix)
        self.assertEqual(12, max_len)

    def test_something3(self):
        matrix = []
        max_len = max_diagonal_match(matrix)
        self.assertEqual(0, max_len)


if __name__ == '__main__':
    unittest.main()
