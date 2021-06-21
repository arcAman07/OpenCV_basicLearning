
# coding: utf-8

# In[1]:


import cv2

cap = cv2.VideoCapture(0)

#CallBack Function Rectangle

def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2,topLeft_clicked,botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        if topLeft_clicked == True & botRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            botRight_clicked = False
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True



# Introducing the variables

pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

#Connect to the callback

cap = cv2.VideoCapture(0)

cv2.namedWindow('StarBoy')
cv2.setMouseCallback('StarBoy',draw_rectangle)

while True:

    res,frame = cap.read()
    frame = cv2.flip(frame, 1)

    #Drawing on the video based on the global variables
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(255,0,0),thickness=-1)

    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame,pt1,pt2,color=(0,0,255),thickness=4)

    cv2.imshow('StarBoy',frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

