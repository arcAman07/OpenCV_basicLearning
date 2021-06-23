
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


chess = cv2.imread("C:/Users/romas/Downloads/2dchess.jpg")


# In[3]:


type(chess)


# In[4]:


plt.imshow(chess)


# In[5]:


graychess = cv2.cvtColor(chess,cv2.COLOR_BGR2GRAY)


# In[6]:


result,corners = cv2.findChessboardCorners(chess,(7,7))


# In[7]:


result


# In[8]:


corners


# In[9]:


cv2.drawChessboardCorners(chess,(7,7),corners,result)


# In[10]:


plt.imshow(chess)


# In[ ]:


#Other similar grid functions are:


# In[ ]:


# 1) Detecting circles in a image: cv2.findCirclesGrid() function and then draw it on the image using drawChessboardCorners() function

