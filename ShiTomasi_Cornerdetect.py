
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


flatchess = cv2.imread("C:/Users/romas/Downloads/2dchess.jpg")


# In[3]:


type(flatchess)


# In[4]:


realchess = cv2.imread("C:/Users/romas/Downloads/real_chess.jpg")


# In[5]:


realchess1 = cv2.cvtColor(realchess,cv2.COLOR_BGR2GRAY)


# In[6]:


flatchess1 = cv2.cvtColor(flatchess,cv2.COLOR_BGR2GRAY)


# In[7]:


plt.imshow(realchess1,cmap='gray')


# In[8]:


plt.imshow(flatchess1)


# In[9]:


realcorners = cv2.goodFeaturesToTrack(realchess1,64,0.01,10)


# In[10]:


flatcorners = cv2.goodFeaturesToTrack(flatchess1,49,0.01,10)


# In[11]:


flatcorners


# In[12]:


realcorners


# In[13]:


flatcorners1 = np.int0(flatcorners)


# In[14]:


realcorners1 = np.int0(realcorners)


# In[15]:


for i in flatcorners1:
    x,y = i.ravel()
    cv2.circle(flatchess,(x,y),3,color=[255,0,0],thickness=-1)


# In[16]:


plt.imshow(flatchess)


# In[17]:


for i in realcorners1:
    a,b = i.ravel()
    cv2.circle(realchess,(a,b),3,color=[255,0,0],thickness=-1)


# In[18]:


plt.imshow(realchess)

