
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


dog = cv2.imread("C:/Users/romas/Downloads/dog.jpg")


# In[9]:


dog1 = cv2.cvtColor(dog,cv2.COLOR_BGR2RGB)


# In[3]:


type(dog)


# In[4]:


dog


# In[5]:


dog1 = cv2.cvtColor(dog,cv2.COLOR_BGR2GRAY)


# In[6]:


edges = cv2.Canny(dog,threshold1=127,threshold2=127)


# In[8]:


plt.imshow(dog, cmap='gray')


# In[10]:


plt.imshow(dog1)


# In[11]:


plt.imshow(edges)


# In[12]:



edges1 = cv2.Canny(dog,threshold1=127,threshold2=127)


# In[14]:


plt.imshow(edges1)


# In[15]:


plt.imshow(dog)


# In[16]:


med_val = np.median(dog)


# In[17]:


med_val


# In[18]:


#Lower Threshold to either 0 or 70% of the median value whichever is greater
low = int(max(0,0.7*med_val))
#Higher Threshold to either 255 or 130% of the median value whichever is smaller
high = int(min(255,1.3*med_val))

# These values like 0.7*med_val for low and 1.3*med_val, can be changed based on trial'n'error and if the med_val of the image is low.


# In[19]:


edges2 = cv2.Canny(dog,low,high)


# In[20]:


plt.imshow(edges2)

