
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def divisorGenerator(upperlimit):
    for i in range(upperlimit):
        yield i



def main():
    for n in divisorGenerator(10):
        print(n)


if __name__ == '__main__':
    main()
