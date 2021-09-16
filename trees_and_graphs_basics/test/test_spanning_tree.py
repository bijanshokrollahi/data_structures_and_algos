import unittest
from ..spanning_tree import *


class MyTestCase(unittest.TestCase):
    def test_disjoint_forests(self):
        d = DisjointForests(10)
        for i in range(10):
            d.make_set(i)

        for i in range(10):
            self.assertEqual(i, d.find(i))

        d.union(0, 1)
        d.union(2, 3)
        self.assertEqual(d.find(0), d.find(1))
        self.assertEqual(d.find(2), d.find(3))
        self.assertNotEqual(d.find(0), d.find(3))
        assert ((d.get_rank(0) == 2 and d.get_rank(1) == 1) or
                (d.get_rank(1) == 2 and d.get_rank(0) == 1)), 'one of the nodes 0 or 1 must have rank 2'

        assert ((d.get_rank(2) == 2 and d.get_rank(3) == 1) or
                (d.get_rank(3) == 2 and d.get_rank(2) == 1)), 'one of the nodes 2 or 3 must have rank 2'

        d.union(3, 4)
        self.assertEqual(d.find(2), d.find(4))
        d.union(5, 7)
        d.union(6, 8)
        d.union(3, 7)
        d.union(0, 6)

        self.assertEqual(d.find(6), d.find(1))
        self.assertEqual(d.find(7), d.find(4))
        print('All tests passed: 10 points.')

    def test_undirected_graph(self):
        g3 = UndirectedGraph(8)
        g3.add_edge(0, 1, 0.5)
        g3.add_edge(0, 2, 1.0)
        g3.add_edge(0, 4, 0.5)
        g3.add_edge(2, 3, 1.5)
        g3.add_edge(2, 4, 2.0)
        g3.add_edge(3, 4, 1.5)
        g3.add_edge(5, 6, 2.0)
        g3.add_edge(5, 7, 2.0)
        res = compute_scc(g3, 2.0)
        print('SCCs with threshold 2.0 computed by your code are:')
        self.assertEqual(2, len(res))
        for (k, s) in res.items():
            print(s)

        # Let us check that your code returns what we expect.
        for (k, s) in res.items():
            if k in [0, 1, 2, 3, 4]:
                self.assertEqual({0, 1, 2, 3, 4}, s)
            if k in [5, 6, 7]:
                self.assertEqual({5, 6, 7}, s)

        # Let us check that the thresholding works
        print('SCCs with threshold 1.5')
        res2 = compute_scc(g3, 1.5)  # This cutsoff edges 2,4 and 5, 6, 7
        for (k, s) in res2.items():
            print(s)
        assert len(res2) == 4, f'Expected 4 SCCs but got {len(res2)}'

        for (k, s) in res2.items():
            if k in [0, 1, 2, 3, 4]:
                self.assertEqual({0, 1, 2, 3, 4}, s)
            if k in [5]:
                self.assertEqual({5}, s)
            if k in [6]:
                self.assertEqual({6}, s)
            if k in [7]:
                self.assertEqual({7}, s)

        print('All tests passed: 10 points')

    def test_undirected_graph_mst(self):
        g3 = UndirectedGraph(8)
        g3.add_edge(0, 1, 0.5)
        g3.add_edge(0, 2, 1.0)
        g3.add_edge(0, 4, 0.5)
        g3.add_edge(2, 3, 1.5)
        g3.add_edge(2, 4, 2.0)
        g3.add_edge(3, 4, 1.5)
        g3.add_edge(5, 6, 2.0)
        g3.add_edge(5, 7, 2.0)
        g3.add_edge(3, 5, 2.0)

        (mst_edges, mst_weight) = compute_mst(g3)
        print('Your code computed MST: ')
        for (i, j, wij) in mst_edges:
            print(f'\t {(i, j)} weight {wij}')
        print(f'Total edge weight: {mst_weight}')

        assert mst_weight == 9.5, 'Optimal MST weight is expected to be 9.5'

        self.assertIn((0, 1, 0.5), mst_edges)
        self.assertIn((0, 2, 1.0), mst_edges)
        self.assertIn((0, 4, 0.5), mst_edges)
        self.assertIn((5, 6, 2.0), mst_edges)
        self.assertIn((5, 7, 2.0), mst_edges)
        self.assertIn((3, 5, 2.0), mst_edges)
        assert (2, 3, 1.5) in mst_edges or (3, 4, 1.5) in mst_edges

        print('All tests passed: 10 points!')


if __name__ == '__main__':
    unittest.main()
