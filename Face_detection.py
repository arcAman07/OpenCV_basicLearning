
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


nadia = cv2.imread("C:/Users/romas/Documents/Open_cv model/Computer-Vision-with-Python/DATA/Nadia_Murad.jpg")


# In[3]:


type(nadia)


# In[4]:


plt.imshow(nadia)


# In[5]:


graynadia = cv2.cvtColor(nadia,cv2.COLOR_BGR2GRAY)


# In[6]:


plt.imshow(graynadia,cmap='gray')


# In[7]:


solvay = cv2.imread("C:/Users/romas/Documents/Open_cv model/Computer-Vision-with-Python/DATA/solvay_conference.jpg")


# In[8]:


type(solvay)


# In[9]:


plt.imshow(solvay)


# In[10]:


graysolvay = cv2.cvtColor(solvay,cv2.COLOR_BGR2GRAY)


# In[11]:


plt.imshow(graysolvay,cmap='gray')


# In[12]:


face_cascade=cv2.CascadeClassifier("C:/Users/romas/Documents/Open_cv model/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_frontalface_default.xml")


# In[13]:


denis = cv2.imread("C:/Users/romas/Documents/Open_cv model/Computer-Vision-with-Python/DATA/Denis_Mukwege.jpg")


# In[14]:


type(denis)


# In[15]:


plt.imshow(denis)


# In[16]:


graydenis = cv2.cvtColor(denis,cv2.COLOR_BGR2GRAY)


# In[17]:


plt.imshow(graydenis,cmap='gray')


# In[18]:


def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)
    
    for(x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),thickness=5)
        return face_img


# In[19]:


result1 = detect_face(graynadia)


# In[20]:


plt.imshow(result1,cmap='gray')


# In[21]:


result2 = detect_face(denis)


# In[22]:


result3 = detect_face(solvay)


# In[23]:


plt.imshow(result2,cmap='gray')


# In[24]:


plt.imshow(result3,cmap='gray')


# In[25]:


cap = cv2.VideoCapture(0)


# In[26]:


while True:
    res,frame = cap.read()
    result4 = detect_face(frame)
    cv2.imshow('Video Face detect',result4)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

