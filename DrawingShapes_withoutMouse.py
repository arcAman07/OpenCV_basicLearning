
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)


# In[4]:


blank_img.shape


# In[15]:


#Drawing shapes on the images


# In[5]:


plt.imshow(blank_img)


# In[6]:


cv2.rectangle(blank_img,pt1=(150,0),pt2=(450,300),color=(0,0,255),thickness=5)


# In[7]:


plt.imshow(blank_img)


# In[8]:


cv2.circle(blank_img,center=(200,400),radius=150,color=(255,0,0),thickness=4)


# In[9]:


plt.imshow(blank_img)


# In[10]:


cv2.circle(blank_img,center=(50,100),radius=60,color=(0,255,0),thickness=-1)


# In[11]:


plt.imshow(blank_img)


# In[12]:


cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(100,100,100),thickness=3)


# In[13]:


plt.imshow(blank_img)


# In[20]:


blank_img2 = np.zeros((1000,1000,3),dtype = np.int16)


# In[21]:


#Writing on Images


# In[26]:


font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(blank_img2,text='I am Aman',org=(10,500),fontFace=font,fontScale=4,color=(0,0,255),thickness=4,lineType=cv2.LINE_AA)


# In[27]:


plt.imshow(blank_img2)


# In[28]:


#drawing shapes where all 4 vertices are known


# In[29]:


vertices = np.array([[200,900],[800,900],[200,300],[800,300]],dtype=np.int32)


# In[30]:


vertices.shape


# In[31]:


#To incorporate shapes with vertices on the images we have to reshape the vertices array into the three dimensional(3 dimensional like tensor which the image comprises of)


# In[37]:


pts = vertices.reshape((-1,1,2))


# In[38]:


pts.shape


# In[39]:


pts


# In[41]:


cv2.polylines(blank_img2,[pts],isClosed=True,color=(255,0,0),thickness=5)


# In[42]:


plt.imshow(blank_img2)

