from ast import While
import cv2
import argparse
import time
import readchar

def tempo_espera():
    for count in range(5):
        print(time.ctime())
        # Prints the current time with a five second difference
        time.sleep(5)



# Abre a imagem
def main():

    # Escolha da imagem
    parser = argparse.ArgumentParser(description='Seleção da imagem')
    parser.add_argument('-ig1','--image1',type = str, required= True,
                    help='Escolha da imagem')
    parser.add_argument('-ig2','--image2',type = str, required= True,
                    help='Escolha da imagem')
    args = vars(parser.parse_args())
    image1 = args['image1'] # Imagem escolhida
    image2 = args['image2']
    image1 = cv2.imread(image1, cv2.IMREAD_COLOR) # Load an image
    image2 = cv2.imread(image2, cv2.IMREAD_COLOR) # Load an image


    while True: 
        cv2.imshow('window', image1)
        key = cv2.waitKey(3000)
        if key!=-1:
            break
        cv2.imshow('window', image2)
        key = cv2.waitKey(3000)
        if key!=-1:
            break
        

    

if __name__ == '__main__':
    main()