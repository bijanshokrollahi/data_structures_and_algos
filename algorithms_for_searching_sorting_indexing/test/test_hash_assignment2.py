import unittest
from hash_assignment2 import *
from matplotlib import pyplot as plt


class MyTestCase(unittest.TestCase):
    def test_something(self):

        # Let's see how well your solution performs for the Great Gatsby words
        cms_list = initialize_k_counters(5, 1000)
        for word in longer_words_gg:
            increment_counters(cms_list, word)

        discrepencies = []
        for word in longer_words_gg:
            l = approximate_count(cms_list, word)
            r = word_freq_gg[word]
            assert (l >= r)
            discrepencies.append(l - r)

        plt.hist(discrepencies)

        assert (
                    max(discrepencies) <= 200), 'The largest discrepency must be definitely less than 200 with high probability. Please check your implementation'
        print('Passed all tests: 10 points')

    def test_something2(self):
        # Let's see how well your solution performs for the War and Peace
        cms_list = initialize_k_counters(5, 5000)
        for word in longer_words_wp:
            increment_counters(cms_list, word)

        discrepencies = []
        for word in longer_words_wp:
            l = approximate_count(cms_list, word)
            r = word_freq_wp[word]
            assert (l >= r)
            discrepencies.append(l - r)

        plt.hist(discrepencies)
        print('Passed all tests: 5 points')


if __name__ == '__main__':
    unittest.main()
