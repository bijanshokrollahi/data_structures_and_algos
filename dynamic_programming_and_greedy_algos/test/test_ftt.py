"""
copyright bijan shokrollahi
10.06.2021

"""
import unittest
from dynamic_programming_and_greedy_algos.fast_fourier_transformation import *
from random import randint


class MyTestCase(unittest.TestCase):
    def test_max_subarray(self):
        self.assertEqual(25, maxSubArray([100, -2, 5, 10, 11, -4, 15, 9, 18, -2, 21, -11]))
        self.assertEqual(26, maxSubArray([-5, 1, 10, 4, 11, 4, 15, 9, 18, 0, 21, -11]))
        self.assertEqual(18, maxSubArray([26, 0, 5, 18, 11, -1, 15, 9, 13, 5, 16, -11]))

        def get_random_array(n):
            assert (n > 100)
            lst = [randint(0, 25) for j in range(n)]
            lst[0] = 1000
            lst[10] = -15
            lst[25] = 40
            lst[n - 10] = 60
            lst[n - 3] = -40
            return lst

        self.assertEqual(75, maxSubArray(get_random_array(50000)))
        self.assertEqual(75, maxSubArray(get_random_array(500000)))
        print('All tests passed (10 points!)')

    def test_multiplication_ftt(self):
        def check_poly(lst1, lst2):
            print(f'Your code found: {lst1}')
            print(f'Expected: {lst2}')
            self.assertEqual(len(lst1), len(lst2))
            for (k, j) in zip(lst1, lst2):
                self.assertTrue(abs(k - j) <= 1E-05)
            print('Passed!')

        print('-------')
        print('Test # 1')
        # multiply (1 + x - x^3) with (2 - x + x^2)
        a = [1, 1, 0, -1]
        b = [2, -1, 1]
        c = polynomial_multiply(a, b)
        self.assertEqual(6, len(c))
        print(f'c={c}')
        check_poly(c, [2, 1, 0, -1, 1, -1])
        print('-------')
        print('Test # 2')
        # multiply 1 - x + x^2 + 2 x^3 + 3 x^5 with
        #            -x^2 + x^4 + x^6
        a = [1, -1, 1, 2, 0, 3]
        b = [0, 0, -1, 0, 1, 0, 1]
        c = polynomial_multiply(a, b)
        self.assertEqual(12, len(c))
        print(f'c={c}')
        check_poly(c, [0, 0, -1, 1, 0, -3, 2, -2, 1, 5, 0, 3])
        print('-------')
        print('Test # 3')
        # multiply 1 - 2x^3 + x^7 - 11 x^11
        # with     2 - x^4 - x^6 + x^8
        a = [1, 0, 0, -2, 0, 0, 0, 1, 0, 0, 0, -11]
        b = [2, 0, 0, 0, -1, 0, -1, 0, 1]
        c = polynomial_multiply(a, b)
        self.assertEqual(20, len(c))
        print(f'c={c}')
        check_poly(c, [2, 0, 0, -4, -1, 0, -1, 4, 1, 2, 0, -25, 0, -1, 0, 12, 0, 11, 0, -11])
        print('All tests passed (10 points!)')

    def test_checksum_exists(self):
        print('-- Test 1 --')
        a = {1, 2, 10, 11}
        b = {2, 5, 8, 10}
        c = {1, 2, 5, 8}
        self.assertFalse(check_sum_exists(a, b, c, 12))
        print('Passed')
        print('-- Test 2 --')
        a = {1, 2, 10, 11}
        b = {2, 5, 8, 10}
        c = {1, 2, 5, 8, 11}
        self.assertTrue(check_sum_exists(a, b, c, 12))

        print('Passed')

        print('-- Test 3 --')
        a = {1, 4, 5, 7, 11, 13, 14, 15, 17, 19, 22, 23, 24, 28, 34, 35, 37, 39, 42, 44}
        b = {0, 1, 4, 9, 10, 11, 12, 15, 18, 20, 25, 31, 34, 36, 38, 40, 43, 44, 47, 49}
        c = {3, 4, 5, 7, 8, 10, 19, 20, 21, 24, 31, 35, 36, 37, 38, 39, 42, 44, 46, 49}
        self.assertTrue(check_sum_exists(a, b, c, 50))
        print('-- Test 4 --')

        a = {98, 2, 99, 40, 77, 79, 87, 88, 89, 27}
        b = {64, 66, 35, 69, 70, 40, 76, 45, 12, 60}
        c = {36, 70, 10, 44, 15, 16, 83, 20, 84, 55}
        self.assertFalse(check_sum_exists(a, b, c, 100))
        print('All Tests Passed (15 points)!')


if __name__ == '__main__':
    unittest.main()
