__author__ = 'yueeong'


def fiboevensummer():
    fibolist = [1,2,3]  #initial start
    evensum = 2

    maxval = 0
    count = 2  #start to append
    while maxval < 4000000:
        maxval = fibolist[count] + fibolist[count-1]
        fibolist.append(maxval)
        print maxval
        if maxval % 2 == 0 & maxval < 4000000:
            evensum += maxval
        count += 1

    print evensum







fiboevensummer()