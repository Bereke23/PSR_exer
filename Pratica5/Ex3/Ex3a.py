import argparse
import cv2

# Global variables
alpha_slider_max = 100
image_gray = None
window_name = 'window - Ex3a'



def onTrackbar(threshold):
    alpha = threshold / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv2.addWeighted(threshold, alpha, image_gray, beta, 0.0)
    cv2.imshow(window_name, dst)
    # Add code here to threshold image_gray and show image in window

def main():
    # Parte da entrada do argume
    parser = argparse.ArgumentParser()
    parser.add_argument('-im', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    cv2.imshow('Imagem',image)
    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.imshow('Imagem cinzenta original',image_gray)
    cv2.namedWindow(window_name)
    

    trackbar_name = 'Alpha x %d' % alpha_slider_max
    cv2.createTrackbar(trackbar_name, window_name , 0, alpha_slider_max, onTrackbar)
    onTrackbar(0)

    # add code to create the trackbar ...
    cv2.waitKey(0)

if __name__ == '__main__':
    main()