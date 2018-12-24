import cv2
import numpy as np 

def frame_operation(image):
    
    img=cv2.rectangle(image,(50,50),(300,300),(255,127,0),5)
    return img

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('First Image',frame_operation(frame))  #this process each frame not required but needed for applying the model

    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
