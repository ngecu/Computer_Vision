import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture('images/video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
