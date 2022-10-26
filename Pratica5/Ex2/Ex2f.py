import cv2
import numpy as np
# Abre a imagem
def main():
    #-------------
    # Initialization 
    #-------------
    image_filename = '/home/bereke/Documents/PSR/psr_22-23/Parte05/images/atlas2000_e_atlasmv.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image'
    #-------------
    # Execution 
    #-------------

    #-------------
    # Processing 
    #-------------

    # Green color detection
    lower_bound = np.array([0,50,0])
    upper_bound = np.array([50,256,50])
    #masking the image using inRange() function
    image_mask = cv2.inRange(image_rgb, lower_bound, upper_bound)
    image_mask = image_mask.astype(bool)
    # Paint red that  were green
    # Estamos a separar a imagem consoante o numero de chanells

    b,g,r = cv2.split(image_rgb)
    # Estamos em cada uma das imagens class resultadas
    # estou a dizer o caixote que corresponde ao image_mask
    # na imagem b sera de preto
    # enquanto na imagem r sera branco

    b[image_mask]= 0  # defenir como preto
    g[image_mask] = 0 # defenir como preto
    r[image_mask] = 255 # defenir como branco

    image_rgb = cv2.merge((b,g,r))
    
    #-------------
    # Visualization 
    #-------------
    # Resoult of comaundigng
    cv2.imshow('Mask Image r ', r)
    cv2.imshow('Tresh RGB', image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding
    #-------------
    # Termination 
    #-------------


if __name__ == '__main__':
    main()