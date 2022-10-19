import cv2
import argparse



# Abre a imagem
def main():

    # Escolha da imagem
    parser = argparse.ArgumentParser(description='Seleção da imagem')
    parser.add_argument('-ig','--image',type = str, required= True,
                    help='Escolha da imagem')
    args = vars(parser.parse_args())
    image = args['image'] # Imagem escolhida
    

    image_filename = image
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()