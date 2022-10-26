#!/usr/bin/env python3
from copy import deepcopy
import cv2
# Abre a imagem
gui_image = None
def main():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        _, img = video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(30, 30)
        )
        for (x, y, w, h) in faces:
            verde = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2).copy()
            gui_image = deepcopy(verde)
            
        for (x, y, w, h) in faces:
            dst = cv2.addWeighted(img, 0.1, gui_image, 0.5, 0.0)
        
        cv2.imshow('Deteção da cara', dst)

        if cv2.waitKey(1) == ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()
        
    


if __name__ == '__main__':
    main()