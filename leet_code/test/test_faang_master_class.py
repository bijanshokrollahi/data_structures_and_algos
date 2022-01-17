"""
copyright bijan shokrollahi
01.11.2022

"""
import unittest
from leet_code.faang_master_class import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        self.assertIsNotNone(linked_list.get_head())
        self.assertEqual(5, linked_list.get_len())

    def test_reverse(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        reversed = linked_list.reverse()
        self.assertIsNotNone(reversed)


if __name__ == '__main__':
    unittest.main()
