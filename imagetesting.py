###################


#LEARNING FACE DETECTION WITH PYTHON

import cv2
import numpy as np
import matplotlib.pyplot as plt 

nadia = cv2.imread('Nadia_Murad.jpg',0)
dennis = cv2.imread('Denis_Mukwege.jpg',0)
solvay = cv2.imread('nanu.jpeg',0)
face_cascade = cv2.CascadeClassifier('E:\\Study Material\\Computer-Vision-with-Python\\DATA\\haarcascades\\haarcascade_frontalface_default.xml')


def detect_face(img):
 
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
    return face_img

result = detect_face(solvay)

plt.imshow(result,cmap='gray')
plt.show()