"""
copyright bijan shokrollahi
01.14.2022

"""
import timeit
import numpy as np
from math import ceil
from itertools import takewhile


matrix_1 = [
    [1, 0, 2, 1, 1, 1, 1],
    [1, 2, 2, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 2, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 2, 1],
    [1, 0, 0, 1, 1, 1, 0]
]

matrix_2 = [
    [1, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def max_diagonal_match(matrix) -> int:
    max_len = 0
    pattern_match = [1, 2, 0, 2, 0, 2, 0]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            max_len = max(
                max_len,
                find_i_minus_j_minus(matrix, i, j, pattern_match, 7),
                find_i_minus_j_plus(matrix, i, j, pattern_match, 7),
                find_i_plus_j_minus(matrix, i, j, pattern_match, 7),
                find_i_plus_j_plus(matrix, i, j, pattern_match, 7)
            )
    return max_len


# i-, j-
def find_i_minus_j_minus(matrix, i, j, pattern, mod):
    count = 0
    while i >= 0 and j >= 0:
        if matrix[i][j] != pattern[count % mod]:
            return count
        count += 1
        i -= 1
        j -= 1
    return count


# i-, j+
def find_i_minus_j_plus(matrix, i, j, pattern, mod):
    count = 0
    while i >= 0 and j < len(matrix[i]):
        if matrix[i][j] != pattern[count % mod]:
            return count
        count += 1
        i -= 1
        j += 1
    return count


# i+, j-
def find_i_plus_j_minus(matrix, i, j, pattern, mod):
    count = 0
    while i < len(matrix) and j >= 0:
        if matrix[i][j] != pattern[count % mod]:
            return count
        count += 1
        i += 1
        j -= 1
    return count


# j+, i+
def find_i_plus_j_plus(matrix, i, j, pattern, mod):
    count = 0
    while i < len(matrix) and j < len(matrix[i]):
        if matrix[i][j] != pattern[count % mod]:
            return count
        count += 1
        i += 1
        j += 1
    return count


def max_sequence(arr):
    pattern = [1, 2, 0, 2, 0, 2, 0]
    solns = []
    i = arr.shape[0]
    for x in range(-i, i+1):
        values = arr.diagonal(x)
        N = len(values)
        possibles = np.where(values == pattern[0])[0]
        for p in possibles:
            check = values[p:p+N]
            m = len(list(takewhile(lambda x:len(set(x))==1, zip(pattern,check))))
            solns.append(m)
    return max(solns)


def find_longest(arr):
    if len(arr) > 0:
        return max([max_sequence(x) for x in [arr, np.fliplr(arr), np.flipud(arr), arr[::-1]]])
    else:
        return 0


def chris_way():
    pattern = [1, 2, 0, 2, 0, 2, 0]
    # Make sure pattern repeats longer than the max diagonal
    pattern = np.tile(pattern, ceil(matrix_2.shape[1] / len(pattern)))
    assert find_longest(matrix_2) == 12
    assert find_longest(matrix_1) == 7
    assert find_longest([]) == 0


def main():
    # print(min(timeit.Timer()
    print('hello')


if __name__ == '__main__':
    main()