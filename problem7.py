__author__ = 'yueeong'
import math


def primetester(number):
    numberToCountUpTo = int(math.ceil(math.sqrt(number)))
    #print numberToCountUpTo
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

            #print str(count) + " : YES " + str(primetotest)
            if count == nthprime:
                print "the 10001th prime is {}".format(primetotest)
            count += 1


        primetotest += 1



#print primetester(25)

primefinder(10001)

