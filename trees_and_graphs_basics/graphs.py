# This is a useful data structure for implementing
# a counter that counts the time.
class DFSTimeCounter:
    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1

    def get(self):
        return self.count


class UndirectedGraph:

    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1
    # Initialize to an empty adjacency list
    # We will store the outgoing edges using a set data structure
    def __init__(self, n):
        self.n = n
        self.adj_list = [set() for i in range(self.n)]

    def add_edge(self, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j
        self.adj_list[i].add(j)
        # Also add edge from j to i
        self.adj_list[j].add(i)

    # get a set of all vertices that
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, i):
        assert 0 <= i < self.n
        return self.adj_list[i]

    # Function: dfs_visit
    # Program a DFS visit of a graph.
    # We maintain a list of discovery times and finish times.
    # Initially all discovery times and finish times are set to None.
    # When a vertex is first visited, we will set discovery time
    # When DFS visit has processed all the neighbors then
    # set the finish time.
    # DFS visit should update the list of discovery and finish times in-place
    # Arguments
    #  i --> id of the vertex being visited.
    #  dfs_timer --> An instance of DFSTimeCounter structure provided for you.
    #  discovery --> discovery time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be visited.
    #  finish --> finish time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be finished.
    #  dfs_tree_parent --> the parent for for each node
    #                       if we visited node j from node i, then j's parent is i.
    #                      Do not forget to set tree_parent when you call dfs_visit
    #                                                         on node j from node i.
    #  dfs_back_edges --> a list of back edges.
    #                     a back edge is an edge from i to j wherein
    #                     DFS has already discovered j when i is discovered
    #                                     but not finished j

    def dfs_visit(self, i, dfs_timer, discovery_times, finish_times,
                  dfs_tree_parent, dfs_back_edges):
        assert 0 <= i < self.n
        assert discovery_times[i] is None
        assert finish_times[i] is None
        discovery_times[i] = dfs_timer.get()
        dfs_timer.increment()
        for v in self.get_neighboring_vertices(i):
            if discovery_times[v] is not None and finish_times[v] is None:
                dfs_back_edges.append((i, v))
            if discovery_times[v] is None:
                dfs_tree_parent[v] = i
                self.dfs_visit(v, dfs_timer, discovery_times, finish_times,
                               dfs_tree_parent, dfs_back_edges)
        finish_times[i] = dfs_timer.get()
        dfs_timer.increment()

    # Function: dfs_traverse_graph
    # Traverse the entire graph.
    def dfs_traverse_graph(self):
        dfs_timer = DFSTimeCounter()
        discovery_times = [None] * self.n
        finish_times = [None] * self.n
        dfs_tree_parents = [None] * self.n
        dfs_back_edges = []
        for i in range(self.n):
            if discovery_times[i] is None:
                self.dfs_visit(i, dfs_timer, discovery_times, finish_times,
                               dfs_tree_parents, dfs_back_edges)
        # Clean up the back edges so that if (i,j) is a back edge then j cannot
        # be i's parent.
        non_trivial_back_edges = [(i, j) for (i, j) in dfs_back_edges if dfs_tree_parents[i] != j]
        return dfs_tree_parents, non_trivial_back_edges, discovery_times, finish_times


def num_connected_components(g):  # g is an UndirectedGraph class
    # your code here
    mscc = get_mscc(g)
    return len(mscc)


def dfs_for_transposed_nodes(transposed_g, g_ordered_stack):
    timer = DFSTimeCounter()
    discovery_times = [None] * transposed_g.n
    finish_times = [None] * transposed_g.n
    dfs_tree_parents = [None] * transposed_g.n
    dfs_back_edges = []
    dont_visit = []
    mscc = []
    for node in g_ordered_stack:
        scc = []
        if node not in dont_visit:
            transposed_g.dfs_visit(node, timer, discovery_times, finish_times,
                                   dfs_tree_parents, dfs_back_edges)
            for i in range(len(finish_times)):
                if finish_times[i] is not None and i not in dont_visit:
                    dont_visit.append(i)
                    scc.append(i)
        dont_visit.append(node)
        if scc:
            mscc.append(scc)
    non_trivial_back_edges = [(i, j) for (i, j) in dfs_back_edges if dfs_tree_parents[i] != j]
    return mscc


def transpose_g(g: UndirectedGraph) -> UndirectedGraph:
    transposed_g = UndirectedGraph(g.n)
    for node in range(len(g.adj_list)):
        for edge in g.adj_list[node]:
            transposed_g.add_edge(edge, node)
    return transposed_g


def create_stack_from_finish_times(finish_times: list) -> list:
    stack = []
    for i in range(0, len(finish_times)):
        max = 0
        location = 0
        for j in range(len(finish_times)):
            if finish_times[j] > max and j not in stack:
                max = finish_times[j]
                location = j
        stack.append(location)
    return stack


def find_all_nodes_in_cycle(g):  # g is an UndirectedGraph class
    set_of_nodes = set()
    # your code here
    mscc = get_mscc(g)
    for scc in mscc:
        for val in scc:
            set_of_nodes.add(val)
    return set_of_nodes


def get_mscc(g):
    dfs_tree_parents, non_trivial_back_edges, discovery_times, finish_times = g.dfs_traverse_graph()
    print(finish_times)
    first_stack = create_stack_from_finish_times(finish_times)
    # transpose
    transposed_g = transpose_g(g)
    # dfs of transposed
    mscc = dfs_for_transposed_nodes(transposed_g, first_stack)
    return mscc



