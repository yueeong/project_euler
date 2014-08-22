__author__ = 'yueeong'

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