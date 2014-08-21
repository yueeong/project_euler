__author__ = 'yueeong'
import math

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def primetester(number):
    numberToCountUpTo = int(math.ceil(math.sqrt(number)))

    startingnumber = 3
    if number == 2 :
        return True
    if number % 2 == 0:
        #print "divisible by 2"
        return False
    for i in range(startingnumber,numberToCountUpTo+1,1):
        if number % i == 0 :
            #print "divisible by : " + str(i)
            return False
        elif i == numberToCountUpTo :
            return True
    #print "i hit the last true"
    return True

def primefinder(nthprime):
    count = 1
    primetotest = 2


    while count <= nthprime:
        #print "Testing : " + str(primetotest)
        if primetester(primetotest) == True :

            #print str(count) + " :  " + str(primetotest)
            if count == nthprime:
                print "the {}th prime is {}".format(nthprime,primetotest)
            count += 1


        primetotest += 1



#print primetester(25)

primefinder(600)

