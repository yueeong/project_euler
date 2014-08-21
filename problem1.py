__author__ = 'yueeong'


'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


UPPERLIMIT = 1000


def allinone():
    sum = 0
    therange = range(1,UPPERLIMIT,1)
    for i in therange:
        if i%3 == 0:
            sum += i
        elif i%5 == 0 :
            sum += i
    return sum

def main():

    print "refactor : " +  str(allinone())


if __name__ == "__main__":
    main()