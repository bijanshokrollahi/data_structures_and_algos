"""
copyright bijan shokrollahi
01.11.2022

"""


class ListNode:
    def __init__(self, val, next = None):
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

    def reverse(self):
        curr = self.get_head()
        prev = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev