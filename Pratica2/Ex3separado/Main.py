#!/usr/bin/env python3
import argparse # importing every function of the library argoarse

from Function import isPerfect


# Neste caso estamos a importar tudo, não só somente a função isPerfect
import Function





def main():
    #maximum_number = 2 # maximum number to test.
    #O que esta libraria nos faz, é especificar um determinado argumento 
    parser = argparse.ArgumentParser(description='Test for PSR.')
    parser.add_argument('--maximum_number', type=int, required= True ,
                    help='The maximum number until witch we check if number is perfect ')
    # o Vars converte the arguments in to a special format
    args = vars(parser.parse_args())
    print(args)
    maximum_number = args['maximum_number']








    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for number in range(2, maximum_number):
        if isPerfect(number):
            print('Number ' + str(number) + ' is perfect.')
        else:
            print('Number ' + str(number) + ' is not perfect ' )    

if __name__ == "__main__":
    main()