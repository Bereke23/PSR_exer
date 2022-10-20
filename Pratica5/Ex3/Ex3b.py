import argparse
import cv2
from functools import partial


def onTrackbar(val,alpha_slidermax,imagegray, windowname):
    alpha_slider_max = alpha_slidermax
    vale = val
    image_gray = imagegray
    window_name = window_name
    alpha = vale / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv2.addWeighted(vale, alpha, image_gray, beta, 0.0)
    return cv2.imshow(window_name,dst)
    # Add code here to threshold image_gray and show image in window

def main():
    alpha_slidermax = 100
    # Parte da entrada do argume
    parser = argparse.ArgumentParser()
    parser.add_argument('-im', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow('window - Ex3a')

    trackbar_name = 'Alpha x %d' % alpha_slidermax
    cv2.createTrackbar(trackbar_name, 'window - Ex3a' ,0 , alpha_slidermax, onTrackbar)

    g = partial(onTrackbar,val = 0, alpha_slidermax = 100,imagegray =  image_gray)
    g(windowname = 'window - Ex3a' )
    

    # add code to create the trackbar ...
    cv2.waitKey(0)


if __name__ == '__main__':
    main()