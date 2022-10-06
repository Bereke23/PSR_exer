import time
import math 
from colorama import Fore, Back, Style
limite_maximo = 50000000

def tic(começo):
    inicio = time.time()  
    return inicio
    

def toc(conta):
    ls =[]
    for i in range(0,limite_maximo +1):
        ls.append(math.sqrt(i))
    fim = time.time()
   # print(ls)
    return fim



def main():
    começo = tic(1)
    acabar = toc(1)
    intervalo = acabar - começo
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("This is Ex1 and current date is " + Back.YELLOW + local_time + Style.RESET_ALL )
    print(intervalo)	

# Esta é sempre chamada no inicio do orograma
if __name__ == "__main__":
    main()
