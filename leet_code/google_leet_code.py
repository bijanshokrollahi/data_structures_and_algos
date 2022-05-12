"""
copyright bijan shokrollahi
03.11.2022

"""


def maxScore(cardPoints: list[int], k: int) -> int:
    if k > len(cardPoints) or len(cardPoints) == 0:
        return 0
    left = [0] * k
    right = [0] * k
    left[0] = cardPoints[0]
    right[0] = cardPoints[len(cardPoints)-1]
    for i in range(1, k):
        left[i] = left[i-1] + cardPoints[i]
    index = 1
    for i in range(len(cardPoints)-2, len(cardPoints)-(k+1), -1):
        right[index] = cardPoints[i] + right[index-1]
        index += 1
    left_index = k-1
    right_index = -1
    max_val = 0
    while left_index > -2 and right_index < k:
        curr_max = 0
        if left_index >= 0:
            curr_max += left[left_index]
        if right_index >= 0:
            curr_max += right[right_index]
        left_index -= 1
        right_index += 1
        max_val = max(max_val, curr_max)
    return max_val


def find_max_value_of_equation(points: list[list[int]], k: int) -> int:
    max_val = float('-inf')
    for i in range(0, len(points) - 1):
        x_i = points[i][0]
        y_i = points[i][1]
        for j in range(i + 1, len(points)):
            x_j = points[j][0]
            y_j = points[j][1]
            q = abs(x_i - x_j)
            if q <= k:
                curr_val = y_i + y_j + q
                max_val = max(max_val, curr_val)
    return max_val


def find_max_value_of_equation2(points: list[list[int]], k: int) -> int:
    """
    can i do this with a 2 pointer method?
    :param points:
    :param k:
    :return:
    """
    max_val = float('-inf')
    i = 0
    j = 1
    while j < len(points):
        x_i = points[i][0]
        y_i = points[i][1]
        x_j = points[j][0]
        y_j = points[j][1]
        q = abs(x_i - x_j)
        if q <= k:
            curr_val = y_i + y_j + q
            max_val = max(max_val, curr_val)
            j += 1
        else:
            i += 1
    return max_val
