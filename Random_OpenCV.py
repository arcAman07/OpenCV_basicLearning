
# coding: utf-8

# In[1]:


#Used to create a Taskbar in the overlay of the image displayed

import cv2 as cv
def trackbar(x):
    text = f'Trackbar: {x}' #trackbar callback function
    cv.displayOverlay('window', text, 1000)
    cv.imshow('window', img)
img = cv.imread("C:/Users/romas/Downloads/margot.jpg", cv.IMREAD_COLOR)
cv.imshow('window', img)
cv.createTrackbar('x', 'window', 100, 255, trackbar)
if cv.waitKey(10) & 0xFF == ord('q'):
    cv.destroyAllWindows()


# In[3]:


import cv2 as cv
import numpy as np
def rgb(x):
    r = cv.getTrackbarPos('red','window')
    g = cv.getTrackbarPos('green','window')
    b = cv.getTrackbarPos('blue','window')
    img[:] = [b, g, r]
    cv.displayOverlay('window', f'Red={r}, Green={g}, Blue={b}')
    cv.imshow('window', img)
img = np.zeros((100, 600, 3), 'uint8')
cv.imshow('window', img)
cv.createTrackbar('red', 'window', 200, 255, rgb)
cv.createTrackbar('green', 'window', 50, 255, rgb)
cv.createTrackbar('blue', 'window', 100, 255, rgb)
rgb(0)
cv.waitKey(0)
cv.destroyAllWindows()
#Used to create taskbars of different colors so that we can see them mixing in different proportions and see the required output

