
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import cv2


# In[3]:


img = cv2.imread("C:/Users/romas/Downloads/margot.jpg")


# In[4]:


type(img)


# In[5]:


img.shape


# In[6]:


plt.imshow(img)


# In[7]:


new_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[8]:


plt.imshow(new_img)


# In[9]:


img_gray = cv2.imread("C:/Users/romas/Downloads/margot.jpg",cv2.IMREAD_GRAYSCALE)


# In[10]:


img_gray


# In[11]:


plt.imshow(img_gray, cmap='gray')


# In[12]:


img_gray.shape


# In[13]:


new_img = cv2.resize(new_img,(800,1000))


# In[14]:


plt.imshow(new_img)


# In[15]:


w_ratio = 1
h_ratio = 1


# In[16]:


new_img = cv2.resize(new_img,(0,0),new_img,w_ratio,h_ratio)


# In[17]:


plt.imshow(new_img)


# In[18]:


new_img = cv2.flip(new_img,0)


# In[19]:


plt.imshow(new_img)


# In[20]:


new_img = cv2.flip(new_img,0)


# In[21]:


plt.imshow(new_img)


# In[22]:


cv2.imwrite("brandnew_img.jpg",new_img)


# In[23]:


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.imshow(img_gray)


# In[ ]:


cv2.imshow('Margot',new_img)
cv2.waitKey()


# In[24]:


while True:
    cv2.imshow('Robbie',new_img)
    if cv2.waitKey(1) & 0xFF ==27:
        break
cv2.destroyAllWindows()

