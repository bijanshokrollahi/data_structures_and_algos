"""
copyright bijan shokrollahi
11/08/2021

"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """

        :rtype: object
        """
        i = 0
        j = 0
        return_list = []
        while i <= (len(nums1) - 1) and j <= (len(nums2) - 1):
            if nums1[i] < nums2[j]:
                return_list.append(nums1[i])
                i += 1
            else:
                return_list.append(nums2[j])
                j += 1
        if i < len(nums1):
            for q in range(i, len(nums1)):
                return_list.append(nums1[q])
        if j < len(nums2):
            for q in range(j, len(nums2)):
                return_list.append(nums2[q])

        N = len(return_list)
        if N % 2 == 0:
            half = N // 2
            half1 = half - 1
            return (return_list[half] + return_list[half1]) / 2
        else:
            mid = N // 2
            return return_list[mid]

    def is_palindrome(self, x: int) -> bool:
        x_as_str = str(x)
        n = len(x_as_str)
        i = 0
        j = n - 1
        while i <= n // 2:
            if x_as_str[i] != x_as_str[j]:
                return False
            i += 1
            j -= 1
        return True

    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        curr = ListNode()
        head = curr
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                current_sum = carry + l2.val
                str_sum: str = str(current_sum)
                if len(str_sum) > 1:
                    carry = int(str_sum[0])
                    curr.val = int(str_sum[1])
                else:
                    carry = 0
                    curr.val = current_sum
                l2 = l2.next
            elif l2 is None:
                current_sum = carry + l1.val
                str_sum = str(current_sum)
                if len(str_sum) > 1:
                    carry = int(str_sum[0])
                    curr.val = int(str_sum[1])
                else:
                    carry = 0
                    curr.val = current_sum
                l1 = l1.next
            else:
                current_sum = l1.val + l2.val + carry
                str_sum = str(current_sum)
                if len(str_sum) > 1:
                    carry = int(str_sum[0])
                    curr.val = int(str_sum[1])
                else:
                    carry = 0
                    curr.val = current_sum
                l1 = l1.next
                l2 = l2.next
            curr.next = ListNode()
            curr = curr.next
        i = 0
        p1 = head
        p2 = head
        while p1 is not None:
            if p1.next is None:
                p2.next = None
            elif i != 0:
                p2 = p2.next
            p1 = p1.next
            i += 1
        return head

    @staticmethod
    def create_list_node(num_list: list) -> 'ListNode':
        list_node = ListNode()
        head = list_node
        for num in num_list:
            list_node.val = num
            list_node.next = ListNode()
            list_node = list_node.next
        return head

    @staticmethod
    def to_list(list_node: 'ListNode') -> list:
        ans = []
        while list_node is not None:
            ans.append(list_node.val)
            list_node = list_node.next
        return ans

    def length_of_longest_substring(self, s: str) -> int:
        return self.find_longest_substring(s, 0, [])

    def find_longest_substring(self, s: str, pos: int, chars: list):
        if pos >= len(s):
            return len(chars)
        if s[pos] not in chars:
            chars.append(s[pos])
            return max(1, len(chars), self.find_longest_substring(s, pos+1, []),
                       self.find_longest_substring(s, pos+1, chars))
        else:
            return max(1, len(chars), self.find_longest_substring(s, pos+1, []))

    def hammingWeight(self, n: str) -> int:
        ans = 0
        for i in range(0, len(n)):
            if n[i] == '1':
                ans += 1
        return ans

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_dict = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if ans_dict.get(sorted_word):
                ans_dict.get(sorted_word).append(word)
            else:
                ans_dict[sorted_word] = [word]
        ans = []
        for key, val in ans_dict.items():
            ans.append(val)
        return ans

    def two_sum(self, num_list: list[int], target: int) -> tuple[int, int]:
        # n^2
        for i in range(0, len(num_list)):
            for j in range(i+1, len(num_list)):
                if num_list[i] + num_list[j] == target:
                    return i, j
        return tuple()

    def two_sum_2(self, num_list: list[int], target: int) -> tuple[int, int]:
        table = {}
        for i in range(0, len(num_list)):
            if table.get(num_list[i]) is not None:
                return table.get(num_list[i]), i
            key = target - num_list[i]
            table[key] = i
        return tuple()

    def largest_bucket(self, bucket_list: list[int]) -> int:
        max_area = 0
        for i in range(len(bucket_list)-1):
            for j in range(i+1, len(bucket_list)):
                if min(bucket_list[i], bucket_list[j]) * (j - i) > max_area:
                    max_area = min(bucket_list[i], bucket_list[j]) * (j - i)
        return max_area

    def largest_bucket_2(self, bucket_list: list[int]) -> int:
        max_area = 0
        
        return max_area

    # def two_sum_fft(self, num_list: list[int], target: int) -> tuple[int, int]:
    #     largest_val = max(num_list)
    #     smallest_val = min(num_list)
    #     n = 0
    #     if largest_val < 0:
    #         n = abs(smallest_val) - abs(largest_val)
    #     elif smallest_val < 0:
    #         n = largest_val + abs(smallest_val)
    #     else:
    #         n = largest_val - smallest_val
    #     represntation = [0] * n
    #     # create mappping
    #     dict_mapping = {}
    #     j = 0
    #     for i in range(smallest_val, largest_val+1):
    #         dict_mapping[j] = i
    #         j+=1
    #     for val in num_list:



class ListNode:
    def __init__(self, val=0, next_el=None):
        self.val = val
        self.next = next_el
