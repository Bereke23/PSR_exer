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





def main(): 
    key = readchar.readkey()
    
    if key is not Empty:
        print('o caracter final ' + key)
        printAllCharsUpTo(ord(key)) 
    # <to complete>






if __name__ == '__main__':
        main()