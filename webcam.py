# CREATE VIRTUAL ENVIRON
# --py -m venv env
# ACTIAVTE VIRUAL ENVIRON
# -- env\Scripts\activate
# INSTALL OPEN CV
# Import Open cv
import cv2

#To capture a video, you need to create a VideoCapture object. 
#Its argument can be either the device index or the name of a video file. 
#A device index is just the number to specify which camera. 
#Normally one camera will be connected (as in my case). 
#So I simply pass 0 (or -1). You can select the second camera by passing 1 and so on. After that, you can capture frame-by-frame.
#But at the end, don't forget to release the capture. 
cap = cv2.VideoCapture(0)

while True:    
    # Load the cascade
    
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    #This code initiates an infinite loop (to be broken later by a break statement), where we have ret and frame being defined as the cap.read(). 
    #Basically, ret is a boolean regarding whether or not there was a return at all, at the frame is each frame that is returned. 
    #If there is no frame, you wont get an error, you will get None
    
    ret,frame = cap.read()
    #Here, we define a new variable, gray, as the frame, converted to gray. 
    #Notice this says BGR2GRAY. 
    #It is important to note that OpenCV reads colors as BGR (Blue Green Red), where most computer applications read as RGB (Red Green Blue).
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #detect face
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
    
    #corner coordinates
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    #Notice that, despite being a video stream, we still use imshow. 
    #Here, we're showing the converted-to-gray feed. If you wish to show both at the same time, you can do imshow for the original frame, and imshow for the gray and two windows will appear.
    cv2.imshow("Ngecu",frame)
    
   #Basically, if we get a key, and that key is a q, we will exit the while loop with a break, which then runs:
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
