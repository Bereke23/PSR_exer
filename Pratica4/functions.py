import argparse
from operator import truediv
import readchar
from queue import Empty
import time
import math 
from colorama import Fore, Back, Style
import random
from collections import namedtuple

#Variaveis gerais usadas
Tempo_maximo = 10
init = time.time()
fin = 0


Inputs = namedtuple('Input', ['requested', 'received','duration'])


def argumentosetrada():
    # Definição dos argumentos de entrada:
    parser = argparse.ArgumentParser(description='Modo de funcionamento')
    parser.add_argument('-utm','--use_time_mode', action='store_true' ,
                    help='Max number of secs for time mode or maximum number os inputs mode.')
    parser.add_argument('-mv','--max_value',type = int, required= True,
                    help='Max number of secs for time mode or maximum number os inputs mode.')
    args = vars(parser.parse_args())
    valor_max = args['max_value']
    temporizador = args['use_time_mode']
    print(args)
    teclainicial(valor_max,temporizador)
    

def teclainicial(numero_maximo, temporizador):
    # Definição da parte inicial do teste:
    seconds = time.time()
    local_time = time.ctime(seconds)
    print(Fore.BLUE + "PARI" + Style.RESET_ALL + " Typing Test, Grupo 6," + local_time + Style.RESET_ALL ) 
    if temporizador:
        print("Test runnig up to " + str(Tempo_maximo) + "s")
    else:
        print("Test runnig up to " + str(numero_maximo) + " inputs" )
    print("Press any key to star the test")
    key = readchar.readkey()
    if key is not Empty:
        modofuncionamento(numero_maximo,temporizador)
    

def modofuncionamento(numero_maximo,temporizador):
    # Escolha do tipo do funcionamento:
    letras_mostradas = []
    letras_escolhidas = []
    types = []
    if temporizador:
        inicio = time.time()
        intervalo = 0
        while intervalo < Tempo_maximo:
            i1 = time.time()
            randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
            print("Type letter " + randomLowerLetter)
            
            tecla = readchar.readkey()
            if randomLowerLetter == tecla:
                print('The key pressed ' + Fore.GREEN + tecla + Style.RESET_ALL)
            else:
                print('The key pressed ' + Fore.RED+ tecla + Style.RESET_ALL)
            if tecla == chr(32) :
                exit(0)
            fim = time.time()
            intervalo = fim - inicio
            f1 = time.time()
            inte1= f1 - i1
            types.append(Inputs(randomLowerLetter, tecla,inte1)) 
        print(types)
        print( "Current test duration " + "(" + str(intervalo)+ ")" + " exceeds maximum of 10")
        Terminiodeseccao()
    else:
        for letras in range(1,numero_maximo+1):
            randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
            print("Type letter " + randomLowerLetter)
            tecla = readchar.readkey()
            if randomLowerLetter == tecla:
                print('The key pressed ' + Fore.GREEN + str(tecla) + Style.RESET_ALL)
            else:
                print('The key pressed ' + Fore.RED+ str(tecla) + Style.RESET_ALL)
            if tecla == chr(32) :
                exit(0)
        Terminiodeseccao()


def Terminiodeseccao():
    fin = time.time()
    Duraçao = fin - init
    #print( "Current test duration " + str(Duraçao)+ "s")
    print(Fore.BLUE + "Test finished!!" + Style.RESET_ALL)
