class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        # (a+bi) + (c+di) = (a+c) + (b+d)i
        # addapt code to use classes

    def multiply(self, y):
        # (a+bi)(c+di) = (ac−bd) + (ad+bc)i
        # addapt code to use classes

    def __str__(self):
        
        # addapt code to use classes

def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(i = 5,r = 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c2.add(c1)
    print(c2)  # uses the __str__ method in the class