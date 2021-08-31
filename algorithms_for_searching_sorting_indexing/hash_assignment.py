def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]


def tryPartition(a):
    # implementation of Lomuto partitioning algorithm
    n = len(a)
    pivot = a[n-1] # choose last element as the pivot.
    i,j = 0,0 # initialize i and j both to be 0
    for j in range(n-1): # j = 0 to n-2 (inclusive)
        # Invariant: a[0] .. a[i] are <= pivot
        #            a[i+1]...a[j-1] are > pivot
        if a[j] <= pivot:
            swap(a, i+1, j)
            i = i + 1
    swap(a, i+1, n-1) # place pivot in its correct place.
    return i+1 # return the index where we placed the pivot


def testIfPartitioned(a, k):
    # TODO : test if all elements at indices < k are all <= a[k]
    #         and all elements at indices > k are all > a[k]
    # return TRUE if the array is correctly partitioned around a[k] and return FALSE otherwise
    assert 0 <= k < len(a)
    # your code here
    k_val = a[k]
    for i in range(0, k):
        if a[i] > k_val:
            return False
    for i in range(k+1, len(a)):
        if a[i] <= k_val:
            return False
    return True


def simplePartition(a, pivot):
    if pivot < len(a):
        i = 0
        j = 1
        pivot_val = a[pivot]
        while j < len(a)-1:
            if a[j] < pivot_val:
                swap(a, i+1, j)
                i += 1
                j += 1
            else:
                j += 1
        swap(a, i+1, len(a)-1)
        simplePartition(a, pivot+1)

## To do: partition the array a according to pivot.
# Your array must be partitioned into two regions - <= pivot followed by elements > pivot
## If an element at the beginning of the array is already <= pivot in the beginning of the array, it should not
## be moved by the algorithm.
# your code here


def boundedSort(a, k):
    for j in range(1, k):
        simplePartition(a, j)


from random import random


def dot_product(lst_a, lst_b):
    and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]
    return 0 if sum(and_list) % 2 == 0 else 1


# encode a matrix as a list of lists with each row as a list.
# for instance, the example above is written as the matrix
# H = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
# encode column vectors simply as a list of elements.
# you can use the dot_product function provided to you.
def matrix_multiplication(H, lst):
    ans = []
    for a in H:
        ans.append(dot_product(a, lst))
    return ans

# your code here


# Generate a random m \times n matrix
# see the comment next to matrix_multiplication for how your matrix must be returned.
def return_random_hash_function(m, n):
    # return a random hash function wherein each entry is chosen as 1 with probability >= 1/2 and 0 with probability < 1/2
    # your code here
    ans = []
    for i in range(0, m):
        tmp = []
        for j in range(0, n):
            val = random()
            if val >= .5:
                tmp.append(1)
            else:
                tmp.append(0)
        ans.append(tmp)
    return ans



