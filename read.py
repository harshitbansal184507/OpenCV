import cv2 as cv
import sys

# reading an image 
img=cv.imread("images/ironman.png")
cv.waitKey(10)

if img is None:
    sys.exit("Could not read the image.") # if image coukld not be read 


cv.imshow("Display window", img) #these arguments are necessary , first is name of the header of the display window and secodn is the instance of the image 
print(type(img)) # type is numpy array 
print(img)
k = cv.waitKey(0)


#reading a video 
video=cv.VideoCapture(0)    # intance of video frame  # 0 here means the camera , else we need to give the filepath 
while True :
    isTrue , frame = video.read()
    cv.imshow('Video',frame)
    
    if(cv.waitKey(20) & 0xFF==ord("d")):
        break 
video.release()
cv.destroyAllWindows()    
print("jai gurudev")