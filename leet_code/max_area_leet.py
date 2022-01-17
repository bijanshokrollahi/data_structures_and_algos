"""
copyright bijan shokrollahi
01/04/2022
"""

import heapq


class Area:
    def __init__(self, a, i, j):
        self.area = -abs(a)
        self.i = i
        self.j = j

    def __lt__(self, nxt):
        return self.area < nxt.area


class MaxArea:
    def __init__(self, height: list[int]):
        self.heights = height
        area, indices = self.brute_force_find()
        self.area = abs(area)
        self.indices = indices

    def get_area(self) -> int:
        return abs(self.area)

    def get_indices(self) -> tuple:
        return self.indices

    def brute_force_find(self):
        if len(self.heights) < 2:
            return 0, (0, 0)
        heap = []
        for i in range(0, len(self.heights) - 1):
            for j in range(i + 1, len(self.heights)):
                area = min(self.heights[i], self.heights[j]) * (j - i)
                heap.append(Area(area, i, j))
        heapq.heapify(heap)
        ans = heap.pop(0)
        return ans.area, (ans.i, ans.j)


class MaxAreaNotBruteForce:
    def __init__(self, height: list[int]):
        self.heights = height
        self.max_area = self.find_max_area()

    def get_area(self):
        return self.max_area

    def find_max_area(self) -> int:
        if len(self.heights) < 2:
            return 0
        i = 0
        j = len(self.heights) - 1
        curr_area = 0
        while i != j:
            curr_area = max(curr_area, (min(self.heights[i], self.heights[j]) * (j - i)))
            if self.heights[i] <= self.heights[j]:
                i += 1
            else:
                j -= 1
        return curr_area


class MaxTrappedWaterBrute:
    def __init__(self, height: list[int]):
        self.height = height
        self.max_area = self._find_max_area()

    def get_area(self):
        return self.max_area

    def _find_max_area(self):
        if len(self.height) < 3:
            return 0
        total_area = 0
        curr = 0
        while curr < len(self.height):
            left = 0
            left_max = 0
            right = len(self.height) - 1
            right_max = 0
            while left <= curr <= right:
                if left != curr:
                    left_max = max(left_max, self.height[left])
                    left += 1
                if right != curr:
                    right_max = max(right_max, self.height[right])
                    right -= 1
                if left == curr and right == curr:
                    break
            curr_water = min(left_max, right_max) - self.height[curr]
            if curr_water > 0:
                total_area += curr_water
            curr += 1
        return total_area


class MaxTrappedWater(MaxTrappedWaterBrute):
    def __init__(self, height: list[int]):
        super().__init__(height)

    def _find_max_area(self):
        length_of_arr = len(self.height)
        max_left_of_point = {}
        max_right_of_point = {}
        curr_max = 0
        max_left_of_point[0] = curr_max
        right_most_index = length_of_arr - 1
        max_right_of_point[right_most_index] = 0
        for i in range(0, right_most_index):
            curr_max = max(curr_max, self.height[i])
            curr_pointer = i + 1
            max_left_of_point[curr_pointer] = curr_max
        curr_max = 0
        for i in range(right_most_index, 0, -1):
            curr_max = max(curr_max, self.height[i])
            curr_pointer = i - 1
            max_right_of_point[curr_pointer] = curr_max
        total_rain_water = 0
        for i in range(length_of_arr):
            curr_water = min(max_left_of_point[i], max_right_of_point[i]) - self.height[i]
            if curr_water > 0:
                total_rain_water += curr_water
        return total_rain_water


class MaxTrappedWaterElite(MaxTrappedWaterBrute):
    def __init__(self, height: list[int]):
        super().__init__(height=height)

    def _find_max_area(self):
        if len(self.height) < 3:
            return 0
        max_left = 0
        max_right = 0
        total_water = 0
        left_index = 0
        right_index = len(self.height) - 1
        while left_index != right_index:
            if self.height[left_index] <= self.height[right_index]:
                if max_left > self.height[left_index]:
                    curr_height = max_left - self.height[left_index]
                    if curr_height > 0:
                        total_water += curr_height
                else:
                    max_left = self.height[left_index]
                left_index += 1
            else:
                if max_right > self.height[right_index]:
                    curr_height = max_right - self.height[right_index]
                    if curr_height > 0:
                        total_water += curr_height
                else:
                    max_right = self.height[right_index]
                right_index -= 1
        return total_water


class TypedOutStrings:
    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2
        self.is_equal = self._find_is_equal()

    def get_is_equal(self):
        return self.is_equal

    def _find_is_equal(self):
        typed_s1 = self.get_typed(self.s1)
        typed_s2 = self.get_typed(self.s2)
        return typed_s1 == typed_s2

    def get_typed(self, s1):
        typed_s1 = []
        for char in s1:
            if char == '#':
                if len(typed_s1) != 0:
                    typed_s1.pop()
            else:
                typed_s1.append(char)
        return typed_s1


def string_as_typed(s1: str, s2: str) -> bool:
    pointer_s1 = len(s1) - 1
    pointer_s2 = len(s2) - 1
    while pointer_s2 > -1 and pointer_s1 > -1:
        if s1[pointer_s1] == '#':
            pointer_s1 -= 2
        if s2[pointer_s2] == '#':
            pointer_s2 -= 2
        if pointer_s1 < 0 or pointer_s2 < 0:
            continue
        if s1[pointer_s1] != s2[pointer_s2]:
            return False
    return True


def string_optimal(s: str, t: str) -> bool:
    s_pointer = len(s) - 1
    t_pointer = len(t) - 1
    while s_pointer >= 0 or t_pointer >= 0:
        if s[s_pointer] == '#' or t[t_pointer] == '#':
            if s[s_pointer] == '#':
                backcount = 2
                while backcount > 0:
                    s_pointer -= 1
                    backcount -= 1
                    if s[s_pointer] == '#':
                        backcount += 2
            else:
                backcount = 2
                while backcount > 0:
                    t_pointer -= 1
                    backcount -= 1
                    if t[t_pointer] == '#':
                        backcount += 2
        else:
            if s[s_pointer] != t[t_pointer]:
                return False
            s_pointer -= 1
            t_pointer -= 1
    return True


def longest_substring(s: str) -> int:
    max_len = 0
    for i in range(len(s)):
        curr_len = 0
        seen_chars = []
        for j in range(i, len(s)):
            if s[j] not in seen_chars:
                curr_len += 1
                seen_chars.append(s[j])
            else:
                curr_len = 0
                seen_chars = []
            max_len = max(max_len, curr_len)
    return max_len


def longest_substring_2(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    max_len = 0
    seen_chars = {}
    left = 0
    for right in range(0, len(s)):
        curr_char = s[right]
        prev_seen_char = seen_chars.get(curr_char, -1)
        if prev_seen_char >= left:
            left = prev_seen_char + 1
        seen_chars[curr_char] = right
        max_len = max(max_len, (right - left) + 1)
    return max_len
