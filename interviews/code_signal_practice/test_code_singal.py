import unittest
from code_signal import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        numbers = [1, 2, 1, 3, 4]
        ans = solution(numbers)
        self.assertEqual([1, 1, 0], ans)

    def test_tiny_solution(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        k = 31
        ans = tiny_solution(a, b, k)
        self.assertEqual(2, ans)

    def test_arr_to_string(self):
        ans = array_to_string(['Daisy', 'Rose', 'Hyacinth', 'Poppy'])
        self.assertEqual("DRHPaoyoisapsecpyiynth", ans)

    def test_arr_to_string2(self):
        arr = ["Claire",
               "learned",
               "that",
               "the",
               "Statue",
               "of",
               "Liberty",
               "was",
               "not",
               "always",
               "the",
               "color",
               "that",
               "it",
               "is",
               "now"]
        ans = array_to_string(arr)
        expected_ans = "ClttSoLwnatctiinlehhtfiaolhohtsoaaaeabstwelawirtteaotrnuryreeetsdy"
        self.assertEqual(expected_ans, ans)


if __name__ == '__main__':
    unittest.main()
