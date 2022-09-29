maximum_number = 9999


def isPrime(x):
    
    # <Fill the blank>
    # O valor que vem como argumento da função is prime vai ser o limite superior
    # Um numero é primo quando é divisivel por si e por 1.
    for i in range(2, x):
         # Nesse sentido no inicio verifica-se o numero é divisivel por 1
         # De seguida verifica-se caso ele é divisivel por si mesmo
         resultado = x % i
         if resultado == 0:
             # Se o modulo da divisao for igual a zero ele:
             return False
             
            
         
    return True




def main():
        print("Starting to compute prime numbers up to " + str(maximum_number))
        # Vamos Percorrer um ciclo for de 0 ate ao numero maximo nao inclusive
        for i in range(1, maximum_number+1):
            # ao entrar dentro do ciclo for ele chama a função isPrime e leva como argumento o numero correspondente ao i
            if isPrime(i):
                # Caso função isPrime retornar verdadeiro entao faz-se o seguinte printe
                print('Number ' + str(i) + ' is prime.')

            else:
                # Caso a função isPrime retornar falso entao faz-se o seguinte
                print('Number ' + str(i) + ' is not prime.')

# Para fazer o exercicio 2.2 de numero menor a 10000
# É preciso na janela de comando meter: 
# python3 Ex2.py | grep "is prime" | grep "3" |  wc -l
# Cada um dos comandos acima são sequenciais ou seja vai primeiro reproduzir o programa
# De seguida vai ver os primos 
# De seguida vai ver aqueles que tem os 3  
# E no final....


if __name__ == "__main__":
        main()