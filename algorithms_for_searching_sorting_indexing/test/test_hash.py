import unittest
from hash_assignment import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = 11
        a = 8
        for i in range(0, 11):
            print((a*i) % p)

    def test_if_partitioned(self):
        self.assertTrue(testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 10, 23], 5))
        self.assertFalse(testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 11, 23], 4))
        self.assertTrue(testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 23, 21], 0))
        self.assertTrue(testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 22, 23], 9))
        self.assertFalse(testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 8, 23], 5))
        self.assertFalse(testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 13, 9, -11], 5))
        self.assertTrue(testIfPartitioned([4, 4, 4, 4, 4, 8, 9, 13, 9, 11], 4))
        print('Passed all tests (10 points)')

    def test_break_partition1(self):
        try:
            a1 = [10, 9, 8, 7, 6, 5, -99]
            j1 = tryPartition(a1)
            assert not testIfPartitioned(a1, j1)
            print('Partitioning was unsuccessful - this is what you were asked to break the code')
        except Exception as e:
            print(f'Assertion failed {e} - this is fine since you were asked to break the code.')

    def test_break_partition2(self):
        try:
            a2 = [10, 9, 8, 7, 6, 5, -199]
            j2 = tryPartition(a2)
            assert not testIfPartitioned(a2, j2)
        except Exception as e:
            print(f'Assertion failed {e} - this is fine since you were asked to break the code.')

    def test_rapid_sorting(self):
        a = [1, 3, 6, 1, 5, 4, 1, 1, 2, 3, 3, 1, 3, 5, 2, 2, 4]
        print(a)
        simplePartition(a, 1)
        print(a)
        assert (a[:5] == [1, 1, 1, 1, 1]), 'Simple partition test 1 failed'

        simplePartition(a, 2)
        print(a)
        assert (a[:5] == [1, 1, 1, 1, 1]), 'Simple partition test 2(A) failed'
        assert (a[5:8] == [2, 2, 2]), 'Simple Partition test 2(B) failed'

        simplePartition(a, 3)
        print(a)
        assert (a[:5] == [1, 1, 1, 1, 1]), 'Simple partition test 3(A) failed'
        assert (a[5:8] == [2, 2, 2]), 'Simple Partition test 3(B) failed'
        assert (a[8:12] == [3, 3, 3, 3]), 'Simple Partition test 3(C) failed'

        simplePartition(a, 4)
        print(a)
        assert (a[:5] == [1, 1, 1, 1, 1]), 'Simple partition test 4(A) failed'
        assert (a[5:8] == [2, 2, 2]), 'Simple Partition test 4(B) failed'
        assert (a[8:12] == [3, 3, 3, 3]), 'Simple Partition test 4(C) failed'
        assert (a[12:14] == [4, 4]), 'Simple Partition test 4(D) failed'

        simplePartition(a, 5)
        print(a)
        assert (a == [1] * 5 + [2] * 3 + [3] * 4 + [4] * 2 + [5] * 2 + [6]), 'Simple Parition test 5 failed'

        print('Passed all tests : 10 points!')

    def test_matrix_multiplication(self):
        H = [[0, 1, 0, 1], [1, 0, 0, 0], [1, 0, 1, 1]]
        a = [1, 1, 1, 0]
        resp = matrix_multiplication(H, a)
        self.assertEqual(resp, [1, 1, 0])

    def test_matrix_random(self):
        A1 = [[0, 1, 0, 1], [1, 0, 0, 0], [1, 0, 1, 1]]
        b1 = [1, 1, 1, 0]
        c1 = matrix_multiplication(A1, b1)
        print('c1=', c1)
        self.assertEqual(c1, [1, 1, 0])

        A2 = [[1, 1], [0, 1]]
        b2 = [1, 0]
        c2 = matrix_multiplication(A2, b2)
        print('c2=', c2)
        self.assertEqual(c2, [1, 0])

        A3 = [[1, 1, 1, 0], [0, 1, 1, 0]]
        b3 = [1, 0, 0, 1]
        c3 = matrix_multiplication(A3, b3)
        print('c3=', c3)
        self.assertEqual(c3, [1, 0])

        H = return_random_hash_function(5, 4)
        print('H=', H)
        assert len(H) == 5, 'Test 5 failed'
        assert all(len(row) == 4 for row in H), 'Test 6 failed'
        assert all(elt == 0 or elt == 1 for row in H for elt in row), 'Test 7 failed'

        H2 = return_random_hash_function(6, 3)
        print('H2=', H2)
        assert len(H2) == 6, 'Test 8 failed'
        assert all(len(row) == 3 for row in H2), 'Test 9 failed'
        assert all(elt == 0 or elt == 1 for row in H2 for elt in row), 'Test 10 failed'
        print('Tests passed: 10 points!')

    def test_quiz(self):
        keys = []
        vals = [3, 5, 10, 13, 14]
        for val in vals:
            for i in range(0, 10):
                ans = (val + i) % 10
                if ans not in keys:
                    keys.append(ans)
                    keys.append((val, ans))
                    break
        print(keys)
        self.assertIsNotNone(keys)


if __name__ == '__main__':
    unittest.main()
