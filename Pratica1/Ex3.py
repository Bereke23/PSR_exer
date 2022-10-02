 #!/usr/bin/env python

from colorama import Fore, Back, Style  


maximum_number = 11
def isPrime(x):
    
    # <Fill the blank>
    
    for i in range(2, x):
        
         resultado = x % i         
         if resultado == 0:
            # Faz o print do divisor dos numeros nao primos, aparece acima
            # Para que na lista que estamos a dar print asseguir apareça o o numero 2 é necessario que a lista contenha mais  
            #do que o próprio elemento, nesse sentido se o unico divisor por causa do qual o 4 não é numero primo 
            # é o divisor 2 nesse sentido para ele aparecer na lista que fazemos print ele tem chegar a esse elemento e devido a isso nós adicionamos o + 1 
             print('O divisor para qual o numero ' + str(x) +  ' não é primo é' + str(list(range(2,i + 1))))           
             return False

    return True




def main():
        print("Starting to compute prime numbers up to " + str(maximum_number))
        
        for i in range(1, maximum_number+1):
     
            if isPrime(i):
                # Ao definir o Style afrente estamos a definir 
                print(Style.BRIGHT +  Fore.BLUE +   'Number ' + str(i) + ' is prime.' + Style.RESET_ALL)

            else:
               
                print(Fore.RED +    'Number ' + str(i) + ' is not prime.'  + Style.RESET_ALL)



if __name__ == "__main__":
        main()