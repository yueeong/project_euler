__author__ = 'yueeong'


'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

UPPERLIMIT = 20

def tester(number):
    #print "\ntesting " + str(number)
    for i in range(1,UPPERLIMIT+1,1):
        if number % i == 0:
            #print str(number) + " is divisible by " +str(i)
            if i == UPPERLIMIT:
                print(str(number) + " is IT!")
                return True
            else:
                continue

        elif number % i != 0:
            #print str(number) + " not divisible by " +str(i) + " fail"
            return False

def calculate() :
    largestnum = 2520
    while tester(largestnum) is False:
        largestnum +=2520




calculate()