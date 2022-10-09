from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    print('1')
    # addapt code to use named tuples

def multiplyComplex(x, y):
    # addapt code to use named tuples
    print('1')

def printComplex(x):
    print('1')
    # addapt code to use named tuples

def main():
    
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    # Test add
    addComplex(c1, c2)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()