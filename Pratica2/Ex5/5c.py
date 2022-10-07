from email.headerregistry import ContentTransferEncodingHeader
from queue import Empty
from unicodedata import numeric
import readchar


def printAllCharsUpTo(stop_char):

    list = []
    print(stop_char)
    for i in range(34,stop_char+1):
        list.append(chr(i))
    print(list)

    # <to complete>

def readAllUpTo(stop_char):
    # eu quero ler de forma continua ate para no caracter X
    # caracter X corresponde ao décimal 88
    list = []
    while True:
        for i in range (stop_char, 88):
            list.append(chr(i))
            if i == 88: 
                break



# def countNumbersUpTo(stop_char):
#     list_numbers =[]
#     list_others = []
#     total_numbers = 0
#     total_others = 0
#     while True:
#         for i in range (stop_char, 88+1):
#             if chr(i).isnumeric():
#                 list_numbers.append(chr(i))
#             if chr(i) is not numeric:
#                 list_others.append(chr(i))
#         break
#     total_numbers = len(list_numbers)
#     total_others = len(list_others)
#     print('You entered ' + str(total_numbers) + ' numbers.')
#     print('You entered ' + str(total_others) + ' others.')
        
def countNumbersUpTo(stop_char):
    inputs = []
    list_numbers = []
    list_others = []
    while True:
        for i in range(stop_char,88+1):
            inputs.append(chr(i))
        break
        # add code here to create a list of inputs

    for input in inputs:
        if input.isnumeric():
            list_numbers.append(input)
        if input is not numeric:
            list_others.append(input)
        # process each input in the list
    total_index = len(list_others)
    list_index = []
    for posiçao in range(0,total_index + 1):
        list_index.append(posiçao)
    others_dictionary = dict(zip(list_index,list_others))
    # zip() permite unir duas listas numa unica so permitindo que uma seja os indixes e a outra os valores
    print(others_dictionary)


    #print(list_numbers)
    # total_numbers = len(list_numbers)
    # total_others = len(list_others)
    # print('You entered ' + str(total_numbers) + ' numbers.')
    # print('You entered ' + str(total_others) + ' others.')






def main(): 
    key = readchar.readkey()
    
    if key is not Empty:
        print('O caracter inicial ' + key)
        countNumbersUpTo(ord(key))
    



if __name__ == '__main__':
        main()