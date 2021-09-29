"""
copyright bijan shokrollahi
09/27/2021

"""
import unittest
from trees_and_graphs_basics.dag import *


class MyTestCase(unittest.TestCase):
    def test_dag(self):
        # Test 1
        verts = {(i, j): Vertex(i, j) for i in range(3) for j in range(3)}
        adj_list = {}

        def connect_nodes(src, dest, weight):
            v1 = src
            v2 = verts[dest]
            if v1 in adj_list:
                adj_list[v1].append((v2, weight))
            else:
                adj_list[v1] = [(v2, weight)]

        # Let's build a graph
        connect_nodes((0, 0), (0, 1), 1.0)
        connect_nodes((0, 0), (1, 0), 0.5)
        connect_nodes((1, 0), (0, 1), 0.5)
        connect_nodes((0, 1), (0, 0), 0.5)
        connect_nodes((1, 0), (1, 1), 0.5)
        connect_nodes((1, 1), (2, 2), 0.25)
        connect_nodes((1, 1), (1, 2), 0.5)
        connect_nodes((1, 1), (2, 1), 1.2)
        connect_nodes((2, 1), (2, 2), 0.25)
        connect_nodes((1, 2), (2, 2), 0.25)

        graph = DummyGraphClass(adj_list, verts)

        path, dist = computeShortestPath(graph, (0, 0), (2, 2))
        print(path)
        self.assertEqual(1.25, dist)
        self.assertEqual([(0, 0), (1, 0), (1, 1), (2, 2)], path)

        for (_, v) in verts.items():
            v.reset()

        graph2 = DummyGraphClass(adj_list, verts)
        (path2, dist2) = computeShortestPath(graph2, (0, 0), (1, 2))
        print(path2)
        self.assertEqual(1.5, dist2)
        self.assertEqual((0, 0), path2[0])
        self.assertEqual((1, 2), path2[-1])

        for (_, v) in verts.items():
            v.reset()

        connect_nodes((2, 2), (2, 1), 0.5)
        connect_nodes((2, 1), (1, 1), 1.0)
        connect_nodes((1, 1), (0, 1), 0.5)

        graph3 = DummyGraphClass(adj_list, verts)
        (path3, dist3) = computeShortestPath(graph3, (2, 2), (0, 0))
        print(path3)
        self.assertEqual(2.5, dist3)
        self.assertEqual((2, 2), path3[0])
        self.assertEqual((0, 0), path3[-1])

        print('All tests passed: 15 points!')


if __name__ == '__main__':
    unittest.main()
