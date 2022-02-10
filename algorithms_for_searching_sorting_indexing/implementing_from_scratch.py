"""

copyright bijan shokrollahi
02.05.2022

"""


class InsertionSort:
    def __init__(self, arr: list):
        self.arr: list = arr

    def insertion_sort(self) -> None:
        if len(self.arr) < 2:
            return None
        for i in range(1, len(self.arr)):
            j = i
            while self.arr[j] < self.arr[j-1] and j > 0:
                self.swap(j, j-1)
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
            self.merge_sort_helper(mid+1, right)
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
        for index in range(left, right+1):
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
            while curr_location > left and self.arr[curr_location] < self.arr[curr_location-1]:
                self.arr[curr_location], self.arr[curr_location-1] = self.arr[curr_location-1], self.arr[curr_location]
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
        elif self.keys[index] < self.keys[index//2]:
            self.keys[index], self.keys[index//2] = self.keys[index//2], self.keys[index]
            self.bubble_up(index//2)
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
        for i in range(len(self)//2, 0, -1):
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
        if self.keys[index] < self.keys[index//2]:
            self.bubble_up(index)
        else:
            self.bubble_down(index)

    def minimum(self):
        return
