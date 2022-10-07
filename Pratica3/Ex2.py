def addComplex(x, y):
    # add code here ...

def multiplyComplex(x, y):
    # add code here ...

def printComplex(x):
    # add code here ...

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()