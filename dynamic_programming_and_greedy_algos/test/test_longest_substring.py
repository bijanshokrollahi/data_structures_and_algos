"""
copyright bijan shokrollahi
10.27.2021

"""
import unittest
from dynamic_programming_and_greedy_algos.longest_substring import *


class MyTestCase(unittest.TestCase):
    def test_lss_length(self):
        # test 1
        n1 = lssLength([1, 4, 2, -2, 0, -1, 2, 3], 0, -1)
        print(n1)
        self.assertEqual(4, n1)
        # test 2
        n2 = lssLength([1, 2, 3, 4, 0, 1, -1, -2, -3, -4, 5, -5, -6], 0, -1)
        print(n2)
        self.assertEqual(8, n2)
        # test 3
        n3 = lssLength([0, 2, 4, 6, 8, 10, 12], 0, -1)
        print(n3)
        self.assertEqual(1, n3)
        # test 4
        n4 = lssLength(
            [4, 8, 7, 5, 3, 2, 5, 6, 7, 1, 3, -1, 0, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1, 2, 4, 5, 0, 2, -3, -9, -4, -2, -3,
             -1], 0, -1)
        print(n4)
        self.assertEqual(14, n4)

    def test_memoize_recurrence(self):
        print('-- Test 1 -- ')
        a1 = [1, 4, 2, -2, 0, -1, 2, 3]
        print(a1)
        T1 = memoizeLSS(a1)
        checkMemoTableHasEntries(a1, T1)
        checkMemoTableBaseCase(a1, T1)
        self.assertEqual(4, T1[(0, -1)])
        print('Passed')

        print('--Test2--')
        a2 = [1, 2, 3, 4, 0, 1, -1, -2, -3, -4, 5, -5, -6]
        print(a2)
        T2 = memoizeLSS(a2)
        checkMemoTableHasEntries(a2, T2)
        checkMemoTableBaseCase(a2, T2)
        assert T2[(0, -1)] == 8, f'Test 2: Expected answer is 8. Your code returns {T2[(0, -1)]}'

        print('--Test3--')
        a3 = [0, 2, 4, 6, 8, 10, 12]
        print(a3)
        T3 = memoizeLSS(a3)
        checkMemoTableHasEntries(a3, T3)
        checkMemoTableBaseCase(a3, T3)
        assert T3[(0, -1)] == 1, f'Test 3: Expected answer is  1. Your code returns {T3[(0, -1)]}'

        print('--Test4--')
        a4 = [4, 8, 7, 5, 3, 2, 5, 6, 7, 1, 3, -1, 0, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1, 2, 4, 5, 0, 2, -3, -9, -4, -2,
              -3, -1]
        print(a4)
        T4 = memoizeLSS(a4)
        checkMemoTableHasEntries(a4, T4)
        checkMemoTableBaseCase(a4, T4)
        assert T4[(0, -1)] == 14, f'Text 4: Expected answer is 14. Your code returns {T4[(0, -1)]}'

        print('All tests passed (7 points)')


    def test_lss_memo_2(self):
        print('--Test4--')
        a4 = [4, 8, 7, 5, 3, 2, 5, 6, 7, 1, 3, -1, 0, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1, 2, 4, 5, 0, 2, -3, -9, -4, -2,
              -3, -1]
        print(a4)
        T4 = memoizeLSS(a4)
        checkMemoTableHasEntries(a4, T4)
        checkMemoTableBaseCase(a4, T4)
        self.assertEqual(14, T4[(0, -1)])

    def test_os_test(self):
        import os
        ret_val = {}
        for root, dirs, files in os.walk('.', topdown=False):
            if '.DS_Store' not in root and root.rsplit('/')[-1] != '.':
                ret_val[root] = files
        self.assertIsNotNone(ret_val)


if __name__ == '__main__':
    unittest.main()
