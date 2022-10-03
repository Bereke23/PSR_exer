#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to print hello world!
# --------------------------------------------------

maximum_number = 50 # maximum number to test.


def getDividers(value):
    dividers = []
    for i in range(1,value):
            # estamos a usar o modulo para retornar o resto da divisao inteira
            # Este ciclo for vai percorer varias vezes ate ao numero i ser igual a valor - 1
            # E em cada ciclo vai fazer o seguinte:
            if value%i == 0:
                # Caso a condição do if seja possitiva vai executar o abaixo
                # append vai basicamente adicionar um determinado elemento a lista
                dividers.append(i)
                print('Este numero ('+ str(i) + ') é um divisor de '+ str(value))



    # Este printe só vai ocorrer apos o ciclo for ter sido percorrido
    print(str(value) + ' tem os seguinte divisores ' + str(dividers))
    # Esta função após o print anterior vai fornecer a lista de valores divisores, sendo estes divisores apenas quando o modulo é igual a 0
    return dividers



def isPerfect(value):
    divisorespossiveis = getDividers(value)
    # Vamos somar todos os elementos da lista e obtemos apenas um elemento
    total = sum(divisorespossiveis)
    if total == value:
     return True
    else:
        return False