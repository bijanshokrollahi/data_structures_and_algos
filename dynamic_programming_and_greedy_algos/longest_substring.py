"""
copyright bijan shokrollahi
10.27.2021

"""


# Program the recurrence for longest stable subsequence
# 0 <= i <= len(a)
# Note that if j == -1, then take aj = None
# else aj = a[j]
def lssLength(a, i, j):
    aj = a[j] if 0 <= j < len(a) else None
    # Implement the recurrence below. Use recursive calls back to lssLength
    assert 0 <= i <= len(a)
    if i >= len(a) or j >= len(a):
        return 0
    if aj and abs(a[i] - a[j]) > 1:
        return lssLength(a, i + 1, j)
    if aj is None or (abs(a[i] - a[j]) <= 1 and i != j):
        return max(lssLength(a, i + 1, j), lssLength(a, i + 1, i) + 1)
    else:
        return lssLength(a, i + 1, j)


# def lssLength(a, i, j):
#     T = {}
#     n = len(a)
#     for i in range(0, n + 1):
#         for j in range(-1, n + 1):
#             T[(i, j)] = 0
#
#     for i in range(n - 1, -1, -1):
#         for j in range(n - 1, -1, -1):
#             aj = a[j] if 0 <= j < len(a) else None
#             if aj is not None and abs(a[i] - a[j]) > 1:
#                 T[(i, j)] = T[(i + 1, j)]
#
#             elif aj is None or abs(a[i] - a[j]) <= 1:
#                 T[(i, j)] = max(T[(i + 1, i)] + 1, T[(i + 1, j)])
#     for i in range(n - 2, -1, -1):
#         T[(i, -1)] = max(T[(i + 1, -1)], T[(i + 1, 0)], T[(i, 0)], 0)
#
#     return T


def memoizeLSS(a):
    T = {}  # Initialize the memo table to empty dictionary
    # Now populate the entries for the base case
    n = len(a)
    for i in range(0, n + 1):
        for j in range(-1, n + 1):
            T[(i, j)] = 0
    # i = n and j
    # Now fill out the table : figure out the two nested for loops
    # It is important to also figure out the order in which you iterate the indices i and j
    # Use the recurrence structure itself as a guide: see for instance that T[(i,j)] will depend on T[(i+1, j)]
    # your code here
    # for j in range(n-1, -2, -1):
    #     for i in range(n-1, -1, -1):
    #         aj = a[j] if 0 <= j < len(a) else None
    #         if i < 0 or j < 0:
    #             T[(i, j)] = 0
    #         if aj and abs(a[i] - a[j]) > 1:
    #             T[(i, j)] = T[(i+1, j)]
    #         if aj is None or (abs(a[i] - a[j]) <= 1 and i != j):
    #             T[(i, j)] = T[(i+1, j)] + 1
    #         else:
    #             T[(i, j)] = T[(i+1, j)]
    # return T
    # for i in range(n - 1, -1, -1):
    #     for j in range(n - 1, -1, -1):
    #         if abs(a[i] - a[j]) > 1:
    #             try:
    #                 T[(i, j)] = max(0, T[(i, j + 1)], T[(i + 1, j)])
    #             except Exception:
    #                 T[(i, j)] = 0
    #         elif abs(a[i] - a[j]) <= 1 and i != j:
    #             if T[(i + 1, j + 1)] == 0:
    #                 T[(i, j)] = 2
    #             else:
    #                 T[(i, j)] = T[(i + 1, j + 1)] + 1
    #         else:
    #             T[(i, j)] = max(0, T[(i + 1, j + 1)])
    # for i in range(n - 2, -1, -1):
    #     T[(i, -1)] = max(T[(i + 1, -1)], T[(i + 1, 0)], T[(i, 0)], 0)
    # return T
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            aj = a[j] if 0 <= j < len(a) else None
            if aj is not None and abs(a[i] - a[j]) > 1:
                T[(i, j)] = T[(i + 1, j)]

            elif aj is None or abs(a[i] - a[j]) <= 1:
                T[(i, j)] = max(T[(i + 1, i)] + 1, T[(i + 1, j)])
    for i in range(n - 2, -1, -1):
        T[(i, -1)] = max(T[(i + 1, -1)], T[(i + 1, 0)], T[(i, 0)], 0)

    return T


def checkMemoTableHasEntries(a, T):
    for i in range(len(a) + 1):
        for j in range(i):
            assert (i, j) in T, f'entry for {(i, j)} not in memo table'


def checkMemoTableBaseCase(a, T):
    n = len(a)
    for j in range(-1, n):
        assert T[(n, j)] == 0, f'entry for {(n, j)} is not zero as expected'
