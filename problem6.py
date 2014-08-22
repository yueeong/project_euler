__author__ = 'yueeong'

'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
'''

import math

def sumOfTheSquares(n):
    sumofnumbers = 0  #initialize the sum
    for i in range(1,n+1,1):

        sumofnumbers += int(math.pow(i,2))
        #print sumofnumbers

    return sumofnumbers

def squareOfTheSum(n):
    sumofthenumbers = 0
    for i in range(1,n+1,1):
        sumofthenumbers += i
    return int(math.pow(sumofthenumbers,2))

if __name__ == "__main__":
    print  squareOfTheSum(100) - sumOfTheSquares(100)
    #print sumOfTheSquares(10)
    #print squareOfTheSum(10)