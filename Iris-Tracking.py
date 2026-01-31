import cv2 as cv
import random 
import mediapipe as mp

initialize = mp.solutions.holistic
holistic_model = initialize.Holistic(
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

mp_drawing = mp.solutions.drawing_utils

feed = cv.VideoCapture(0)
if not feed.isOpened():
    print("camera is not starting")
    exit()

while True:
    ret,frame = feed.read()

    if not ret:
        print("ret error")
        break

    frame = cv.resize(frame,(800,600))
    h,w,_ = frame.shape

    RGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    RGB.flags.writeable = False
    results = holistic_model.process(RGB)
    RGB.flags.writeable = True
    BGR = cv.cvtColor(RGB ,cv.COLOR_RGB2BGR)
    
    if results.face_landmarks:
        leftout = results.face_landmarks.landmark[33]
        pxlo = int(leftout.x*w)
        pylo = int(leftout.y*h)

        leftin = results.face_landmarks.landmark[133]
        pxli = int(leftin.x*w)
        pyli = int(leftin.y*h)

        pxl = int(((pxlo+pxli)/2))
        pyl = int(((pylo+pyli)/2))

        rightout = results.face_landmarks.landmark[263]
        pxro = int(rightout.x*w)
        pyro = int(rightout.y*h)

        rightin = results.face_landmarks.landmark[362]
        pxri = int(rightin.x*w)
        pyri = int(rightin.y*h)

        pxr = int(((pxro+pxri)/2))
        pyr = int(((pyro+pyri)/2))


        cv.circle(BGR, (pxr,pyr), 4, (255,0,255),-1)
        cv.circle(BGR, (pxl,pyl), 4, (255, 0, 255),-1)
        

    cv.imshow("feed",BGR)
    if cv.waitKey(1) == ord('q'):
        break
feed.release()
cv.destroyAllWindows()