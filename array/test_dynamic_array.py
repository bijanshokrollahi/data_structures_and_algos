import unittest
from dynamic_array import DynamicArray
import sys


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = DynamicArray()
        arr.append(5)
        self.assertEqual(1, len(arr))

    def test_dynamic_array(self):
        arr = DynamicArray()
        arr.append(5)
        arr.append(6)
        arr.append(7)
        self.assertEqual(6, arr[1])

    def test_dynamic_sizing(self):
        arr = DynamicArray()
        for i in range(0, 100000):
            arr.append(i)
            print("len {0}, size {1}".format(arr.n, sys.getsizeof(arr)))

    @staticmethod
    def is_anagram(arr_1, arr_2) -> bool:
        return sorted(arr_1) == sorted(arr_2)

    @staticmethod
    def is_anagram_2(arr_1, arr_2) -> bool:
        arr_1 = arr_1.replace(' ', '').lower()
        arr_2 = arr_2.replace(' ', '').lower()
        if len(arr_1) != len(arr_2):
            return False
        count = {}
        for item in arr_1:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1

        for item in arr_2:
            if item in count:
                count[item] = count[item] - 1
            else:
                return False

        for val in count.values():
            if val != 0:
                return False
        return True

    def test_is_anagram(self):
        str1 = "tacocat"
        str2 = "cattaco"
        self.assertTrue(self.is_anagram_2(str2, str1))

    def test_anagram2(self):
        str1 = "cat"
        str2 = "dog"
        self.assertFalse(self.is_anagram_2(str1, str2))

    def test_anagram3(self):
        str1 = "clinteastwood"
        str2 = "oldwestaction"
        self.assertTrue(self.is_anagram_2(str1, str2))

    @staticmethod
    def pair_sum(num_list, sum) -> list:
        ans = []
        for i in range(0, len(num_list)-1):
            for j in range(i+1, len(num_list)):
                if num_list[i] + num_list[j] == sum:
                    ans.append((num_list[i], num_list[j]))
        return ans

    def test_unique_pairs(self):
        pairs = [1, 3, 2, 2]
        sum = 4
        ans = self.pair_sum(pairs, sum)
        print(ans)
        self.assertEqual(2, len(ans))


if __name__ == '__main__':
    unittest.main()
