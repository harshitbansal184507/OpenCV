import cv2 as cv 
import numpy as np 

# two ways to draw 


#create a blank image 
blank= np.zeros((500,500,3),dtype='uint8')  # uint8 is the data type of image  ((height, width , no. of colour channels), dtype= )

blank[:]=0,0,255  #(this will make the image red (blank one)

#to colour a portion just mention the pixels 
blank[200:300, 300:400]=0,255,0
cv.imshow("blank",blank)

#draw a rectangle 
cv.rectangle(blank,(0,0),(250,250), (255,0,0),thickness=2)  #(0,0) is the starting point and (250,250) is the ending point and the last one is colour 

# to fill the retangle 
cv.rectangle(blank,(0,0),(250,250), (255,0,0),thickness=cv.FILLED) # INSTEAD OF -1 
#OTHER WAY 
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2), (255,0,0),thickness=cv.FILLED) # this is just by doing ratios 
blank= np.zeros((500,500,3),dtype='uint8')


#draw a circle 
cv.circle(blank , (blank.shape[1]//2,blank.shape[0]//2),radius=40 ,color= (0,255,0),thickness=-1) # these can be positional arguments in the same order as well 


#draw a line 

cv.line(blank , (0,0),(blank.shape[1]//2,blank.shape[0]//2),color= (255,0,0),thickness=3)



#write text on image 


cv.putText(blank ,"hello",(blank.shape[1]//2,blank.shape[0]//2), cv.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=2,thickness=2 , color=(2,255,2))
cv.imshow("blank",blank)
cv.waitKey(0)
