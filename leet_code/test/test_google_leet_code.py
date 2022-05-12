from leet_code.google_leet_code import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ans = maxScore([1, 2, 3, 4, 5, 6, 1], 3)
        self.assertEqual(12, ans)

    def test_max_count(self):
        ans = maxScore([2, 2, 2], 2)
        self.assertEqual(4, ans)

    def test_max_count2(self):
        ans = maxScore([9, 7, 7, 9, 7, 7, 9], 7)
        self.assertEqual(55, ans)

    def test_max_count3(self):
        ans = maxScore([], 2)
        self.assertEqual(0, ans)

    def test_max_count4(self):
        ans = maxScore([11, 0, 0, 5, 6, 1], 3)
        self.assertEqual(18, ans)

    def test_max_count5(self):
        ans = maxScore([], 0)
        self.assertEqual(0, ans)

    def test_max_val_equation(self):
        ans = find_max_value_of_equation([[1, 3], [2, 0], [5, 10], [6, -10]], 1)
        self.assertEqual(4, ans)

    def test_max_val_equation2(self):
        ans = find_max_value_of_equation([[-19, 9], [-15, -19], [-5, -8]], 10)
        self.assertEqual(-6, ans)

    def test_max_val_equation3(self):
        ans = find_max_value_of_equation2([[1, 3], [2, 0], [5, 10], [6, -10]], 1)
        self.assertEqual(4, ans)

    def test_max_val_equation4(self):
        ans = find_max_value_of_equation2([[-19, 9], [-15, -19], [-5, -8]], 10)
        self.assertEqual(-6, ans)


if __name__ == '__main__':
    unittest.main()
