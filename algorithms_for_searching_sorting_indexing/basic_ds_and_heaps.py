# First let us complete a minheap data structure.
# Please complete missing parts below.

class MinHeap:
    def __init__(self):
        self.H = [None]

    def size(self):
        return len(self.H) - 1

    def __repr__(self):
        return str(self.H[1:])

    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[
                i // 2], f'Min heap property fails at position {i // 2}, parent elt: {self.H[i // 2]}, child elt: {self.H[i]}'

    def min_element(self):
        return self.H[1]

    ## bubble_up function at index
    ## WARNING: this function has been cut and paste for the next problem as well
    def bubble_up(self, index):
        assert index >= 1
        if index == 1:
            return
        parent_index = index // 2
        if self.H[parent_index] < self.H[index]:
            return
        else:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)

    ## bubble_down function at index
    ## WARNING: this function has been cut and paste for the next problem as well
    def bubble_down(self, index):
        assert 1 <= index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        # set up the value of left child to the element at that index if valid, or else make it +Infinity
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else float('inf')
        # set up the value of right child to the element at that index if valid, or else make it +Infinity
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else float('inf')
        # If the value at the index is lessthan or equal to the minimum of two children, then nothing else to do
        if self.H[index] <= min(lchild_value, rchild_value):
            return
            # Otherwise, find the index and value of the smaller of the two children.
        # A useful python trick is to compare
        min_child_value, min_child_index = min((lchild_value, lchild_index), (rchild_value, rchild_index))
        # Swap the current index with the least of its two children
        self.H[index], self.H[min_child_index] = self.H[min_child_index], self.H[index]
        # Bubble down on the minimum child index
        self.bubble_down(min_child_index)

    # Function: heap_insert
    # Insert elt into heap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here
        self.H.append(elt)
        self.bubble_up(self.size())

    # Function: heap_delete_min
    # delete the smallest element in the heap. Use bubble_up/bubble_down
    def delete_min(self):
        # your code here
        self.H[1] = self.H[self.size()]
        self.H.pop()
        if self.size() <= 1:
            return
        else:
            self.bubble_down(1)


class TopKHeap:

    # The constructor of the class to initialize an empty data structure
    def __init__(self, k):
        self.k = k
        self.A = []
        self.H = MinHeap()

    def size(self):
        return len(self.A) + (self.H.size())

    def get_jth_element(self, j):
        assert 0 <= j < self.k - 1
        assert j < self.size()
        return self.A[j]

    def satisfies_assertions(self):
        # is self.A sorted
        for i in range(len(self.A) - 1):
            assert self.A[i] <= self.A[i + 1], f'Array A fails to be sorted at position {i}, {self.A[i], self.A[i + 1]}'
        # is self.H a heap (check min-heap property)
        self.H.satisfies_assertions()
        # is every element of self.A less than or equal to each element of self.H
        for i in range(len(self.A)):
            assert self.A[
                       i] <= self.H.min_element(), f'Array element A[{i}] = {self.A[i]} is larger than min heap element {self.H.min_element()}'

    # Function : insert_into_A
    # This is a helper function that inserts an element `elt` into `self.A`.
    # whenever size is < k,
    #       append elt to the end of the array A
    # Move the element that you just added at the very end of
    # array A out into its proper place so that the array A is sorted.
    # return the "displaced last element" jHat (None if no element was displaced)
    def insert_into_A(self, elt):
        print("k = ", self.k)
        assert (self.size() < self.k)
        self.A.append(elt)
        j = len(self.A) - 1
        while (j >= 1 and self.A[j] < self.A[j - 1]):
            # Swap A[j] and A[j-1]
            (self.A[j], self.A[j - 1]) = (self.A[j - 1], self.A[j])
            j = j - 1
        return

    # Function: insert -- insert an element into the data structure.
    # Code to handle when self.size < self.k is already provided
    def insert(self, elt):
        size = self.size()
        # If we have fewer than k elements, handle that in a special manner
        if size <= self.k:
            self.insert_into_A(elt)
            return
            # Code up your algorithm here.
        # your code here
        else:
            #needs to get put in A
            if elt < self.A[len(self.A)-1]:
                self.A.append(elt)
                self.A.sort()
                to_be_added_to_h = self.A.pop()
                self.H.insert(to_be_added_to_h)
            else:
                self.H.insert(elt)

    # Function: Delete top k -- delete an element from the array A
    # In particular delete the j^{th} element where j = 0 means the least element.
    # j must be in range 0 to self.k-1
    def delete_top_k(self, j):
        k = self.k
        assert self.size() > k  # we need not handle the case when size is less than or equal to k
        assert j >= 0
        assert j < self.k
        # your code here
        del self.A[j]
        self.A.append(self.H.min_element())
        self.A.sort()
        self.H.delete_min()


