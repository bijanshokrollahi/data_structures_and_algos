"""
copyright bijan shokrollahi
09/27/2021

"""

import math
from matplotlib import pyplot as plt
import cv2

def fixPixelValues(px):
    # convert the RGB values into floating point to avoid an overflow that will give me wrong answers
    return [float(px[0]), float(px[1]), float(px[2])]


# This is a useful function that given a list of (x,y) values,
# draw a series of red lines between each coordinate and next to
# show the path in the image
def drawPath(img, path, pThick=2):
    v = path[0]
    x0, y0 = v[0], v[1]
    for v in path:
        x, y = v[0], v[1]
        cv2.line(img, (x, y), (x0, y0), (255, 0, 0), pThick)
        x0, y0 = x, y


class Vertex:  # This is the outline for a vertex data structure

    def __init__(self, i, j):
        self.x = i  # The x coordinate
        self.y = j  # The y coordinate
        self.d = float('inf')  # the shortest path estimate
        self.processed = False  # Has this vertex's final shortest path distance been computed
        # this is important for Dijksatra's algorithm
        # We will track where the vertex is in the priority queue.
        self.idx_in_priority_queue = -1  # The index of this vertex in the queue
        self.pi = None  # the parent vertex in the shortest path tree.

    def reset(self):
        self.d = float('inf')
        self.processed = False  # Has this vertex's final shortest path distance been computed
        # this is important for Dijksatra's algorithm
        # We will track where the vertex is in the priority queue.
        self.idx_in_priority_queue = -1  # The index of this vertex in the queue
        self.pi = None  # the parent vertex in the shortest path tree.


# However, if you want Dijkstra efficiently, we will need a priority queue
# We will provide you with a heap data structure from course 1.
class PriorityQueue:
    # Constructor:  Implement a empty heap data structure
    def __init__(self):
        self.q = [None]  # pad it with one element

    def __iter__(self):
        return iter(self.q)

    # Function: insert
    # Insert a vertex v of type Vertex into the queue.
    # Remember to set the field `idx_in_priority_queue` and
    # keep updating it.
    def insert(self, v):
        n = len(self.q)
        self.q.append(v)
        v.idx_in_priority_queue = n
        self.bubble_up(n)
        # self.check_invariant()

    # Function: swap two elements in the priority queue.
    # Remember to swap the vertices at positions i and j
    # But also remember to update the positions of the vertices in the
    # priority queue.
    # You can use this to implement bubble_up and bubble_down
    def swap(self, i, j):
        tmp = self.q[i]
        self.q[i] = self.q[j]
        self.q[i].idx_in_priority_queue = i
        self.q[j] = tmp
        self.q[j].idx_in_priority_queue = j

    # Function: bubble_up
    # bubble up an element j
    # until min heap property is restored.
    def bubble_up(self, j):
        assert j >= 1
        assert j < len(self.q)
        if j == 1:
            return
        val = self.q[j].d
        parent_idx = j // 2
        parent_val = self.q[parent_idx].d
        if val < parent_val:
            self.swap(j, parent_idx)
            self.bubble_up(parent_idx)
        return

    # Function: bubble_down
    # Bubble down an element j until
    # min heap property is restored.
    def bubble_down(self, j):
        n = len(self.q)
        left_child_idx = 2 * j
        right_child_idx = 2 * j + 1
        if left_child_idx >= n:
            return
        if right_child_idx >= n:
            child_idx = left_child_idx
            child_d = self.q[left_child_idx].d
        else:
            (child_d, child_idx) = min((self.q[left_child_idx].d, left_child_idx),
                                       (self.q[right_child_idx].d, right_child_idx)
                                       )
        if self.q[j].d > child_d:
            self.swap(j, child_idx)
            self.bubble_down(child_idx)
        return

        # Function: get_and_delete_min

    # Find the minimum weight vertex and delete it from the heap.
    # return the deleted vertex back
    def get_and_delete_min(self):
        n = len(self.q)
        assert n > 1
        v = self.q[1]
        if n > 2:
            self.q[1] = self.q[n - 1]
            self.q[n - 1].idx_in_priority_queue = 1
            del self.q[n - 1]
            self.bubble_down(1)
        # self.check_invariant()
        return v

    # Is the heap empty?
    def is_empty(self):
        return len(self.q) == 1

    # This is a useful function since in Dijkstra
    # the weight of a vertex updates on the fly.
    # We will need to call this to update the vertex weight.
    def update_vertex_weight(self, v):
        j = v.idx_in_priority_queue
        n = len(self.q)
        assert j >= 0 and j < n
        self.bubble_down(j)
        self.bubble_up(j)
        # self.check_invariant()


