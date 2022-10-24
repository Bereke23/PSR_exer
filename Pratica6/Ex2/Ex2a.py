#!/usr/bin/env python3
import cv2

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    _, image = capture.read()  # get an image from the camera

    # add code to show acquired image
    cv2.imshow(window_name,image)

    cv2.waitKey(0)
    capture.release()
    cv2.destroyAllWindows()
    # add code to wait for a key press

if __name__ == '__main__':
    main()