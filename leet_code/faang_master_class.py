"""
copyright bijan shokrollahi
01.11.2022

"""


class DoubleLinkedList:
    def __init__(self, val, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

    def to_list(self) -> list:
        ans = []
        curr = self
        return self.find_depth(curr, ans)

    def find_depth(self, node: 'DoubleLinkedList', ans: list):
        if node is None:
            return ans
        ans.append(node.val)
        if node.child is not None:
            ans = self.find_depth(node.child, ans)
        return self.find_depth(node.next, ans)


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_val(self, val):
        self.val = val

    def set_next(self, next):
        self.next = next

    def to_list(self) -> list:
        ans = []
        curr = self
        while curr is not None:
            ans.append(curr.val)
            curr = curr.next
        return ans


class FaangMasterClass:
    def __init__(self, val_list: list):
        assert val_list is not None
        self.head = ListNode(val_list[0])
        if len(val_list) != 1:
            curr = self.head
            for i in range(1, len(val_list)):
                curr.next = ListNode(val_list[i])
                curr = curr.next

    def get_head(self):
        return self.head

    def get_len(self) -> int:
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def to_list(self) -> list:
        curr = self.get_head()
        ans = []
        while curr is not None:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def reverse(self):
        curr = self.get_head()
        prev = None
        next_node = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    @staticmethod
    def reverse_with_tail(head):
        curr = head
        prev = None
        next_node = None
        tail = curr
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev, tail

    def reverse_subsection(self, left, right):
        if left == right:
            return self.head
        count = 1
        curr = self.get_head()
        left_dot_prev = None
        right_dot_next = None
        sub_section_head = None
        while right_dot_next is None and curr is not None:
            if count + 1 == left:
                left_dot_prev = curr
            if count == left:
                sub_section_head = curr
            if count == right:
                right_dot_next = curr.next
                curr.next = None
            count += 1
            curr = curr.next
        l, r = self.reverse_with_tail(sub_section_head)
        if left_dot_prev is not None:
            left_dot_prev.next = l
        r.next = right_dot_next
        return self.get_head()

    def reverse_sub_section_stack(self, left, right):
        if left == right:
            return self.head
        head = self.head
        curr = head
        count = 1
        stack = []
        prev_left = None
        right_next = None
        while curr is not None and right_next is None:
            if left <= count <= right:
                stack.append(curr)
            if count + 1 == left:
                prev_left = curr
            if count == right:
                right_next = curr.next
                curr.next = None
            count += 1
            curr = curr.next
        curr = None
        if prev_left is not None:
            prev_left.next = stack.pop()
            curr = prev_left.next
        while len(stack) > 0:
            if curr is None:
                curr = stack.pop()
            else:
                curr.next = stack.pop()
                curr = curr.next
        curr.next = right_next
        return head

    def reverse_subsection_linked_list(self, m, n) -> ListNode:
        head = self.get_head()
        curr_position = 1
        curr_node = head
        start = head
        while curr_position < m:
            start = curr_node
            curr_node = curr_node.next
            curr_position += 1
        new_list = None
        tail = curr_node
        while m <= curr_position <= n:
            next = curr_node.next
            curr_node.next = new_list
            new_list = curr_node
            curr_node = next
            curr_position += 1
        start.next = new_list
        tail.next = curr_node
        if m == 1:
            return new_list
        return head


class DoubleNodeWChild:
    def __init__(self, val, prev: 'DoubleNodeWChild' = None, next_node: 'DoubleNodeWChild' = None,
                 child: 'DoubleNodeWChild' = None):
        self.val = val
        self.prev = prev
        self.next_node = next_node
        self.child = child


class DoubleLinkedListWChild:
    def __init__(self, val):
        self.head = DoubleNodeWChild(val)

    def flatten(self):
        curr = self.head
        while curr is not None:
            if curr.child is not None:
                self.flatten_helper(curr, curr.child, curr.next_node)
            curr = curr.next_node

    @staticmethod
    def flatten_helper(curr: 'DoubleNodeWChild', child: 'DoubleNodeWChild', next_node: 'DoubleNodeWChild'):
        if curr is None:
            return
        if child is None:
            assert curr.next_node == next_node
        curr.next_node = child
        tmp_curr = child
        curr.child = None
        child.prev = curr
        while tmp_curr.next_node is not None:
            tmp_curr = tmp_curr.next_node
        tmp_curr.next_node = next_node
        if next_node is not None:
            next_node.prev = tmp_curr

    def to_list(self) -> list:
        """
        must be flattened
        :return: list representation
        """
        dll_as_list = []
        curr = self.head
        while curr is not None:
            dll_as_list.append(curr.val)
            curr = curr.next_node
        return dll_as_list


class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LLDetectCycle:
    def __init__(self, val):
        self.head = LLNode(val=val)

    def cycle_exists(self) -> bool:
        slow = self.head
        fast = slow
        if slow is None:
            return False
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast.next is None:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False


def is_valid(s: str) -> bool:
    options_dict = {
        '(': 'left',
        ')': 'right',
        '[': 'left',
        ']': 'right',
        '{': 'left',
        '}': 'right'
    }
    mapping_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    ans_stack = []
    for char in s:
        if options_dict.get(char) == 'left':
            ans_stack.append(char)
        elif options_dict.get(char) == 'right':
            if len(ans_stack) == 0:
                return False
            if mapping_dict.get(ans_stack.pop()) != char:
                return False
    if len(ans_stack) != 0:
        return False
    return True
