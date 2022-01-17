"""
copyright bijan shokrollahi
01.13.2022

"""
import unittest
from amazon_assessment_file import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        head = LinkedList(1)
        head.set_next(LinkedList(4))
        head.next.set_next(LinkedList(3))
        head.next.next.set_next(LinkedList(2))
        amazon_assessment = AmazonAssessment()
        maximum_pages = amazon_assessment.maximumPages(head=head)
        self.assertEqual(7, maximum_pages)

    def test_something2(self):
        head = LinkedList(1)
        head.set_next(LinkedList(4))
        head.next.set_next(LinkedList(3))
        head.next.next.set_next(LinkedList(2))
        head.next.next.next.set_next(LinkedList(5))
        head.next.next.next.next.set_next(LinkedList(1))
        amazon_assessment = AmazonAssessment()
        maximum_pages = amazon_assessment.maximumPages(head=head)
        self.assertEqual(9, maximum_pages)

    def test_something3(self):
        head = LinkedList(0)
        amazon_assessment = AmazonAssessment()
        maximum_pages = amazon_assessment.maximumPages(head=head)
        self.assertEqual(0, maximum_pages)

    def test_something4(self):
        head = LinkedList(1)
        head.set_next(LinkedList(4))
        head.next.set_next(LinkedList(3))
        head.next.next.set_next(LinkedList(2))
        amazon_assessment = AmazonAssessment()
        maximum_pages = amazon_assessment.maximumPages2(head=head)
        self.assertEqual(7, maximum_pages)

    def test_something5(self):
        head = LinkedList(1)
        head.set_next(LinkedList(4))
        head.next.set_next(LinkedList(3))
        head.next.next.set_next(LinkedList(2))
        head.next.next.next.set_next(LinkedList(5))
        head.next.next.next.next.set_next(LinkedList(1))
        amazon_assessment = AmazonAssessment()
        maximum_pages = amazon_assessment.maximumPages2(head=head)
        self.assertEqual(9, maximum_pages)

    def test_something6(self):
        head = LinkedList(0)
        amazon_assessment = AmazonAssessment()
        maximum_pages = amazon_assessment.maximumPages2(head=head)
        self.assertEqual(0, maximum_pages)

    def test_valid_discounts(self):
        amazon_assessment = AmazonAssessment()
        valid_discounts = amazon_assessment.findValidDiscountCoupons(['abba', 'abca'])
        self.assertEqual([1, 0], valid_discounts)


if __name__ == '__main__':
    unittest.main()
