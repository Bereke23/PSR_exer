#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to print hello world!
# --------------------------------------------------


# Neste caso estamos apenas a importar a função isperfect
from My_functions import isPerfect


# Neste caso estamos a importar tudo, não só somente a função isPerfect
import My_functions

maximum_number = 50 # maximum number to test.



def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for number in range(2, maximum_number):
        if isPerfect(number):
            print('Number ' + str(number) + ' is perfect.')
        else:
            print('Number ' + str(number) + ' is not perfect ' )    


if __name__ == "__main__":
    main()