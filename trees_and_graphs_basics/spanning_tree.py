class DisjointForests:
    def __init__(self, n):
        assert n >= 1, ' Empty disjoint forest is disallowed'
        self.n = n
        self.parents = [None] * n
        self.rank = [None] * n

    # Function: dictionary_of_sets
    # Convert the disjoint forest structure into a dictionary d
    # wherein d has an entry for each representative i
    # d[i] maps to each elements which belongs to the tree corresponding to i
    # in the disjoint forest.
    def dictionary_of_sets(self):
        d = {}
        for i in range(self.n):
            if self.is_representative(i):
                d[i] = {i}
        for j in range(self.n):
            if self.parents[j] is not None:
                root = self.find(j)
                assert root in d
                d[root].add(j)
        return d

    def make_set(self, j):
        assert 0 <= j < self.n
        assert self.parents[j] is None, 'You are calling make_set on an element multiple times -- not allowed.'
        self.parents[j] = j
        self.rank[j] = 1

    def is_representative(self, j):
        return self.parents[j] == j

    def get_rank(self, j):
        return self.rank[j]

    # Function: find
    # Implement the find algorithm for a node j in the set.
    # Repeatedly traverse the parent pointer until we reach a root.
    # Implement the "rank compression" strategy by making all
    # nodes along path from j to the root point directly to the root.
    def find(self, j):
        assert 0 <= j < self.n
        assert \
        self.parents[j] is not None, 'You are calling find on an element that is not part of the family yet. Please call make_set first.'
        # your code here

    # Function : union
    # Compute union of j1 and j2
    # First do a find to get to the representatives of j1 and j2.
    # If they are not the same, then
    #  implement union using the rank strategy I.e, lower rank root becomes
    #  child of the higher ranked root.
    #  break ties by making the first argument j1's root the parent.
    def union(self, j1, j2):
        assert 0 <= j1 < self.n
        assert 0 <= j2 < self.n
        assert self.parents[j1] is not None
        assert self.parents[j2] is not None
        # your code here


class UndirectedGraph:

    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1
    # We simply store the edges in a list.
    def __init__(self, n):
        assert n >= 1, 'You are creating an empty graph -- disallowed'
        self.n = n
        self.edges = []
        self.vertex_data = [None] * self.n

    def set_vertex_data(self, j, dat):
        assert 0 <= j < self.n
        self.vertex_data[j] = dat

    def get_vertex_data(self, j):
        assert 0 <= j < self.n
        return self.vertex_data[j]

    def add_edge(self, i, j, wij):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j with weight wij
        self.edges.append((i, j, wij))

    def sort_edges(self):
        # sort edges in ascending order of weights.
        self.edges = sorted(self.edges, key=lambda edg_data: edg_data[2])


def compute_scc(g, W):
    # create a disjoint forest with as many elements as number of vertices
    # Next compute the strongly connected components using the disjoint forest data structure
    d = DisjointForests(g.n)
    # your code here

    # extract a set of sets from d
    return d.dictionary_of_sets()


def compute_mst(g):
    # return a tuple of two items
    #   1. list of edges (i,j) that are part of the MST
    #   2. sum of MST edge weights.
    d = DisjointForests(g.n)
    mst_edges = []
    g.sort_edges()
    # your code here


