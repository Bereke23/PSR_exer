import cv2
import argparse
# Abre a imagem
def main():
    #-------------
    # Initialization 
    #-------------
    # Escolha da imagem
    parser = argparse.ArgumentParser(description='Seleção da imagem')
    parser.add_argument('-ig','--image',type = str, required= True,
                    help='Escolha da imagem')
    args = vars(parser.parse_args())
    image = args['image'] # Imagem escolhida
    image_filename = image
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image


    #-------------
    # Execution 
    #-------------
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    centerh = int(image.shape[0]/2)
    centerw = int(image.shape[1]/2)
    radius = 50
    color = (0,255, 0)
    window_name = 'Image of a circle'
    thickness = 2
    #-------------
    # Processing 
    #-------------
    center_coordinates = (centerw, centerh)
    image = cv2.circle(image, center_coordinates, radius, color, thickness)

    #-------------
    # Visualization 
    #-------------
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    #-------------
    # Termination 
    #-------------


if __name__ == '__main__':
    main()