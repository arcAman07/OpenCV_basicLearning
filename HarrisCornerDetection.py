
# coding: utf-8

# In[1]:


import cv2


# In[3]:


import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


real_chess = cv2.imread("C:/Users/romas/Downloads/real_chess.jpg")


# In[8]:


type(real_chess)


# In[9]:


plt.imshow(real_chess)


# In[10]:


real_chess1 = cv2.imread("C:/Users/romas/Downloads/real_chess1.jpg")


# In[11]:


type(real_chess1)


# In[13]:


plt.imshow(real_chess1)


# In[16]:


chess_2d = cv2.imread("C:/Users/romas/Downloads/2dchess.jpg")


# In[17]:


plt.imshow(chess_2d)


# In[18]:


graychess2d = cv2.cvtColor(chess_2d,cv2.COLOR_BGR2GRAY)


# In[20]:


plt.imshow(graychess2d, cmap='gray')


# In[21]:


grayreal_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)


# In[22]:


plt.imshow(grayreal_chess, cmap='gray')


# In[23]:


graychess2d


# In[24]:


gray = np.float32(graychess2d)


# In[25]:


grayreal_chess


# In[26]:


gray_1 = np.float32(grayreal_chess) # To apply Harris corner detection all elements in the array need to be in float


# In[27]:


gray_2 = np.float32(graychess2d)


# In[28]:


flat_corners = cv2.cornerHarris(src=gray_2,blockSize=2,ksize=3,k=0.04)


# In[29]:


flat_corners = cv2.dilate(flat_corners,None)


# In[30]:


chess_2d[flat_corners>0.01*flat_corners.max()] = [255,0,0] #coloring the corners red


# In[31]:


plt.imshow(chess_2d) # the outside corners not detected as due lack of plane surface outside those corners. Hence cant decide there is a change in direction when the edges are intersecting.


# In[32]:


flat_corners1 = cv2.cornerHarris(src=gray_1,blockSize=2,ksize=3,k=0.04)


# In[33]:


flat_corners1 = cv2.dilate(flat_corners1,None)


# In[35]:


real_chess[flat_corners1>0.01*flat_corners1.max()] = [255,0,0] #coloring the corners red


# In[36]:


plt.imshow(real_chess)

