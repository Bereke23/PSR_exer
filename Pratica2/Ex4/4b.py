from email.headerregistry import ContentTransferEncodingHeader
from queue import Empty
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
                return False
        







def main(): 
    key = readchar.readkey()
    
    if key is not Empty:
        print('o caracter final ' + key)
        printAllCharsUpTo(ord(key)) 
        while True:
            readAllUpTo(ord(key))



if __name__ == '__main__':
        main()