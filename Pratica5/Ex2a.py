import cv2
# Abre a imagem
def main():
    #-------------
    # Initialization 
    #-------------
    image_filename = '/home/bereke/Documents/PSR/psr_22-23/Parte05/images/atlascar2.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image'
    threshold_level = 128


    #-------------
    # Execution 
    #-------------




    #-------------
    # Processing 
    #-------------
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    _, image_thresholded = cv2.threshold(image_gray, threshold_level, 255, cv2.THRESH_BINARY)




    cv2.imshow('RGB IMAGE', image_rgb)  # Display the image
    cv2.imshow('gray IMAGE', image_gray)
    cv2.waitKey(0) # wait for a key press before proceeding

    #-------------
    # Visualization 
    #-------------
    cv2.imshow('RGB IMAGE', image_rgb)  # Display the image
    cv2.imshow('gray IMAGE', image_gray)
    cv2.imshow('Threshilded IMAGE', image_thresholded)
    cv2.waitKey(0) # wait for a key press before proceeding
    #-------------
    # Termination 
    #-------------


if __name__ == '__main__':
    main()