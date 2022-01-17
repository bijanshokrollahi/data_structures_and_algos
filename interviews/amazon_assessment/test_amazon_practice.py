import unittest
from amazon_practice import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        repository = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad']
        customer_query = 'mouse'
        amazon_practice = AmazonPractice()
        search_suggestions = amazon_practice.searchSuggestions(repository=repository, customerQuery=customer_query)
        self.assertIsNotNone(search_suggestions)

    def test_amazon(self):
        repository = ['jbckjsc', 'Kjabnkasj', 'iojncklsmc', 'dnklasnmaskl', 'ohdkan', 'niahdklas', 'iandkja',
                      'hjdklasnc', 'ancksJ', 'nhx']
        customer_query = 'abcd'
        amazon_practice = AmazonPractice()
        search_suggestions = amazon_practice.searchSuggestions(repository=repository, customerQuery=customer_query)
        self.assertIsNotNone(search_suggestions)

    def test_amazon_fresh(self):
        amazon_practice = AmazonPractice()
        code_list = [['apple', 'apple'], ['banana', 'anything', 'banana']]
        shopping_cart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
        is_winner = amazon_practice.amazon_fresh_winner(codeList=code_list, shoppingCart=shopping_cart)
        self.assertEqual(1, is_winner)


if __name__ == '__main__':
    unittest.main()
