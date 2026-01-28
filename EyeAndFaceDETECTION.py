import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
face = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
if not cap.isOpened():
    print("Unable to Start Camera")
    exit()
while True:
    ret,frame = cap.read()

    if not ret:
        print("ret error")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)
    eyes = eye.detectMultiScale(gray,1.3,5)
    
    if len(eyes)>2:
        eyes = eyes[0:2]

    for (x,y,w,h) in faces:
        cv.rectangle(gray,(x,y),((x+w),(y+h)),(0,255,0),2)
        a = int((x+(x+w))/2)
        b = int((y+(y+h))/2)
        cv.circle(gray,(a,b),6,(0,255,0),-1)

    for (x,y,w,h) in eyes:
        cv.rectangle(gray,(x,y),((x+w),(y+h)),(0,255,0),2)
        a = int((x+(x+w))/2)
        b = int((y+(y+h))/2)
        cv.circle(gray,(a,b),6,(0,255,0),-1)
    
    cv.imshow('Live Feed',gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()