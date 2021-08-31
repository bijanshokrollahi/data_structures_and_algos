import unittest
from trees_and_graphs_basics.bst import *


class MyTestCase(unittest.TestCase):
    def test_bst_insert(self):
        t1 = Node(25, None)
        t2 = Node(12, t1)
        t3 = Node(18, t2)
        t4 = Node(40, t1)

        print('-- Testing basic node construction (originally provided code) -- ')
        self.assertEqual(t1.left, t2)
        self.assertEqual(t2.parent, t1)
        self.assertEqual(t2.right, t3)
        self.assertEqual(t3.parent, t2)
        self.assertEqual(t1.right, t4)
        self.assertIsNone(t4.left)
        self.assertIsNone(t4.right)

        # The tree should be :
        #             25
        #             /\
        #         12     40
        #         /\
        #     None  18
        #

        print('-- Testing search -- ')
        (b, found_node) = t1.search(18)
        assert b and found_node.key == 18, 'test 8 failed'
        (b, found_node) = t1.search(25)
        assert b and found_node.key == 25, 'test 9 failed -- you should find the node with key 25 which is the root'
        (b, found_node) = t1.search(26)
        assert (not b), 'test 10 failed'
        self.assertEqual(found_node.key, 40)
        print('-- Testing insert -- ')
        ins_node = t1.insert(26)
        self.assertEqual(ins_node.key, 26)
        self.assertEqual(ins_node.parent, t4)
        self.assertEqual(t4.left, ins_node)

        ins_node2 = t1.insert(33)
        self.assertEqual(ins_node2.key, 33)
        self.assertEqual(ins_node2.parent, ins_node)
        self.assertEqual(ins_node.right, ins_node2)

        print('-- Testing height -- ')

        self.assertEqual(t1.height(), 4)
        self.assertEqual(t4.height(), 3)
        self.assertEqual(t2.height(), 2)

        print('Success: 15 points.')

    def test_best_delete(self):
        # Testing deletion
        t1 = Node(16, None)
        # insert the nodes in the list
        lst = [18, 25, 10, 14, 8, 22, 17, 12]
        for elt in lst:
            t1.insert(elt)

        # The tree should look like this
        #               16
        #            /     \
        #          10      18
        #        /  \     /  \
        #       8   14   17  25
        #          /         /
        #         12        22

        # Let us test the three deletion cases.
        # case 1 let's delete node 8
        # node 8 does not have left or right children.
        t1.delete(8)  # should have both children nil.
        (b8, n8) = t1.search(8)
        self.assertFalse(b8)
        (b, n) = t1.search(10)
        self.assertTrue(b)
        self.assertIsNone(n.left)

        # Let us test deleting the node 14 whose right child is none.
        # n is still pointing to the node 10 after deleting 8.
        # let us ensure that it's right child is 14
        self.assertIsNotNone(n.right)
        self.assertEqual(n.right.key, 14)

        # Let's delete node 14
        t1.delete(14)
        (b14, n14) = t1.search(14)
        self.assertFalse(b14)
        (b, n) = t1.search(10)
        self.assertIsNotNone(n.right)
        self.assertEqual(n.right.key, 12)

        # Let's delete node 18 in the tree.
        # It should be replaced by 22.

        t1.delete(18)
        (b18, n18) = t1.search(18)
        self.assertFalse(b18)
        self.assertEqual(t1.right.key, 22)
        self.assertIsNone(t1.right.right.left)

        print('-- All tests passed: 15 points!--')

    def test_2(self):
        import random

        # 1. make list of  numbers from 0 to n-1
        # 2. randomly shuffle the list
        # 3. insert the random list elements in order into a tree.
        # 4. return the height of the resulting ree.
        def run_single_experiment(n):
            # your code here
            lst = [item for item in range(0, n)]
            random.shuffle(lst)
            t1 = Node(lst[0], None)
            # insert the nodes in the list
            for i in range(1, len(lst)):
                t1.insert(lst[i])
            return t1.height()

        def run_multiple_trials(n, numTrials):
            lst_of_depths = [run_single_experiment(n) for j in range(numTrials)]
            return (sum(lst_of_depths) / len(lst_of_depths), lst_of_depths)

        from matplotlib import pyplot as plt
        import math

        (avg64, lst_of_results_64) = run_multiple_trials(64, 1000)
        plt.hist(lst_of_results_64)
        plt.xlim(0, 64)
        plt.xlabel('Depth of Tree')
        plt.ylabel('Frequency')
        plt.title('Histogram of depths for n = 64')
        print(f'Average depth for 64 = {avg64}')
        self.assertGreaterEqual(12, avg64)
        self.assertGreaterEqual(avg64, 8)

        plt.figure()
        (avg128, lst_of_results_128) = run_multiple_trials(128, 1000)
        print(f'Average depth for 128 = {avg128}')
        self.assertGreaterEqual(16, avg128)
        self.assertGreaterEqual(avg128, 12)

        plt.hist(lst_of_results_128)
        plt.xlim(0, 128)
        plt.xlabel('Depth of Tree')
        plt.ylabel('Frequency')
        plt.title('Histogram of depths for n = 128')

        nmin = 16
        nmax = 64

        lst_of_average_depths = [run_multiple_trials(j, 1000)[0] for j in range(nmin, nmax)]
        plt.figure()
        l1 = plt.plot(range(nmin, nmax), lst_of_average_depths, label='Avg. Depth')
        plt.xlabel('n')
        plt.ylabel('depth')
        l2 = plt.plot(range(nmin, nmax), [1.6 * math.log(j) / math.log(2) for j in range(nmin, nmax)], '--r',
                      label='1.6log2(n)')
        l3 = plt.plot(range(nmin, nmax), [2.2 * math.log(j) / math.log(2) for j in range(nmin, nmax)], '--b',
                      label='2.2log2(n)')
        # plt.legend(handles=[l1, l2, l3])
        plt.title('Average depth as a function of n and comparison with 1.6 log2(n), 2.2 log2(n)')
        print('Passed all tests -- 15 points')


if __name__ == '__main__':
    unittest.main()
