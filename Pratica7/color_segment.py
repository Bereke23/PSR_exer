#!/usr/bin/env python3
from ast import Pass
import cv2
import numpy as np
alpha_slider_max = 255


def Rmin():
    Pass
def Rmax():
    Pass
def Gmin():
    Pass
def Gmax():
    Pass
def Bmin():
    Pass
def Bmax():
    Pass


def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_original = 'Janela de video real'
    window_segment = 'Janela de parametrização'
    cv2.namedWindow(window_original,cv2.WINDOW_AUTOSIZE)
    trackbar_name = 'Alpha x %d' % alpha_slider_max
    while True:
        ret, image_rgb = capture.read()  # get an image from the camera

        if ret:
             # add code to show acquired image
            cv2.createTrackbar('Rmin ( %d' % alpha_slider_max + ')', window_segment , 0, alpha_slider_max, Rmin)
            cv2.createTrackbar('Rmax ( %d' % alpha_slider_max  + ')', window_segment , 0, alpha_slider_max, Rmax)
            cv2.createTrackbar('Gmin ( %d' % alpha_slider_max  + ')', window_segment , 0, alpha_slider_max, Gmin)
            cv2.createTrackbar('Gmax ( %d' % alpha_slider_max  + ')', window_segment , 0, alpha_slider_max, Gmax)
            cv2.createTrackbar('Bmin ( %d' % alpha_slider_max  + ')', window_segment , 0, alpha_slider_max, Bmin)
            cv2.createTrackbar('Bmax ( %d' % alpha_slider_max  + ')', window_segment , 0, alpha_slider_max, Bmax)
        
            lower_bound = np.array([10, 100, 20])
            upper_bound = np.array([25, 255, 255])
            #masking the image using inRange() function
            image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
            image_hsv_mask = cv2.inRange(image_hsv,lower_bound, upper_bound)
        
        cv2.imshow(window_original,image_rgb)
        cv2.imshow(window_segment,image_hsv_mask )

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
        # add code to wait for a key press
    capture.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    main()