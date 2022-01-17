import unittest
from leet_code.max_area_leet import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        max_area = MaxArea([1, 1])
        self.assertEqual(1, max_area.get_area())

    def test_max_area(self):
        max_area = MaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(49, max_area.get_area())

    def test_max_area2(self):
        max_area = MaxArea([])
        self.assertEqual(0, max_area.get_area())

    def test_max_area3(self):
        max_area = MaxArea([0, 0, 0, 0])
        self.assertEqual(0, max_area.get_area())

    def test_max_area4(self):
        max_area = MaxArea([0, 0])
        self.assertEqual(0, max_area.get_area())

    def test_something2(self):
        max_area = MaxAreaNotBruteForce([1, 1])
        self.assertEqual(1, max_area.get_area())

    def test_max_area5(self):
        max_area = MaxAreaNotBruteForce([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(49, max_area.get_area())

    def test_max_area6(self):
        max_area = MaxAreaNotBruteForce([])
        self.assertEqual(0, max_area.get_area())

    def test_max_area7(self):
        max_area = MaxAreaNotBruteForce([0, 0, 0, 0])
        self.assertEqual(0, max_area.get_area())

    def test_max_area8(self):
        max_area = MaxAreaNotBruteForce([0, 0])
        self.assertEqual(0, max_area.get_area())

    def test_max_water_brute(self):
        max_water = MaxTrappedWaterBrute([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, max_water.get_area())

    def test_max_water_brute2(self):
        max_water = MaxTrappedWaterBrute([4, 2, 0, 3, 2, 5])
        self.assertEqual(9, max_water.get_area())

    def test_max_water_brute3(self):
        max_water = MaxTrappedWaterBrute([0, 0])
        self.assertEqual(0, max_water.get_area())

    def test_max_water_brute4(self):
        max_water = MaxTrappedWaterBrute([])
        self.assertEqual(0, max_water.get_area())

    def test_max_water_brute5(self):
        max_water = MaxTrappedWaterBrute([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, max_water.get_area())

    def test_max_water(self):
        max_water = MaxTrappedWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, max_water.get_area())

    def test_max_water2(self):
        max_water = MaxTrappedWater([4, 2, 0, 3, 2, 5])
        self.assertEqual(9, max_water.get_area())

    def test_max_water3(self):
        max_water = MaxTrappedWater([0, 0])
        self.assertEqual(0, max_water.get_area())

    def test_max_water4(self):
        max_water = MaxTrappedWater([])
        self.assertEqual(0, max_water.get_area())

    def test_max_water5(self):
        max_water = MaxTrappedWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, max_water.get_area())

    def test_max_water_elite(self):
        max_water = MaxTrappedWaterElite([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, max_water.get_area())

    def test_max_water_elite2(self):
        max_water = MaxTrappedWaterElite([4, 2, 0, 3, 2, 5])
        self.assertEqual(9, max_water.get_area())

    def test_max_water_elite3(self):
        max_water = MaxTrappedWaterElite([0, 0])
        self.assertEqual(0, max_water.get_area())

    def test_max_water_elite4(self):
        max_water = MaxTrappedWaterElite([])
        self.assertEqual(0, max_water.get_area())

    def test_max_water_elite5(self):
        max_water = MaxTrappedWaterElite([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, max_water.get_area())

    def test_typed_out_strings(self):
        typed_out_strings = TypedOutStrings('abc', 'abc')
        self.assertTrue(typed_out_strings.get_is_equal())

    def test_typed_out_strings2(self):
        typed_out_strings = TypedOutStrings('abc#', 'abc#')
        self.assertTrue(typed_out_strings.get_is_equal())

    def test_typed_out_strings3(self):
        typed_out_strings = TypedOutStrings('', '')
        self.assertTrue(typed_out_strings.get_is_equal())

    def test_typed_out_strings4(self):
        typed_out_strings = TypedOutStrings('###', '##')
        self.assertTrue(typed_out_strings.get_is_equal())

    def test_typed_out_strings5(self):
        typed_out_strings = TypedOutStrings('ab#cd#e', 'ab#cd#e')
        self.assertTrue(typed_out_strings.get_is_equal())

    def test_typed_out_strings6(self):
        typed_out_strings = TypedOutStrings('b#cd#e', 'ab#cd#e')
        self.assertFalse(typed_out_strings.get_is_equal())

    def test_typed_out_strings7(self):
        typed_out_strings = TypedOutStrings('abcde####', 'abcde###')
        self.assertFalse(typed_out_strings.get_is_equal())

    def test_optimal_typed_out_string(self):
        self.assertTrue(string_as_typed('###', '#'))

    def test_optimal_typed_out_string2(self):
        self.assertTrue(string_optimal('###', '#'))

    def test_longest_substring(self):
        self.assertEqual(4, longest_substring('abcaacde'))

    def test_longest_substring2(self):
        self.assertEqual(1, longest_substring('aaaa'))

    def test_longest_substring3(self):
        self.assertEqual(2, longest_substring('abababa'))

    def test_longest_substring4(self):
        self.assertEqual(0, longest_substring(''))

    def test_longest_substring5(self):
        self.assertEqual(5, longest_substring('12345'))

    def test_longest_substring_opt(self):
        self.assertEqual(4, longest_substring_2('abcaacde'))

    def test_longest_substring2_opt(self):
        self.assertEqual(1, longest_substring_2('aaaa'))

    def test_longest_substring3_opt(self):
        self.assertEqual(2, longest_substring_2('abababa'))

    def test_longest_substring4_opt(self):
        self.assertEqual(0, longest_substring_2(''))

    def test_longest_substring5_opt(self):
        self.assertEqual(5, longest_substring_2('12345'))

    def test_longest_substring6_opt(self):
        self.assertEqual(2, longest_substring_2('aabbcc'))


if __name__ == '__main__':
    unittest.main()
