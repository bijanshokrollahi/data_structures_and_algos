# Python3 program Miller-Rabin randomized primality test
# Copied from geeksforgeeks: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
import random


# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
    # Initialize result
    res = 1

    # Update x if it is more than or
    # equal to p
    x = x % p
    while y > 0:

        # If y is odd, multiply
        # x with result
        if y & 1:
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4)

    # Compute a^d % n
    x = power(a, d, n)

    if x == 1 or x == n - 1:
        return True

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

        # Return composite
    return False


# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime(n, k):
    # Corner cases
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Iterate given nber of 'k' times
    for i in range(k):
        if not miillerTest(d, n):
            return False

    return True


# Driver Code
# Number of iterations
k = 4

print("All primes smaller than 100: ")
for n in range(1, 100):
    if isPrime(n, k):
        print(n, end=" ")

    # This code is contributed by mits (see citation above)


# Get a random triple (p, a, b) where p is prime and a,b are numbers betweeen 2 and p-1
def get_random_hash_function():
    n = random.getrandbits(64)
    if n < 0:
        n = -n
    if n % 2 == 0:
        n = n + 1
    while not isPrime(n, 20):
        n = n + 1
    a = random.randint(2, n - 1)
    b = random.randint(2, n - 1)
    return n, a, b


# hash function fora number
def hashfun(hfun_rep, num):
    (p, a, b) = hfun_rep
    return (a * num + b) % p


# hash function for a string.
def hash_string(hfun_rep, hstr):
    n = hash(hstr)
    return hashfun(hfun_rep, n)


# We will now implement the algorithm for a bank of k counters

# Initialize k different counters
def initialize_k_counters(k, m):
    return [CountMinSketch(m) for i in range(k)]


# Function increment_counters
# increment each of the individual counters with the word
def increment_counters(count_min_sketches, word):
    for count_min_sketch in count_min_sketches:
        count_min_sketch.increment(word)

# your code here


# Function: approximate_count
# Get the approximate count by querying each counter bank and taking the minimum
def approximate_count(count_min_sketches, word):
    return min([cms.approximateCount(word) for cms in count_min_sketches])


# Class for implementing a count min sketch "single bank" of counters
class CountMinSketch:
    # Initialize with `num_counters`
    def __init__(self, num_counters):
        self.m = num_counters
        self.hash_fun_rep = get_random_hash_function()
        self.counters = [0] * self.m

    # your code here

    # function: increment
    # given a word, increment its count in the countmin sketch
    def increment(self, word):
        self.counters[hash_string(self.hash_fun_rep, word) % self.m] += 1
    # your code here

    # function: approximateCount
    # Given a word, get its approximate count
    def approximateCount(self, word):
        # your code here
        return self.counters[hash_string(self.hash_fun_rep, word) % self.m]


class BloomFilter:
    def __init__(self, nbits, nhash):
        self.bits = [False] * nbits  # Initialize all bits to fals
        self.m = nbits
        self.k = nhash
        # get k randdom hash functions
        self.hash_fun_reps = [get_random_hash_function() for i in range(self.k)]

    # Function to insert a word in a Bloom filter.
    def insert(self, word):
        # your code here
        for hash_fun_rep in self.hash_fun_reps:
            self.bits[hash_string(hash_fun_rep, word) % self.m] = True

    # Check if a word belongs to the Bloom Filter
    def member(self, word):
        # your code here
        for hash_fun_rep in self.hash_fun_reps:
            if not self.bits[hash_string(hash_fun_rep, word) % self.m]:
                return False
        return True



