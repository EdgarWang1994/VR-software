'''
Created on 17 May 2018

@author: Edgar
'''
import numpy as np 
import cv2 
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    scaled = cv2.resize(frame,(800,800))
    # Display the resulting frame
    cv2.imshow('frame',scaled)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()













