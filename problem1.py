__author__ = 'yueeong'





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