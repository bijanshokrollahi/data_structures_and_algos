"""

copyright bijan shokrollahi
02.05.2022

"""
import random
TIME = 1


class InsertionSort:
    def __init__(self, arr: list):
        self.arr: list = arr

    def insertion_sort(self) -> None:
        if len(self.arr) < 2:
            return None
        for i in range(1, len(self.arr)):
            j = i
            while self.arr[j] < self.arr[j - 1] and j > 0:
                self.swap(j, j - 1)
                j -= 1

    def swap(self, i: int, j: int) -> None:
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def get_arr(self):
        return self.arr


class BinarySearch:
    def __init__(self, arr: list):
        self.arr: list = arr

    def binary_search(self, val) -> int:
        left = 0
        right = len(self.arr)
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == val:
                return mid
            if self.arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return -99


class MergeSort:
    def __init__(self, arr: list):
        self.arr: list = arr

    def merge_sort(self):
        self.merge_sort_helper(0, len(self.arr) - 1)

    def merge_sort_helper(self, left, right):
        if left >= right:
            return None
        if left + 1 == right:
            if self.arr[left] > self.arr[right]:
                # swap
                self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            return None
        else:
            mid = (left + right) // 2
            self.merge_sort_helper(left, mid)
            self.merge_sort_helper(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        i = left
        j = mid + 1
        tmp = []
        while i <= mid and j <= right:
            if self.arr[i] < self.arr[j]:
                tmp.append(self.arr[i])
                i += 1
            else:
                tmp.append(self.arr[j])
                j += 1
        while i <= mid:
            # copy rest of i to mid
            tmp.append(self.arr[i])
            i += 1
        while j <= right:
            # copy rest of j to right
            tmp.append(self.arr[j])
            j += 1
        tmp_index = 0
        for index in range(left, right + 1):
            self.arr[index] = tmp[tmp_index]
            tmp_index += 1

    def get_arr(self):
        return self.arr


class MergeInsertionSort:
    def __init__(self, arr: list):
        self.arr = arr

    def merge_insertion_sort(self) -> None:
        self.merge_insertion_sort_helper(0, len(self.arr) - 1)

    def merge_insertion_sort_helper(self, left, right):
        if left >= right:
            return None
        if left + 1 == right:
            if self.arr[left] > self.arr[right]:
                self.arr[right], self.arr[left] = self.arr[left], self.arr[right]
            return None
        else:
            mid = (left + right) // 2
            self.merge_insertion_sort_helper(left, mid)
            self.merge_insertion_sort_helper(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right) -> None:
        for i in range(mid, right + 1):
            curr_location = i
            while curr_location > left and self.arr[curr_location] < self.arr[curr_location - 1]:
                self.arr[curr_location], self.arr[curr_location - 1] = self.arr[curr_location - 1], self.arr[
                    curr_location]
                curr_location -= 1

    def get_arr(self) -> list:
        return self.arr


class HeapDS:
    def __init__(self, keys: list):
        self.keys = [0]
        self.keys += keys

    def __len__(self):
        if len(self.keys) == 0:
            return 0
        return len(self.keys) - 1

    def get_heap(self):
        return self.keys[1:]

    def get_min_element(self):
        return self.keys[1]

    def bubble_up(self, index) -> None:
        """
        swap current node value with parent
        only done if current node <= parent
        :return: None
        """
        assert index <= len(self)
        if index <= 1:
            return
        elif self.keys[index] < self.keys[index // 2]:
            self.keys[index], self.keys[index // 2] = self.keys[index // 2], self.keys[index]
            self.bubble_up(index // 2)
        return

    def bubble_down(self, index) -> None:
        """
        swap current node value with child
        only done if child <= current node
        :param index:
        :return:
        """
        # check to see if index has no children
        # else check to see if children are smaller than index
        # find smaller child
        # swap index with smaller child
        # call bubble down on new index
        # return None
        length = len(self)
        left = 2 * index
        right = left + 1
        if left > length:
            return
        if left <= length < right:
            if self.keys[index] > self.keys[left]:
                self.keys[index], self.keys[left] = self.keys[left], self.keys[index]
                self.bubble_down(left)
        else:
            small = right
            if self.keys[left] < self.keys[right]:
                small = left
            if self.keys[index] > self.keys[small]:
                self.keys[index], self.keys[small] = self.keys[small], self.keys[index]
                self.bubble_down(small)
        return

    def heapify(self):
        # start from end of self.keys down to 1 and bubble down
        for i in range(len(self) // 2, 0, -1):
            self.bubble_down(i)

    def insert(self, key):
        self.keys.append(key)
        self.bubble_up(len(self))

    def delete(self, key):
        return

    def delete_index(self, index):
        # replace self.keys[index] with self.keys[len(self)]
        # self.keys = self.keys[:-1]
        # bubble down index
        #
        self.keys[index] = self.keys[len(self)]
        self.keys = self.keys[:-1]
        if self.keys[index] < self.keys[index // 2]:
            self.bubble_up(index)
        else:
            self.bubble_down(index)

    def minimum(self):
        return


class ListItem:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    def __init__(self, size_of_arr: int = 16):
        self.arr = [None] * size_of_arr
        self.index = 0

    def __len__(self) -> int:
        return self.index

    def _size_of_arr(self) -> int:
        return len(self.arr)

    def _hash(self, val) -> int:
        return hash(val)

    def insert(self, key, val) -> None:
        if ((self.index + 1) / self._size_of_arr()) >= .75:
            self.resize_hash_table()
        self._insert(key, val, self.arr)
        self.index += 1

    @staticmethod
    def _insert(key, val, arr: list) -> None:
        hash_val = hash(key)
        mod = hash_val % len(arr)
        if arr[mod] is None:
            arr[mod] = ListItem(key, val)
        else:
            curr = ListItem(key, val)
            curr.next = arr[mod]
            arr[mod] = curr

    def get(self, key, return_if_not_found=None) -> any:
        """

        :param key: key to find value
        :param return_if_not_found: if key is not in dictionary, return return_if_not_found
        :return: will return the value of the specified key, None or return_if_not_found if defined
        """
        hash_val = self._hash(key)
        mod = hash_val % self._size_of_arr()
        if self.arr[mod] is None:
            return return_if_not_found
        else:
            curr = self.arr[mod]
            while curr.key != key:
                curr = curr.next
                if curr is None:
                    return return_if_not_found
            return curr.val

    def resize_hash_table(self) -> None:
        new_arr = [None] * (2 * self._size_of_arr())
        for i in range(0, self._size_of_arr()):
            curr = self.arr[i]
            while curr is not None:
                self._insert(curr.key, curr.val, new_arr)
                curr = curr.next
        self.arr = new_arr

    def delete(self, key) -> bool:
        """
        find the hash
        find the mod
        find the head
        if head is none return false
        else curr = head
        prev = curr
        while curr.val is not val
        prev = curr
        curr = curr.next
        prev.next = curr.next
        delete(curr)
        return True
        """
        hash_val = self._hash(key)
        mod = hash_val % self._size_of_arr()
        head = self.arr[mod]
        if head is None:
            return False
        if head.key == key:
            self.arr[mod] = head.next
            self.index -= 1
            return True
        curr = head
        prev = None
        while curr.key != key:
            prev = curr
            curr = curr.next
            if curr is None:
                return False
        prev.next = curr.next
        self.index -= 1
        return True


class QuickSort:
    def __init__(self, arr: list):
        self.arr = arr

    def sort(self):
        self._quick_sort(0, len(self.arr) - 1)

    def _quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self._quick_sort(left, pivot - 1)
            self._quick_sort(pivot + 1, right)

    def partition(self, left, right):
        x = self.arr[right]
        i = left - 1
        for j in range(left, right):
            if self.arr[j] <= x:
                i = i + 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[right] = self.arr[right], self.arr[i + 1]
        return i + 1


class QuickSelect:
    def __init__(self, arr: list):
        self.arr = arr

    def quick_select(self, kth_smallest_element: int):
        self._quick_select(kth_smallest_element, 0, len(self.arr) - 1)

    def _quick_select(self, kth_smallest_element, left, right):
        pivot = self._partition(left, right)
        if pivot == kth_smallest_element:
            return self.arr[pivot]
        if pivot > kth_smallest_element:
            return self._quick_select(kth_smallest_element, left, pivot - 1)
        return self._quick_select(kth_smallest_element, pivot + 1, right)

    def _partition(self, left: int, right: int):
        x = self.arr[right]
        i = left - 1
        for j in range(left, right + 1):
            if self.arr[j] <= x:
                i = i + 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[right] = self.arr[right], self.arr[i + 1]
        return i


class BstNodeItem:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Bst:
    def __init__(self, val):
        self.head = BstNodeItem(val)

    def find(self, val):
        return self._find(self.head, val)

    def _find(self, node, val):
        if node is None:
            return node
        else:
            if node.val == val:
                return node
            elif val < node.val:
                return self._insert_find(node.left, val)
            else:
                return self._insert_find(node.right, val)

    def _insert_find(self, node, val):
        if node is None:
            return node
        else:
            if node.val == val:
                return node
            elif val < node.val:
                if node.left is None:
                    return node
                return self._insert_find(node.left, val)
            else:
                if node.right is None:
                    return node
                return self._insert_find(node.right, val)

    @staticmethod
    def tree_minimum(node):
        while node.left is not None:
            node = node.left
        return node

    @staticmethod
    def tree_maximum(node):
        while node.right is not None:
            node = node.right
        return node

    @staticmethod
    def iterative_tree_search(node, val):
        while node is not None and val != node.val:
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return node

    def tree_search(self, node, val):
        if node is None or val == node.val:
            return node
        if val < node.val:
            return self.tree_search(node.left, val)
        else:
            return self.tree_search(node.right, val)

    """
    print_in_order_traversal(node)
    recursive
    if node is none:
        return
    print_in_order_traversal(node.left)
    print(node.val)
    print_in_order_traversal(node.right)
    
    """

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.left)
        print(node.val)
        self.in_order_traversal(node.right)

    """
    pre_order_traversal(node)
    if node is none:
        return
    print(node.val)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    """

    def pre_order_traversal(self, node):
        if node is None:
            return
        print(node.val)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

    """
    post_order_traversal(node)
    if node is none:
        return none
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.val)
    """

    def post_order_traversal(self, node):
        if node is None:
            return
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.val)

    def insert(self, val):
        node = self._insert_find(self.head, val)
        if val < node.val:
            node.left = BstNodeItem(val)
        else:
            node.right = BstNodeItem(val)

    def height(self):
        return self._height(self.head)

    def _height(self, node):
        if node is None:
            return 0
        else:
            return max(self._height(node.left), self._height(node.right)) + 1

    # def transplant(self, u, v):
    #     if u.

    def delete(self, val):
        """
         deletion cases
         case 0 both children are none
         case 1 one of the children is none
         case 2 neither children are none
             find successor which is one to the right and all the way left
             replace w/ successor then delete successor
         """
        # insert find returns the parent of the node in question
        parent = self._insert_find(self.head, val)
        if parent is None:
            return False
        node = parent.left
        if parent.right.val == val:
            node = parent.right
        # case 0 both children are none
        if node.left is None and node.right is None:
            if parent.right == node:
                parent.right = None
            else:
                parent.left = None
            del node
            return True
        # case 2 neither children are none
        if node.right is not None and node.left is not None:
            # complicated case
            return True
        # case 1 either child is none
        if node.right is not None:
            if parent.right == node:
                parent.right = node.right
            else:
                parent.left = node.right
            del node
            return True
        else:
            if parent.right == node:
                parent.right = node.left
            else:
                parent.left = node.left
            del node
            return True
        # elif node.left is not None and node.right is not None:
        #     # find successor
        #     # replace w/ successor
        # elif node.left is None:
        #     node = node.right
        # else node.right is None:
        #


"""
TREAP = TREE + HEAP
if you know the insertions ahead of time you can randomize the insertion and end up getting around Ølog(n)
add random seed value to each node. those seed values must follow heap rules. if not bubble up aka rotate left or right
"""


class RbtNode:
    def __init__(self, val, color):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """
    rbt rules
    1. roots and leaves must be black
    2. every red node must have black children
    3. the number of black nodes on any path from any node to a leaf must be the same
        black height is defined for each node
    """

    def __init__(self, val):
        self.root = RbtNode(val, 'black')

    def find(self, val):
        return self.root

    def delete(self, val):
        return self.root

    def insert(self, val):
        """
        1. newly inserted node is always colored red
        2. if lucky, the parent of new node is black and nothing needs to be done
        3. unlucky if parent is red. will cause red-red violation
        :param val:
        :return:
        """
        return self.root

    def left_rotate(self, node_x):
        node_y = node_x.right
        node_x.right = node_y.left
        if node_y.left is not None:
            node_y.left.parent = node_x
        node_y.parent = node_x.parent
        if node_x.parent is None:
            self.root = node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y
        node_y.left = node_x
        node_x.parent = node_y


"""
skip lists easier than rb tree, randomized data structure
rules
1. many layers
each layer <= layer below
bottom layer = all elements
each layer is sorted
each node has pointer to down + right
"""

"""
GRAPHS
directed graph vs undirected graph(each edge is bidirectional. symmetric relation)
different representations
adjacency matrix - inefficient becuase it has a size of n^2
adjacency list - each node in the list has a pointer to a list of its neighbors, size n + number of edges

"""


# BFS
# 1. can only visit node once
# 2. driven by queue data structure which stores the nodes
"""
node
    parent: which parent did we discover this node from
    depth: depth of the node
    seen: true/false if the node has been visited
"""


class GraphNode:
    def __init__(self, val, parent=None, depth=0, seen=False):
        self.val = val
        self.parent = parent
        self.depth = depth
        self.seen = seen
        self.neighbors: list[GraphNode] = []


def bfs(graph, node_to_start: GraphNode):
    from queue import Queue
    bfs_queue = Queue()
    bfs_queue.put(node_to_start)
    node_to_start.depth = 0
    node_to_start.seen = True
    node_to_start.parent = None
    while not bfs_queue.empty():
        node = bfs_queue.get()
        for neighbor in node.neighbors:
            if neighbor.seen is False:
                neighbor.parent = node
                neighbor.depth = node.depth + 1
                neighbor.seen = True
                bfs_queue.put(neighbor)


class DfsGraphNode:
    def __init__(self, val, parent=None, time=None, finished=None, seen=False):
        self.val = val
        self.parent = parent
        self.time = time
        self.finished = finished
        self.seen = seen
        self.neighbors: list[DfsGraphNode] = []


def dfs_visit(graph, node):
    global TIME
    if node.seen:
        return
    TIME += 1
    node.time = TIME
    for neighbor in node.neighbors:
        if neighbor.seen is False:
            neighbor.parent = node
            dfs_visit(graph, neighbor)
            neighbor.seen = True
    node.finished = TIME


"""
topological sort
do dfs when node finishes add to head of list, you end with topologically sorted graph, only for dag
"""

"""
strongly connected components
dfs on g
transpose g
dfs on transposed g in descending order of finish times (heap), remove nodes from consideration as they are visited

"""

"""
shortest path problems
single source or all pairs
bellman-ford

shortest path on dag
topological sort, then iterate through each vertex in topological order and relxax
"""


""""
dijkstra 

until all nodes are visited
choose unvisted node with smallest distance value, current_node
    relax outgoing edges of current_node
    set current_node to visited
"""


def dijkstra(vertices, edges, source_node):
    import heapq
    for vertex in vertices:
        if vertex == source_node:
            vertex.depth = 0
            vertex.parent = None
        else:
            vertex.depth = float('inf')
            vertex.parent = None

    heap = []
    # will need to override __lt__
    heapq.heapify(heap)
    while len(heap) > 0:
        curr_node = heapq.heappop(heap)
        if curr_node.visited is False:
            for neighbor in curr_node.neighbors:
                relax(neighbor)


def relax(graph, neighbor):
    """
    if the current path cost is > current cost + the wegith of the edge
        set the new cost to current cost + weight of the edge
        set the parent of the node to
    :param graph:
    :param neighbor:
    :return:
    """
    return 0


def max_subarray(array, left, right):
    if left == right:
        return 0
    elif right == left + 1:
        return max(array[right] - array[left], 0)
    else:
        middle = (left + right) // 2
        m1 = max_subarray(array, left, middle)
        m2 = max_subarray(array, middle+1, right)
        min_m1 = find_min(array, left, middle)
        max_m2 = find_max(array, middle+1, right)
        return max(m1, m2, max_m2 - min_m1)


def find_min(array, left, right):
    min_found = float('inf')
    for i in range(left, right+1):
        min_found = min(min_found, array[i])
    return min_found


def find_max(array, left, right):
    max_found = float('-inf')
    for i in range(left, right+1):
        max_found = max(max_found, array[i])
    return max_found


"""
notes:

b[i] = a[i] - i
"""
