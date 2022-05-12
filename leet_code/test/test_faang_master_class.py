"""
copyright bijan shokrollahi
01.11.2022

"""
import unittest
from leet_code.faang_master_class import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        self.assertIsNotNone(linked_list.get_head())
        self.assertEqual(5, linked_list.get_len())

    def test_reverse(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        reversed = linked_list.reverse()
        self.assertIsNotNone(reversed)

    def test_reverse_sub_section(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        reversed_sub_section = linked_list.reverse_subsection(2, 4)
        self.assertEqual([1, 4, 3, 2, 5], reversed_sub_section.to_list())

    def test_reverse_sub_section2(self):
        linked_list = FaangMasterClass([5])
        reversed_sub_section = linked_list.reverse_subsection(1, 1)
        self.assertEqual([5], reversed_sub_section.to_list())

    @unittest.skipIf(True, 'skipping')
    def test_reverse_sub_section3(self):
        linked_list = FaangMasterClass([3, 5])
        reversed_sub_section = linked_list.reverse_subsection(1, 2)
        self.assertEqual([5, 3], reversed_sub_section.to_list())

    def test_reverse_sub_section4(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        reversed_sub_section = linked_list.reverse_sub_section_stack(2, 4)
        self.assertEqual([1, 4, 3, 2, 5], reversed_sub_section.to_list())

    def test_reverse_sub_section5(self):
        linked_list = FaangMasterClass([5])
        reversed_sub_section = linked_list.reverse_sub_section_stack(1, 1)
        self.assertEqual([5], reversed_sub_section.to_list())

    def test_reverse_sub_section6(self):
        linked_list = FaangMasterClass([3, 5])
        reversed_sub_section = linked_list.reverse_sub_section_stack(1, 2)
        self.assertEqual([5, 3], reversed_sub_section.to_list())

    def test_reverse_linked_list_ans(self):
        linked_list = FaangMasterClass([3, 5])
        reversed_sub_section = linked_list.reverse_subsection_linked_list(1, 2)
        self.assertEqual([5, 3], reversed_sub_section.to_list())

    def test_reverse_sub_section_ans(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        reversed_sub_section = linked_list.reverse_subsection_linked_list(2, 4)
        self.assertEqual([1, 4, 3, 2, 5], reversed_sub_section.to_list())

    def test_reverse_sub_section2_ans(self):
        linked_list = FaangMasterClass([5])
        reversed_sub_section = linked_list.reverse_subsection_linked_list(1, 1)
        self.assertEqual([5], reversed_sub_section.to_list())

    def test_reverse_sub_section3_ans(self):
        linked_list = FaangMasterClass([3, 5])
        reversed_sub_section = linked_list.reverse_subsection_linked_list(1, 2)
        self.assertEqual([5, 3], reversed_sub_section.to_list())

    def test_reverse_sub_section4_ans(self):
        linked_list = FaangMasterClass([1, 2, 3, 4, 5])
        reversed_sub_section = linked_list.reverse_subsection_linked_list(2, 4)
        self.assertEqual([1, 4, 3, 2, 5], reversed_sub_section.to_list())

    def test_reverse_sub_section5_ans(self):
        linked_list = FaangMasterClass([5])
        reversed_sub_section = linked_list.reverse_subsection_linked_list(1, 1)
        self.assertEqual([5], reversed_sub_section.to_list())

    def test_flatten_linked_list(self):
        head = DoubleLinkedList(1)
        head.next = DoubleLinkedList(2)
        head.next.child = DoubleLinkedList(7)
        head.next.child.next = DoubleLinkedList(8)
        head.next.child.next.child = DoubleLinkedList(10)
        head.next.child.next.child.next = DoubleLinkedList(11)
        head.next.child.next.next = DoubleLinkedList(9)
        head.next.next = DoubleLinkedList(3)
        head.next.next.next = DoubleLinkedList(4)
        head.next.next.next.next = DoubleLinkedList(5)
        head.next.next.next.next.child = DoubleLinkedList(12)
        head.next.next.next.next.child.next = DoubleLinkedList(13)
        head.next.next.next.next.next = DoubleLinkedList(6)
        ans = head.to_list()
        self.assertEqual([1, 2, 7, 8, 10, 11, 9, 3, 4, 5, 12, 13, 6], ans)

    def test_flatten_double_link_w_child(self):
        dbl_ll = DoubleLinkedListWChild(1)
        dbl_ll.head.next_node = DoubleNodeWChild(2)
        dbl_ll.head.next_node.child = DoubleNodeWChild(7)
        dbl_ll.head.next_node.child.next_node = DoubleNodeWChild(8)
        dbl_ll.head.next_node.child.next_node.child = DoubleNodeWChild(10)
        dbl_ll.head.next_node.child.next_node.child.next_node = DoubleNodeWChild(11)
        dbl_ll.head.next_node.child.next_node.next_node = DoubleNodeWChild(9)
        dbl_ll.head.next_node.next_node = DoubleNodeWChild(3)
        dbl_ll.head.next_node.next_node.next_node = DoubleNodeWChild(4)
        dbl_ll.head.next_node.next_node.next_node.next_node = DoubleNodeWChild(5)
        dbl_ll.head.next_node.next_node.next_node.next_node.child = DoubleNodeWChild(12)
        dbl_ll.head.next_node.next_node.next_node.next_node.child.next_node = DoubleNodeWChild(13)
        dbl_ll.head.next_node.next_node.next_node.next_node.next_node = DoubleNodeWChild(6)
        dbl_ll.flatten()
        dll_as_list = dbl_ll.to_list()
        self.assertEqual([1, 2, 7, 8, 10, 11, 9, 3, 4, 5, 12, 13, 6], dll_as_list)

    def test_ll_cycle(self):
        ll = LLDetectCycle(1)
        ll.head.next = LLNode(2)
        ll.head.next.next = LLNode(3)
        ll.head.next.next = LLNode(4)
        ll.head.next.next.next = LLNode(5)
        ll.head.next.next.next.next = LLNode(6)
        ll.head.next.next.next.next.next = ll.head.next.next
        cycle_exists = ll.cycle_exists()
        self.assertTrue(cycle_exists)

    def test_ll_cycle2(self):
        ll = LLDetectCycle(1)
        ll.head.next = LLNode(2)
        ll.head.next.next = LLNode(3)
        ll.head.next.next = LLNode(4)
        ll.head.next.next.next = LLNode(5)
        ll.head.next.next.next.next = LLNode(6)
        ll.head.next.next.next.next.next = LLNode(7)
        cycle_exists = ll.cycle_exists()
        self.assertFalse(cycle_exists)

    def test_ll_cycle3(self):
        ll = LLDetectCycle(1)
        ll.head = None
        cycle_exists = ll.cycle_exists()
        self.assertFalse(cycle_exists)

    def test_valid_par(self):
        self.assertTrue(is_valid('()'))

    def test_valid_par2(self):
        self.assertFalse(is_valid('({'))

    def test_valid_par3(self):
        self.assertFalse(is_valid('({{}}'))

    def test_valid_par4(self):
        self.assertTrue(is_valid('({{}})'))

    def test_valid_par5(self):
        self.assertTrue(is_valid(''))

    def test_valid_par6(self):
        self.assertFalse(is_valid('))))))))'))

    def test_valid_par7(self):
        self.assertFalse(is_valid('{{{{{{{{{{'))

    def test_valid_par8(self):
        self.assertFalse(is_valid('{'))

    def test_valid_par9(self):
        self.assertFalse(is_valid('}'))

    def test_valid_par10(self):
        self.assertTrue(is_valid('abcdefg'))


if __name__ == '__main__':
    unittest.main()
