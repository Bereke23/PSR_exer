maximum_number = 100

def isPerfect(value):
    # Estamos a defenir o valor da soma de forma a começar com um valor
    soma = 0
    # <Fill the blanks>
    for x in range(1, value): 
        # Estamos a verificar  o módulo é igual ao zero de forma a saber se é um divisor
         resultado = value%x         
         if resultado < 1:
            # caso estes numeros sejam inferiores a um
              soma = soma+x
              # a variavel soma vai igualar ao valor anterior da variavel soma 
              # e ao valor dos indices atraves dos quais ele consegue fazer a divisao
              if soma==value:
                # caso a soma seja igual ao valor indicado entao ele é perfeito 
                return True
    
    return False


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number+1):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()