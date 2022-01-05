"""
copyright bijan shokrollahi
10.06.2021

"""

from numpy.fft import fft, ifft, fftfreq
from numpy import real, imag
import csv
from matplotlib import pyplot as plt

#
# weekly_prices = []
# dates = []
#
# plt.plot(range(len(weekly_prices)), weekly_prices, '-b')
# plt.xlabel('Week #')
# plt.ylabel('Crude Oil Future Price')
# # here we have computed the fft of the weekly_prices
# fft_data = fft(weekly_prices)
# N = len(fft_data)
# assert (N == len(weekly_prices))
#
#
# # TODO: first fill in the frequencies call this list
# # fft_frequencies -- it must have length N
# # it must store the frequencies of each element in the fft_data
# # ensure that the frequencies of the second half are negative.
# # your code here
#
# # This function will be useful for you. Please go through the code.
#
#
# def select_all_items_in_freq_range(lo, hi):
#     # TODO: go through the fft_data and select only those frequencies in the range lo/hi
#     new_fft_data = []  # make sure we have the 0 frequency component
#     fft_frequencies = []
#     for (fft_val, fft_freq) in zip(fft_data, fft_frequencies):
#         if lo <= fft_freq and fft_freq < hi:
#             new_fft_data.append(fft_val)
#         elif -hi < fft_freq and fft_freq <= -lo:
#             new_fft_data.append(fft_val)
#         else:
#             new_fft_data.append(0.0)
#     filtered_data = ifft(new_fft_data)
#     assert all(abs(imag(x)) <= 1E-10 for x in filtered_data)
#     return [real(x) for x in filtered_data]
#
#
# upto_1_year = []  # All signal components with frequency < 1/52
# one_year_to_1_quarter = []  # All signal components with frequency between 1/52 (inclusive) and 1/13 weeks (not inclusive)
# less_than_1_quarter = []  # All signal components with frequency >= 1/13
#
#
# # TODO: Redefine the three lists using the select_all_items function
# # your code here
#
#
# # inputs sets a, b, c
# # return True if there exist n1 in a, n2 in B such that n1+n2 in C
# # return False otherwise
# # number n which signifies the maximum number in a, b, c
# # here is a useful reference to set data structure in python
# # https://docs.python.org/3/tutorial/datastructures.html#sets


def check_sum_exists(a, b, c, n):
    a_coeffs = [0] * n
    b_coeffs = [0] * n
    # convert sets a, b into polynomials as provided in the hint
    # a_coeffs and b_coeffs should contain the result
    # your code here
    for coeff in a:
        a_coeffs[coeff] = 1
    for coeff in b:
        b_coeffs[coeff] = 1
    # multiply them together
    c_coeffs = polynomial_multiply(a_coeffs, b_coeffs)
    # use the result to solve the problem at hand
    # your code here
    for coeff in c:
        if c_coeffs[coeff] >= .5:
            return True
    return False
    # return True/False


def polynomial_multiply(a_coeff_list, b_coeff_list):
    # Return the coefficient list of the multiplication
    # of the two polynomials
    # Returned list must be a list of floating point numbers.
    # Please convert list from complex to reals by using the
    # real function in numpy.
    for i in range(len(a_coeff_list) - 1):
        b_coeff_list.append(0)
    for i in range(len(b_coeff_list) - 1):
        a_coeff_list.append(0)
    a_fft = fft(a_coeff_list)
    b_fft = fft(b_coeff_list)
    c = []
    for i in range(len(a_fft)):
        c.append(a_fft[i] * b_fft[i])
    return real(ifft(c))


def maxSubArray(a):
    n = len(a)
    if n == 1:
        return 0
    # your code here
    # left, right, sum_x = find_max_subarray(a, 0, n-1)
    # return sum_x
    return find_min_and_max_elements(a, 0, n - 1)


def simple_sub_array(a, low, high):
    if low == high:
        return 0
    elif low + 1 == high:
        return max((a[high] - a[low]), 0)
    else:
        mid = (low + high) // 2
        left_min, left_max = find_min_and_max_elements(a, low, mid)
        right_min, right_max = find_min_and_max_elements(a, mid + 1, high)
        return max((left_max - left_min), (right_max - right_min), (right_max - left_min))


def find_min_and_max_elements(a, low, high):
    if low == high:
        return 0
    elif low == high + 1:
        return max(a[high] - a[low, 0])
    else:
        mid = (low + high) // 2
        m1 = find_min_and_max_elements(a, low, mid)
        m2 = find_min_and_max_elements(a, mid + 1, high)
        y1 = max_element(a, mid + 1, high)
        x1 = min_element(a, low, mid)
        return max(m1, m2, y1 - x1)


def min_element(a, low, high):
    min_ele = float('inf')
    for i in range(low, high + 1):
        min_ele = min(min_ele, a[i])
    return min_ele


def max_element(a, low, high):
    max_ele = float('-inf')
    for i in range(low, high + 1):
        max_ele = max(max_ele, a[i])
    return max_ele


def find_max_subarray(a, low, high):
    if high == low:
        return low, high, a[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_subarray(a, low, mid)
    right_low, right_high, right_sum = find_max_subarray(a, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(a, low, mid, high):
    left_sum = float('-inf')
    sum_x = 0
    max_left = None
    max_right = None
    for i in range(mid, low, -1):
        sum_x += a[i]
        if sum_x > left_sum:
            left_sum = sum_x
            max_left = i
    right_sum = float('-inf')
    sum_x = 0
    for j in range(mid + 1, high):
        sum_x += a[j]
        if sum_x > right_sum:
            right_sum = sum_x
            max_right = j
    return max_left, max_right, left_sum + right_sum
