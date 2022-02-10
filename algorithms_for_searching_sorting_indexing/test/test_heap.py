import unittest
from algorithms_for_searching_sorting_indexing.basic_ds_and_heaps import MinHeap, TopKHeap, MaxHeap, \
    MedianMaintainingHeap


class MyTestCase(unittest.TestCase):
    def test_something(self):
        heap = MinHeap()
        heap.insert(5)
        self.assertEqual(heap.min_element(), 5)
        heap.insert(2)
        self.assertEqual(heap.min_element(), 2)
        heap.insert(4)
        self.assertEqual(heap.min_element(), 2)
        heap.insert(-1)
        self.assertEqual(heap.min_element(), -1)
        heap.insert(7)
        self.assertEqual(heap.min_element(), -1)
        # delete
        heap.delete_min()
        self.assertEqual(heap.min_element(), 2)
        heap.delete_min()
        self.assertEqual(heap.min_element(), 4)
        heap.delete_min()
        self.assertEqual(heap.min_element(), 5)
        heap.delete_min()
        self.assertEqual(heap.min_element(), 7)
        heap.delete_min()
        # self.assertEqual(heap.size(), 0)

    def test_heap_top_k(self):
        h = TopKHeap(5)
        # Force the array A
        h.A = [-10, -9, -8, -4, 0]
        # Force the heap to this heap
        [h.H.insert(elt) for elt in [1, 4, 5, 6, 15, 22, 31, 7]]

        print('Initial data structure: ')
        print('\t A = ', h.A)
        print('\t H = ', h.H)

        # Insert an element -2
        print('Test 1: Inserting element -2')
        h.insert(-2)
        print('\t A = ', h.A)
        print('\t H = ', h.H)
        # After insertion h.A should be [-10, -9, -8, -4, -2]
        # After insertion h.H should be [None, 0, 1, 5, 4, 15, 22, 31, 7, 6]
        self.assertEqual(h.A, [-10, -9, -8, -4, -2])
        self.assertEqual(h.H.min_element(), 0)
        h.satisfies_assertions()

        print('Test2: Inserting element -11')
        h.insert(-11)
        print('\t A = ', h.A)
        print('\t H = ', h.H)
        self.assertEqual(h.A, [-11, -10, -9, -8, -4])
        self.assertEqual(h.H.min_element(), -2)
        h.satisfies_assertions()

        print('Test 3 delete_top_k(3)')
        h.delete_top_k(3)
        print('\t A = ', h.A)
        print('\t H = ', h.H)
        h.satisfies_assertions()
        self.assertEqual(h.A, [-11, -10, -9, -4, -2])
        self.assertEqual(h.H.min_element(), 0)
        h.satisfies_assertions()

        print('Test 4 delete_top_k(4)')
        h.delete_top_k(4)
        print('\t A = ', h.A)
        print('\t H = ', h.H)
        self.assertEqual(h.A, [-11, -10, -9, -4, 0])
        h.satisfies_assertions()

        print('Test 5 delete_top_k(0)')
        h.delete_top_k(0)
        print('\t A = ', h.A)
        print('\t H = ', h.H)
        self.assertEqual(h.A, [-10, -9, -4, 0, 1])
        h.satisfies_assertions()

        print('Test 6 delete_top_k(1)')
        h.delete_top_k(1)
        print('\t A = ', h.A)
        print('\t H = ', h.H)
        self.assertEqual(h.A, [-10, -4, 0, 1, 4])
        h.satisfies_assertions()

    def test_max_heap(self):
        h = MaxHeap()
        print('Inserting: 5, 2, 4, -1 and 7 in that order.')
        h.insert(5)
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 5)
        h.insert(2)
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 5)
        h.insert(4)
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 5)
        h.insert(-1)
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 5)
        h.insert(7)
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 7)
        h.satisfies_assertions()

        print('Deleting maximum element')
        h.delete_max()
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 5)
        h.delete_max()
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 4)
        h.delete_max()
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), 2)
        h.delete_max()
        print(f'\t Heap = {h}')
        self.assertEqual(h.max_element(), -1)
        # Test delete_max on heap of size 1, should result in empty heap.
        h.delete_max()
        print(f'\t Heap = {h}')
        print('All tests passed: 5 points!')

    def test_median_heap(self):
        m = MedianMaintainingHeap()
        print('Inserting 1, 5, 2, 4, 18, -4, 7, 9')

        m.insert(1)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()
        self.assertEqual(m.get_median(), 1)

        m.insert(5)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()
        self.assertEqual(m.get_median(), 3)

        m.insert(2)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()

        self.assertEqual(m.get_median(), 2)
        m.insert(4)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()
        self.assertEqual(m.get_median(), 3)

        m.insert(18)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()
        self.assertEqual(m.get_median(), 4)

        m.insert(-4)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()
        self.assertEqual(m.get_median(), 3)

        m.insert(7)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()
        self.assertEqual(m.get_median(), 4)

        m.insert(9)
        print(m)
        print(m.get_median())
        m.satisfies_assertions()
        self.assertEqual(m.get_median(), 4.5)

        print('All tests passed: 15 points')


if __name__ == '__main__':
    unittest.main()
