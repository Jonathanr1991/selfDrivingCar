import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('stop_sign.xml')
video_capture = cv2.VideoCapture(1)

while(1):
    ret,img = video_capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow ('img',img)
    k=cv2.waitKey(30) & 0xff
    if k== 27:
        break

cv.destroyAllWindows()