class DirectedGraphFromImage:
    def __init__(self, img):
        self.img = img
        self.coords2vertex = {}  # construct a dictionary that maps coordinates [(i,j)] to corresponding vertices in graph

    def get_vertex_from_coords(self, i, j):
        if (i, j) in self.coords2vertex:  # is pixel (i,j) already there?
            return self.coords2vertex[(i, j)]  # if yes, just return the vertex corresponding
        v = Vertex(i, j)
        self.coords2vertex[(i, j)] = v
        return v

    ## Given (x,y) coordinates of two neighboring pixels, calculate the edge weight.
    # We take the squared euclidean distance between the pixel values and add 0.1
    def getEdgeWeight(self, u, v):
        img = self.img
        # get edge weight for edge between u, v
        i0, j0 = u.x, u.y
        i1, j1 = v.x, v.y
        height, width, _ = img.shape
        # First make sure that the edge is legit
        # Edges can only go from each pixel to neighboring pixel
        assert 0 <= i0 < width and 0 <= j0 < height  # pixel position valid?
        assert 0 <= i1 < width and 0 <= j1 < height  # pixel position valid?
        assert -1 <= i0 - i1 <= 1  # edge between node and neighbor?
        assert -1 <= j0 - j1 <= 1
        px1 = fixPixelValues(img[j0, i0])
        px2 = fixPixelValues(img[j1, i1])
        return 0.1 + (px1[0] - px2[0]) ** 2 + (px1[1] - px2[1]) ** 2 + (px1[2] - px2[2]) ** 2

    # Function: get_list_of_neighbors
    # Given a vertex in the graph, get its list of neighbors
    #  I.e, for given vertex `vert` return a list [(v1, w1), (v2, w2),..,(vk,wk)]
    #  Such that vert has an edge to v1 with weight w1, edge to v2 with weight w2 and ...
    #   edge to vk with weight wk
    # Note that rather than build an adjacency list up front, we simply call this function
    # to get the neighbors of a vertex.
    def get_list_of_neighbors(self, vert):
        img = self.img
        i = vert.x
        j = vert.y
        height, width, _ = img.shape
        lst = []
        if i > 0:
            # Get the adjacent vertex directly to the WEST
            # What is the weight of the edge from pixel (i,j) to (i-1,j)
            v0 = self.get_vertex_from_coords(i - 1, j)
            w0 = self.getEdgeWeight(vert, v0)
            # Append the adjacent vertex and its weight.
            lst.append((v0, w0))
        if j > 0:
            # Get the adjacent vertex directly to the SOUTH
            v1 = self.get_vertex_from_coords(i, j - 1)
            w1 = self.getEdgeWeight(vert, v1)
            # Append the adjacent vertex and its weight.
            lst.append((v1, w1))
        if i < width - 1:
            # EAST
            v2 = self.get_vertex_from_coords(i + 1, j)
            w2 = self.getEdgeWeight(vert, v2)
            lst.append((v2, w2))
        if j < height - 1:
            # NORTH
            v3 = self.get_vertex_from_coords(i, j + 1)
            w3 = self.getEdgeWeight(vert, v3)
            lst.append((v3, w3))
        return lst


# Function: computeShortestPath
# Let us implement Dijkstra's algorithm
# graph - instance of the DirectedGraphFromImage class
# source - a vertex that is the source (i,j) pixel coordinates
# dest - a vertex that is the destination (i,j) pixel coordinates
def computeShortestPath(graph, source_coordinates, dest_coordinates):
    # your code here
    priority_queue = PriorityQueue()
    source = graph.get_vertex_from_coords(source_coordinates[0], source_coordinates[1])
    source.d = 0
    priority_queue.insert(source)
    distance = 0
    path = []
    while not priority_queue.is_empty():
        u = priority_queue.get_and_delete_min()
        u.processed = True
        if u.x == dest_coordinates[0] and u.y == dest_coordinates[1]:
            distance = u.d
            break
        # for each outgoing edge from 'u' to 'v' with weight 'w'
        for v in graph.get_list_of_neighbors(u):
            if v[0].processed is False and v[0].d > u.d + v[1]:
                v[0].d = u.d + v[1]
                v[0].pi = u
                if v[0].idx_in_priority_queue == -1:
                    priority_queue.insert(v[0])
                else:
                    priority_queue.update_vertex_weight(v[0])
    # do the path
    destination = graph.get_vertex_from_coords(dest_coordinates[0], dest_coordinates[1])
    while destination is not None:
        path.append((destination.x, destination.y))
        destination = destination.pi
    return path[::-1], distance


class DummyGraphClass:
    def __init__(self, adj_list, verts):
        self.verts = verts
        self.adj_list = adj_list

    def get_vertex_from_coords(self, i, j):
        assert (i, j) in self.verts
        return self.verts[(i, j)]

    def get_list_of_neighbors(self, vert):
        coords = (vert.x, vert.y)
        if coords in self.adj_list:
            return self.adj_list[(vert.x, vert.y)]
        else:
            return []


