# Import the OpenCV and NumPy libraries.
import cv2
import numpy as numpy

# Loads frames from a webcam using the VideoCapture()method. The parameter 0 indicates the first webcam, and the number can change if there is more than one webcam.
# Its argument can be either the device index or the name of a video file
cap = cv2.VideoCapture(0)



# A video is just a sequence of images, and you need to loop (using a while loop) through images. Each frame from the video is read using the read() method
while True:
    
    #face characteristic files from opencv library
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    # ret is a boolean variable that returns true if the frame is available.
    # frame is an image array vector captured based on the default frames per second defined explicitly or implicitly 

    ret,frame = cap.read()
    print(frame)
    # draw a rectangle on the image frame
    # takes in parameters:
        # image object
        # Pixel cordinates of the vertex at top left
        # Pixel cordinates of the vertex at lower right
        # Color in BGR NOT RGB
        # Thickness(in pixel)

    # convert to grey color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,
    scaleFactor=1.05,
    minNeighbors=5)


    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #show the image arrays continously in a window entitled "ngecu"
    
    cv2.imshow("Ngecu",frame)

    # The waitkey() method is used to wait until you press the key
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()