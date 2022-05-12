import unittest
from algorithms_for_searching_sorting_indexing.implementing_from_scratch import *
import numpy as np
import random


class MyTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        for _ in range(0, 1000):
            rand_arr = list(np.random.randint(0, 10000, 100))
            ins_sort = InsertionSort(rand_arr)
            ins_sort.insertion_sort()
            self.assertEqual(ins_sort.get_arr(), sorted(rand_arr))

    def test_binary_search(self):
        for _ in range(0, 100):
            sample = sorted(random.sample(range(0, 20000), 25))
            position = random.randint(0, len(sample)-1)
            binary_search = BinarySearch(sample)
            self.assertEqual(position, binary_search.binary_search(sample[position]))

    def test_merge_sort(self):
        for _ in range(0, 100):
            rand_arr = list(np.random.randint(0, 10000, 100))
            merge_sort = MergeSort(rand_arr)
            merge_sort.merge_sort()
            self.assertEqual(merge_sort.get_arr(), sorted(rand_arr))

    def test_insertion_merge_sort(self):
        for _ in range(0, 1000):
            rand_arr = list(np.random.randint(0, 10000, 100))
            merge_sort = MergeInsertionSort(rand_arr)
            merge_sort.merge_insertion_sort()
            self.assertEqual(merge_sort.get_arr(), sorted(rand_arr))

    def test_bubble_up_heap(self):
        heap = HeapDS([1, 2, 3, 0, 4, 6, 7])
        heap.bubble_up(4)
        self.assertEqual([0, 1, 3, 2, 4, 6, 7], heap.get_heap())

    def test_bubble_up_heap2(self):
        heap = HeapDS([0])
        heap.bubble_up(1)
        self.assertEqual([0], heap.get_heap())

    def test_bubble_up_heap3(self):
        heap = HeapDS([0])
        heap.bubble_up(4)
        self.assertEqual([0], heap.get_heap())

    def test_bubble_up_heap4(self):
        heap = HeapDS([0])
        heap.bubble_up(-4)
        self.assertEqual([0], heap.get_heap())

    def test_bubble_up_heap5(self):
        heap = HeapDS([])
        heap.bubble_up(-4)
        self.assertEqual([], heap.get_heap())

    def test_insert_heap(self):
        heap = HeapDS([0, 1, 3, 2, 4, 6, 7])
        heap.insert(0)
        self.assertEqual([0, 0, 0, 3, 1, 4, 6, 7, 2], heap.keys)

    def test_heapify(self):
        heap = HeapDS([100, 1, 12, 44, 9, 16, 18, 12, 1])
        heap.heapify()
        self.assertEqual([1, 1, 12, 12, 9, 16, 18, 100, 44], heap.get_heap())

    def test_hash_map(self):
        hash_table = HashTable()
        hash_table.insert('a', 44)
        hash_table.insert('b', 55)
        hash_table.insert('c', 2)
        hash_table.insert('d', 57)
        hash_table.insert('e', 122)
        hash_table.insert('f', 1)
        self.assertEqual(6, len(hash_table))
        val = hash_table.get('b')
        self.assertEqual(55, val)
        hash_table.resize_hash_table()
        self.assertEqual(4, hash_table._size_of_arr())
        val = hash_table.get('z')
        self.assertIsNone(val)

    def test_hash_table_delete(self):
        hash_table = HashTable()
        hash_table.insert('a', 44)
        hash_table.insert('b', 55)
        hash_table.insert('c', 2)
        hash_table.insert('d', 57)
        hash_table.insert('e', 122)
        hash_table.insert('f', 1)
        hash_table.insert('g', 12)
        hash_table.insert('h', 11)
        self.assertTrue(hash_table.delete('a'))
        val = hash_table.get('a')
        self.assertIsNone(val)

    def test_quick_sort(self):
        arr = [0, 4, -1, 55, 12, 8, 12]
        qs = QuickSort(arr)
        qs.sort()
        self.assertEqual(sorted(arr), qs.arr)

    def test_quick_sort2(self):
        arr = []
        qs = QuickSort(arr)
        qs.sort()
        self.assertEqual(sorted(arr), qs.arr)

    def test_quick_sort3(self):
        arr = [4]
        qs = QuickSort(arr)
        qs.sort()
        self.assertEqual(sorted(arr), qs.arr)

    def test_quick_sort4(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        qs = QuickSort(arr)
        qs.sort()
        self.assertEqual(sorted(arr), qs.arr)

    def test_qu5(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        qs = QuickSort(arr)
        qs.sort()
        self.assertEqual(sorted(arr), qs.arr)

    def test_quick_select(self):
        arr = [110, 10, 2, 35, 46, 5]
        qs = QuickSelect(arr)
        ele = qs.quick_select(1)
        self.assertEqual(5, ele)

    def test_bst(self):
        bst = Bst(50)
        bst.insert(25)
        bst.insert(24)
        bst.insert(54)
        bst.insert(124)
        bst.insert(12)
        bst.insert(126)
        bst.insert(156)
        bst.insert(6)
        bst.insert(5)
        self.assertEqual(50, bst.find(50).val)

    def test_bst_height(self):
        bst = Bst(50)
        bst.insert(25)
        bst.insert(24)
        bst.insert(54)
        bst.insert(124)
        bst.insert(12)
        bst.insert(126)
        bst.insert(156)
        bst.insert(6)
        bst.insert(5)
        height = bst.height()
        self.assertEqual(6, height)

    def test_bst_post_order_traversal(self):
        bst = Bst(50)
        bst.insert(25)
        bst.insert(30)
        bst.insert(24)
        bst.insert(54)
        bst.insert(52)
        bst.insert(124)
        bst.insert(12)
        bst.insert(126)
        bst.insert(125)
        bst.insert(156)
        bst.insert(6)
        bst.insert(7)
        bst.insert(5)
        bst.post_order_traversal(bst.head)

    def test_bst_pre_order_traversal(self):
        bst = Bst(50)
        bst.insert(25)
        bst.insert(30)
        bst.insert(24)
        bst.insert(54)
        bst.insert(52)
        bst.insert(124)
        bst.insert(12)
        bst.insert(126)
        bst.insert(125)
        bst.insert(156)
        bst.insert(6)
        bst.insert(7)
        bst.insert(5)
        bst.pre_order_traversal(bst.head)

    def test_bst_in_order_traversal(self):
        bst = Bst(50)
        bst.insert(25)
        bst.insert(30)
        bst.insert(24)
        bst.insert(54)
        bst.insert(52)
        bst.insert(124)
        bst.insert(12)
        bst.insert(126)
        bst.insert(125)
        bst.insert(156)
        bst.insert(6)
        bst.insert(7)
        bst.insert(5)
        bst.in_order_traversal(bst.head)

    def test_max_subarray_(self):
        arr = [0, 10, 155, 22, -250, 12000]
        max_val = max_subarray(arr, 0, len(arr)-1)
        self.assertEqual(12250, max_val)


if __name__ == '__main__':
    unittest.main()
