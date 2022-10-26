#!/usr/bin/env python3
import cv2
import numpy as np

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    while(True):
        ret, frame = capture.read()
        if ret:

            # hsv is better to recognize color, convert the BGR frame to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            threshold_level_b = 50
            threshold_level_g = 100
            threshold_level_r = 150
            # in hsv red color located in two region. Create the mask for red color
            # mask the red color and get an grayscale output where red is white
            # everything else are black
            b,g,r = cv2.split(frame)
            print(frame.shape)
            cv2.imshow('b',b)
            print(b.shape)
            cv2.imshow('g',g)
            print(g.shape)
            print(r.shape)
            cv2.imshow('r',r)

            #mask1 = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))
            #mask2 = cv2.inRange(hsv, (50,50,50), (255,255,255))
            #mask = cv2.bitwise_or(mask1, mask2)

            # get the index of the white areas and make them orange in the main frame
            #for i in zip(*np.where(mask1 == 255)):
            #       frame[i[0], i[1], 0] = 0
            #      frame[i[0], i[1], 1] = 0
            #        frame[i[0], i[1], 2] = 0

            # play the new video
            #cv2.imshow(window_name,frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cv2.destroyAllWindows()

 image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image'
    threshold_level_b = 50
    threshold_level_g = 100
    threshold_level_r = 150
    #-------------
    # Execution 
    #-------------




    #-------------
    # Processing 
    #-------------
    image_b,image_g,image_r = cv2.split(image_rgb) # Estamos a separar os diversos canais existentes numa 
    #imagem a cores para em varias matrizes em vez de pertencerem apenas a uma matriz global tridimensional
    _, image_thresholded_b = cv2.threshold(image_b, threshold_level_b, 255, cv2.THRESH_BINARY)
    _, image_thresholded_g = cv2.threshold(image_g, threshold_level_g, 255, cv2.THRESH_BINARY)
    _, image_thresholded_r = cv2.threshold(image_r, threshold_level_r, 255, cv2.THRESH_BINARY)
    image_thresholded_rgb = cv2.merge((image_thresholded_b,image_thresholded_g,image_thresholded_r))
    
if __name__ == '__main__':
    main()