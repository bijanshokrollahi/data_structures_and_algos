# Define the function findCrossoverIndex that wil
# call the helper function findCrossoverIndexHelper
def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2 why?
    # your code here
    return findCrossoverIndexHelper(x, y, 0, len(x)-1)


# First write a "helper" function with two extra parameters
# left, right that ddedscribes the search region as shown below
def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert (len(x) == len(y))
    assert (left >= 0)
    assert (left <= right - 1)
    assert (right < len(x))
    # Here is the key property we would like to maintain.
    assert(x[left] > y[left])
    assert(x[right] < y[right])

    # your code here
    if left > right:
        return None
    else:
        mid = (left + right) // 2
        # if x[i] < y[i] and x[i-1]>y[i-1]
        # return i
        if x[mid] > y[mid] and x[mid + 1] < y[mid + 1]:
            return mid
        # x[mid] < y[mid]
        # recursive x, y, mid+1, right
        elif x[mid] > y[mid]:
            return findCrossoverIndexHelper(x, y, mid + 1, right)
        # else
        # recursive x, y, left, mid-1
        else:
            return findCrossoverIndexHelper(x, y, left, mid - 1)

def integerCubeRootHelper(n, left, right):
    cube = lambda x: x * x * x # anonymous function to cube a number
    # assert(n >= 1)
    # #assert(left < right)
    # assert(left >= 0)
    # assert(right < n)
    # assert(cube(left) < n), f'{left}, {right}'
    # assert(cube(right) > n), f'{left}, {right}'
    # your code here
    if left > right:
        return None
    else:
        mid = (left + right) // 2
        if mid ** 3 <= n < (mid + 1) ** 3:
            return mid
        elif mid ** 3 > n:
            return integerCubeRootHelper(n, left, mid - 1)
        else:
            return integerCubeRootHelper(n, mid + 1, right)


# Write down the main function
def integerCubeRoot(n):
    assert( n > 0)
    if n == 1:
        return 1
    if n == 2:
        return 1
    return integerCubeRootHelper(n, 0, n-1)


def twoWayMerge(lst1, lst2):
    # Implement the two way merge algorithm on
    #          two ascending order sorted lists
    # return a fresh ascending order sorted list that
    #          merges lst1 and lst2
    # your code here
    i = 0
    j = 0
    return_list = []
    while i <= (len(lst1) - 1) and j <= (len(lst2) - 1):
        if lst1[i] < lst2[j]:
            return_list.append(lst1[i])
            i += 1
        else:
            return_list.append(lst2[j])
            j += 1
    if i < len(lst1):
        for q in range(i, len(lst1)):
            return_list.append(lst1[q])
    if j < len(lst2):
        for q in range(j, len(lst2)):
            return_list.append(lst2[q])
    return return_list

# given a list_of_lists as input,
#   if list_of_lists has 2 or more lists,
#        compute 2 way merge on elements i, i+1 for i = 0, 2, ...
#   return new list of lists after the merge
#   Handle the case when the list size is odd carefully.
def oneStepKWayMerge(list_of_lists):
    if len(list_of_lists) <= 1:
        return list_of_lists
    ret_list_of_lists = []
    k = len(list_of_lists)
    for i in range(0, k, 2):
        if i < k - 1:
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i + 1]))
        else:
            ret_list_of_lists.append(list_of_lists[k - 1])
    return ret_list_of_lists

# Given a list of lists wherein each
#    element of list_of_lists is sorted in ascending order,
# use the oneStepKWayMerge function repeatedly to merge them.
# Return a single merged list that is sorted in ascending order.
def kWayMerge(list_of_lists):
    k = len(list_of_lists)
    if k == 1:
        return list_of_lists[0]
    else:
        new_list_of_lists = oneStepKWayMerge(list_of_lists)
        return kWayMerge(new_list_of_lists)
