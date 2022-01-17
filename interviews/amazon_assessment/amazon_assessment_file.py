"""
copyright bijan shokrollahi
01.13.2022

"""


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class AmazonAssessment:
    def maximumPages(self, head: LinkedList):
        if head is None:
            return 0
        num_pages = 0
        prev = None
        max_num_pages = 0
        while head.next is not None:
            num_pages += head.get_data()
            curr = head.get_next()
            while curr is not None:
                if curr.next is None:
                    prev.next = None
                    num_pages += curr.get_data()
                    curr = None
                    max_num_pages = max(num_pages, max_num_pages)
                    num_pages = 0
                else:
                    prev = curr
                    curr = curr.get_next()
            head = head.get_next()
        return max_num_pages

    def maximumPages2(self, head: LinkedList):
        if head is None:
            return 0
        list_of_pages = []
        curr = head
        while curr is not None:
            list_of_pages.append(curr.data)
            curr = curr.next
        max_pages = 0
        i = 0
        j = len(list_of_pages) - 1
        while i <= j:
            max_pages = max(max_pages, (list_of_pages[i] + list_of_pages[j]))
            i += 1
            j -= 1
        return max_pages

    def findValidDiscountCoupons(self, discounts: list):
        are_discounts_valid = [0] * len(discounts)
        valid_dicounts = {}
        for i in range(len(discounts)):
            val, valid_dicounts = self.check_stripped_string(discounts[i], valid_dicounts)
            are_discounts_valid[i] = max(self.check_empty_string(discounts[i]), val)
        return are_discounts_valid

    def check_empty_string(self, curr_string):
        if curr_string == '':
            return 1
        return 0

    def check_stripped_string(self, curr_string, valid_discounts):
        actual_str = curr_string
        i = 0
        j = len(curr_string) - 1
        # while i <= j:
        #     if curr_string[i] != curr_string[j]:
        #
        # for i in range(0, )
        while curr_string != '':
            for key, val in valid_discounts.items():
                if key in curr_string:
                    curr_string.replace(key, '')
                    if self.check_empty_string(curr_string) == 1 or valid_discounts.get(curr_string, False):
                        valid_discounts[actual_str] = True
                        return 1, valid_discounts
                    if len(curr_string) == 2 and curr_string[0] == curr_string[1]:
                        valid_discounts[actual_str] = True
                        return 1, valid_discounts
        return 0, valid_discounts

