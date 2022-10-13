import cv2
# Abre a imagem
def main():

    image_filename = '/home/bereke/Documents/PSR/psr_22-23/Parte05/docs/atlascar2_multichannel_thresholded.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()