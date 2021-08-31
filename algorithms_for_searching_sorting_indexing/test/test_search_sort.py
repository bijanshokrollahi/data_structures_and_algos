import unittest
import insertion_sort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        x1 = [0, 2, 4, 5, 6, 7, 8, 10]
        y1 = [-2, 0, 2, 4, 7, 8, 10, 12]
        crossover = insertion_sort.findCrossoverIndex(x1, y1)
        self.assertEqual(crossover, 3)

    def test_something_else(self):
        x2 = [0, 1, 4, 5, 6, 7, 8, 10]
        y2 = [-2, 1.5, 2, 4, 7, 8, 10, 12]
        crossover = insertion_sort.findCrossoverIndex(x2, y2)
        self.assertIn(crossover, [0, 3])

    def test_3(self):
        x1 = [0, 1, 2, 3, 4, 5, 6, 7]
        y1 = [-2, 0, 4, 5, 6, 7, 8, 9]
        crossover = insertion_sort.findCrossoverIndex(x1, y1)
        self.assertEqual(crossover, 1)

    def test_4(self):
        x1 = [0, 1, 2, 3, 4, 5, 6, 7]
        y1 = [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9]
        crossover = insertion_sort.findCrossoverIndex(x1, y1)
        self.assertIn(crossover, [1, 5])

    def test_5(self):
        x1 = [0, 1]
        y1 = [-10, 10]
        crossover = insertion_sort.findCrossoverIndex(x1, y1)
        self.assertEqual(crossover, 0)

    def test_6(self):
        x1 = [0, 1, 2, 3]
        y1 = [-10, -9, -8, 5]
        crossover = insertion_sort.findCrossoverIndex(x1, y1)
        self.assertEqual(crossover, 2)

    def test_7(self):
        n = insertion_sort.integerCubeRoot(7)
        self.assertEqual(n, 1)

    def test_8(self):
        n = insertion_sort.integerCubeRoot(8)
        self.assertEqual(n, 2)

    def test_9(self):
        n = insertion_sort.integerCubeRoot(20)
        self.assertEqual(n, 2)

    def test_10(self):
        n = insertion_sort.integerCubeRoot(26)
        self.assertEqual(n, 2)

    def test_11(self):
        for j in range(27, 64):
            self.assertEqual(insertion_sort.integerCubeRoot(j), 3)

    def test_12(self):
        for j in range(64, 125):
            self.assertEqual(insertion_sort.integerCubeRoot(j), 4)

    def test_14(self):
        for j in range(125, 216):
            self.assertEqual(insertion_sort.integerCubeRoot(j), 5)

    def test_13(self):
        for j in range(216, 343):
            self.assertEqual(insertion_sort.integerCubeRoot(j), 6)

    def test_18(self):
        for j in range(343, 512):
            self.assertEqual(insertion_sort.integerCubeRoot(j), 7)

    def test_15(self):
        lst1 = insertion_sort.kWayMerge([[1, 2, 3], [4, 5, 7], [-2, 0, 6], [5]])
        expected_output = [-2, 0, 1, 2, 3, 4, 5, 5, 6, 7]
        self.assertEqual(lst1, expected_output)

    def test_16(self):
        lst1 = insertion_sort.kWayMerge([[-2, 4, 5, 8], [0, 1, 2], [-1, 3, 6, 7]])
        expected_output = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(lst1, expected_output)

    def test_17(self):
        lst1 = insertion_sort.kWayMerge([[-1, 1, 2, 3, 4, 5]])
        expected_output = [-1, 1, 2, 3, 4, 5]
        self.assertEqual(lst1, expected_output)


if __name__ == '__main__':
    unittest.main()
