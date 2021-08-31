import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError('item is out of bounds')
        return self.A[item]

    def append(self, item):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = item
        self.n += 1

    def _resize(self, new_size):
        B = self.make_array(new_size)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_size

    @staticmethod
    def make_array(new_size):
        return (new_size * ctypes.py_object)()
