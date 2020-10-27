# ------------------------------------------------------------------------------
# Project Euler - Problem 012 - Highly divisible triangular number
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=012
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from math import *

# returns number of distinct factors of  n
def factorCount(n):

    # as only factor of 1 is 1
    if n == 1:
        return 1

    # initialising count to 2, as 1 and n are always factors of n
    factorCount = 2
    
    # only runs up to square root of n, as all factors apart from the square root
    # come in pairs, one being below and one being above the square root 
    for i in range(2, int(sqrt(n)) + 1):

        # checks if i evenly divides n
        if n % i == 0:

            # if i is the square root of n
            if i*i == n:
                factorCount += 1

            # to account for factors i & n/i
            else:
                factorCount += 2
                
    return factorCount


# returns first triangular number with more than n factors
def triangularFactors(n):

    # tracking which triangular number is currently being considered
    term = 1

    # current triangular number
    triangularNum = 1
    
    while True:
        if factorCount(triangularNum) > n:
            return triangularNum

        # incrementing to next triangular number
        term += 1
        triangularNum += term


print (triangularFactors(500))
