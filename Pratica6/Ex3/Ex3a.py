from ast import While
import cv2
# Abre a imagem
def main():
    #-------------
    # Initialization 
    #-------------

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    video = cv2.VideoCapture(0)
    #-------------
    # Execution 
    #-------------
    if not video.isOpened():
        print("Cannot open camera")
        exit()
    #-------------
    # Processing 
    #-------------
    #-------------
    # Visualization 
    #-------------

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
            verde = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), -2).copy()
        for (x, y, w, h) in faces:
            dst = cv2.addWeighted(img, 0.1, verde, 0.5, 0.0)
        
        cv2.imshow('Deteção da cara', dst)

        if cv2.waitKey(1) == ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()
        
        
        
    #-------------
    # Termination 
    #-------------


if __name__ == '__main__':
    main()