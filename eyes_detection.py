
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


eyes = cv2.CascadeClassifier("C:/Users/romas/Documents/Open_cv model/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_eye.xml")


# In[3]:


def eye_detect(img):
    eye_img = img.copy()
    eyes_rects = eyes.detectMultiScale(eye_img)
    for(x,y,w,h) in eyes_rects:
        cv2.rectangle(eye_img,(x,y),(x+w,y+h),(255,255,255),thickness=3)
    return eye_img
    


# In[4]:


cap = cv2.VideoCapture(0)


# In[5]:


while True:
    res,frame = cap.read()
    frame = eye_detect(frame)
    cv2.imshow('Video Face detect',frame)
    k = cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()

