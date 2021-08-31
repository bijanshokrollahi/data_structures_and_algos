import unittest
from ..graphs import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # create the graph from problem 1A.
        g = UndirectedGraph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 4)

        # Test DFS visit
        discovery_times = [None] * 5
        finish_times = [None] * 5
        dfs_tree_parents = [None] * 5
        dfs_back_edges = []
        g.dfs_visit(0, DFSTimeCounter(), discovery_times, finish_times, dfs_tree_parents, dfs_back_edges)

        print('DFS visit discovery and finish times given by your code.')
        print('Node\t Discovery\t Finish')
        for i in range(5):
            print(f'{i} \t {discovery_times[i]}\t\t {finish_times[i]}')

        self.assertEqual(discovery_times[0], 0)
        self.assertEqual(discovery_times[1], 1)
        self.assertEqual(finish_times[1], 2)
        self.assertEqual(discovery_times[2], 3)

        self.assertEqual(finish_times[2], 8)
        self.assertEqual(discovery_times[3], 4)
        self.assertEqual(finish_times[3], 7)
        self.assertEqual(discovery_times[4], 5)
        self.assertEqual(finish_times[4], 6)

        print('Success -- discovery and finish times seem correct.')
        print()

        print('Node\t DFS-Tree-Parent')
        for i in range(5):
            print(f'{i} \t {dfs_tree_parents[i]}')

        self.assertIsNone(dfs_tree_parents[0])
        self.assertEqual(dfs_tree_parents[1], 0)
        self.assertEqual(dfs_tree_parents[2], 0)
        self.assertEqual(dfs_tree_parents[3], 2)
        self.assertEqual(dfs_tree_parents[4], 3)

        print('Success-- DFS parents are set correctly.')

        print()
        # Filter out all trivial back eddges (i,j)  where j is simply the parent of i.
        # such back edges occur because we are treating an undirected edge as two directed edges
        # in either direction.
        non_trivial_back_edges = [(i, j) for (i, j) in dfs_back_edges if dfs_tree_parents[i] != j]
        print('Back edges are')
        for (i, j) in non_trivial_back_edges:
            print(f'{(i, j)}')

        self.assertEqual(len(non_trivial_back_edges), 2)
        self.assertIn((4, 2), non_trivial_back_edges)
        self.assertIn((4, 0), non_trivial_back_edges)

        print('Success -- 15 points!')

    def test_2(self):
        # create the graph from problem 1A.
        g = UndirectedGraph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 4)

        self.assertEqual(num_connected_components(g), 1)

        g2 = UndirectedGraph(7)
        g2.add_edge(0, 1)
        g2.add_edge(0, 2)
        g2.add_edge(0, 4)
        g2.add_edge(2, 3)
        g2.add_edge(2, 4)
        g2.add_edge(3, 4)
        g2.add_edge(5, 6)

        self.assertEqual(num_connected_components(g2), 2)

        g3 = UndirectedGraph(8)
        g3.add_edge(0, 1)
        g3.add_edge(0, 2)
        g3.add_edge(0, 4)
        g3.add_edge(2, 3)
        g3.add_edge(2, 4)
        g3.add_edge(3, 4)
        g3.add_edge(5, 6)

        self.assertEqual(num_connected_components(g3), 3)

        g3.add_edge(7, 5)
        self.assertEqual(num_connected_components(g3), 2)

    def test_3(self):
        # this is the example that we had for the problem.
        g3 = UndirectedGraph(8)
        g3.add_edge(0, 1)
        g3.add_edge(0, 2)
        g3.add_edge(0, 4)
        g3.add_edge(2, 3)
        g3.add_edge(2, 4)
        g3.add_edge(3, 4)
        g3.add_edge(5, 6)
        g3.add_edge(5, 7)

        s = find_all_nodes_in_cycle(g3)
        print(f'Your code returns set of nodes: {s}')
        self.assertEqual(s, {0, 2, 3, 4})

        # let's also add the edge 6,7
        g3.add_edge(6, 7)
        s1 = find_all_nodes_in_cycle(g3)
        print(f'Your code returns set of nodes: {s1}')
        self.assertEqual(s1, {0, 2, 3, 4, 5, 6, 7})

        print('All tests passedd: 10 points!')


if __name__ == '__main__':
    unittest.main()