class MaxHeap:
    def __init__(self):
        self.H = [None]

    def size(self):
        return len(self.H) - 1

    def __repr__(self):
        return str(self.H[1:])

    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] <= self.H[
                i // 2], f'Maxheap property fails at position {i // 2}, parent elt: {self.H[i // 2]}, child elt: {self.H[i]}'

    def max_element(self):
        return self.H[1]

    def bubble_up(self, index):
        assert index >= 1
        if index == 1:
            return
        parent_index = index // 2
        if self.H[parent_index] > self.H[index]:
            return
        else:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)

    def bubble_down(self, index):
        # your code here
        assert 1 <= index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        # set up the value of left child to the element at that index if valid, or else make it +Infinity
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else float('-inf')
        # set up the value of right child to the element at that index if valid, or else make it +Infinity
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else float('-inf')
        # If the value at the index is lessthan or equal to the minimum of two children, then nothing else to do
        if self.H[index] >= max(lchild_value, rchild_value):
            return
            # Otherwise, find the index and value of the smaller of the two children.
        # A useful python trick is to compare
        min_child_value, min_child_index = max((lchild_value, lchild_index), (rchild_value, rchild_index))
        # Swap the current index with the least of its two children
        self.H[index], self.H[min_child_index] = self.H[min_child_index], self.H[index]
        # Bubble down on the minimum child index
        self.bubble_down(min_child_index)

    # Function: insert
    # Insert elt into minheap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here
        self.H.append(elt)
        self.bubble_up(self.size())

    # Function: delete_max
    # delete the largest element in the heap. Use bubble_up/bubble_down
    def delete_max(self):
        # your code here
        self.H[1] = self.H[self.size()]
        self.H.pop()
        if self.size() <= 1:
            return
        else:
            self.bubble_down(1)


class MedianMaintainingHeap:
    def __init__(self):
        self.hmin = MinHeap()
        self.hmax = MaxHeap()

    def satisfies_assertions(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0
            return
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            return
            # 1. min heap min element >= max heap max element
        assert self.hmax.max_element() <= self.hmin.min_element(), f'Failed: Max element of max heap = {self.hmax.max_element()} > min element of min heap {self.hmin.min_element()}'
        # 2. size of max heap must be equal or one lessthan min heap.
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        assert (
                    s_min == s_max or s_max == s_min - 1), f'Heap sizes are unbalanced. Min heap size = {s_min} and Maxheap size = {s_max}'

    def __repr__(self):
        return 'Maxheap:' + str(self.hmax) + ' Minheap:' + str(self.hmin)

    def get_median(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, 'Sizes are not balanced'
            assert False, 'Cannot ask for median from empty heaps'
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, 'Sizes are not balanced'
            return self.hmin.min_element()
        # your code here
        if self.hmin.size() > self.hmax.size():
            return self.hmin.min_element()
        elif self.hmin.size() < self.hmax.size():
            return self.hmax.max_element()
        else:
            return (self.hmin.min_element() + self.hmax.max_element()) / 2
    # function: balance_heap_sizes
    # ensure that the size of hmax == size of hmin or size of hmax +1 == size of hmin
    # If the condition above does not hold, move the max element from max heap into the min heap or
    # vice versa as needed to balance the sizes.
    # This function could be called from insert/delete_median methods

    def balance_heap_sizes(self):
        # your code here
        if abs(self.hmax.size() - self.hmin.size()) <= 1:
            return
        else:
            if self.hmax.size() > self.hmin.size():
                self.hmin.insert(self.hmax.max_element())
                self.hmax.delete_max()
                self.balance_heap_sizes()
            else:
                self.hmax.insert(self.hmin.min_element())
                self.hmin.delete_min()
                self.balance_heap_sizes()

    def insert(self, elt):
        # Handle the case when either heap is empty
        if self.hmin.size() == 0:
            # min heap is empty -- directly insert into min heap
            self.hmin.insert(elt)
            return
        if self.hmax.size() == 0:
            # max heap is empty -- this better happen only if min heap has size 1.
            assert self.hmin.size() == 1
            if elt > self.hmin.min_element():
                # Element needs to go into the min heap
                current_min = self.hmin.min_element()
                self.hmin.delete_min()
                self.hmin.insert(elt)
                self.hmax.insert(current_min)
                # done!
            else:
                # Element goes into the max heap -- just insert it there.
                self.hmax.insert(elt)
            return
            # Now assume both heaps are non-empty
        # your code here
        self.hmin.insert(elt)
        self.balance_heap_sizes()

    def delete_median(self):
        self.hmax.delete_max()
        self.balance_heap_sizes()
