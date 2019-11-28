# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:39:17 2019

@author: vaibhav
"""
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
tim =float(time.time())
tim_10=tim+10

while tim_10>tim:
  ret, frame = cap.read()

    # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
  cv2.imshow('frame',frame)
  cv2.imshow('frame',gray)
  
  #cv2.imshow('frame',gray)
  if cv2.waitKey(2) & 0xFF == ord('q'):
        break  

# When everything done, release the capture
cap.release()
#exit(0)
cv2.destroyAllWindows()
