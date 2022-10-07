from re import A


class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        # (a+bi) + (c+di) = (a+c) + (b+d)i
        self.r += y.r
        self.i += y.i
        
        
        # addapt code to use classes

    def multiply(self, y):
        # (a+bi)(c+di) = (ac−bd) + (ad+bc)i
        self.r = ((self.r * y.r) - (self.i * y.i))
        self.i = ((self.r * y.i) + (self.i * y.r))
        # addapt code to use classes

    def __str__(self):
        text = ' Numero complexo' + str(self.r)  + ' + ' + str(self.i) + 'i'
        return text
        # addapt code to use classes

def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5,3)  # use order when not naming
    c2 = Complex(7, -2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    #test add para c2
    print(c2)  # uses the __str__ method in the class
    c2.add(c1)
    print(c2)  # uses the __str__ method in the class
    

    # teste multiplicao para c1
    print(c2)  # uses the __str__ method in the class
    c2.multiply(c1)
    print(c2)


if __name__ == "__main__":
    main()