"""
copyright bijan shokrollahi
11.08.2021

"""

import unittest
from leet import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_something(self):
        ans = self.solution.findMedianSortedArrays([1, 2], [2])
        self.assertEqual(2, ans)

    def test_2(self):
        ans = self.solution.findMedianSortedArrays([1, 2], [3, 4])
        self.assertEqual(2.5, ans)

    def test_is_pal(self):
        is_pal = self.solution.is_palindrome(10101)
        self.assertTrue(is_pal)
        is_pal2 = self.solution.is_palindrome(-121)
        self.assertFalse(is_pal2)
        is_pal3 = self.solution.is_palindrome(10)
        self.assertFalse(is_pal3)
        is_pal4 = self.solution.is_palindrome(-101)
        self.assertFalse(is_pal4)

    def test_add_two_numbers(self):
        list_node_1 = self.solution.create_list_node([9, 9, 9, 9, 9, 9, 9])
        list_node_2 = self.solution.create_list_node([9, 9, 9, 9])
        ans = self.solution.addTwoNumbers(list_node_1, list_node_2)
        ans_list = self.solution.to_list(ans)
        self.assertEqual([8, 9, 9, 9, 0, 0, 0, 1], ans_list)

    def test_longest_substring(self):
        ans = self.solution.length_of_longest_substring("abcabcbb")
        self.assertEqual(3, ans)

    def test_longest_substring2(self):
        ans = self.solution.length_of_longest_substring("bbbbb")
        self.assertEqual(1, ans)

    def test_longest_substring3(self):
        ans = self.solution.length_of_longest_substring("pwwkew")
        self.assertEqual(3, ans)

    def test_longest_substring4(self):
        ans = self.solution.length_of_longest_substring("")
        self.assertEqual(0, ans)

    def test_longest_substring5(self):
        ans = self.solution.length_of_longest_substring("rlcsautpzrriinmflpqcc")
        self.assertEqual(9, ans)

    def test_hamming_weight(self):
        ans = self.solution.hammingWeight('00000000000000000000000000001011')
        self.assertEqual(3, ans)

    def test_group_anagram(self):
        ans = self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]], ans)

    def test_two_sum(self):
        indicies = self.solution.two_sum_2([1, 2, 5, 8, 10], 11)
        self.assertEqual((0, 4), indicies)

    def test_two_sum2(self):
        indicies = self.solution.two_sum_2([0, 0, 0, 0, 0, 0], 1)
        self.assertEqual((), indicies)

    def test_two_sum3(self):
        indicies = self.solution.two_sum_2([1], 2)
        self.assertEqual((), indicies)

    def test_two_sum4(self):
        indicies = self.solution.two_sum_2([], 0)
        self.assertEqual((), indicies)

    def test_two_sum5(self):
        indicies = self.solution.two_sum_2([-1, -99, 56, 1, 12], 0)
        self.assertEqual((0, 3), indicies)

    def test_largest_bucket(self):
        ans = self.solution.largest_bucket([10, 0, 0, 0, 10])
        self.assertEqual(40, ans)

    def test_largest_bucket2(self):
        ans = self.solution.largest_bucket([])
        self.assertEqual(0, ans)

    def test_largest_bucket3(self):
        ans = self.solution.largest_bucket([5, 0, 0, 0, 10])
        self.assertEqual(20, ans)

    def test_largest_bucket4(self):
        ans = self.solution.largest_bucket([10])
        self.assertEqual(0, ans)


if __name__ == '__main__':
    unittest.main()
