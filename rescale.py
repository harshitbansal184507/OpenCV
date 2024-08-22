import cv2 as cv
import sys

# rescaling function 
def rescale(img , scale = 0.75): # works with all types of images , vidoe and live video 
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(img,dimensions, interpolation=cv.INTER_AREA)
# reading an image 
img=cv.imread("images/ironman.png")
cv.waitKey(10)

if img is None:
    sys.exit("Could not read the image.") # if image coukld not be read 


#cv.imshow("Display window", img) 


img2=rescale(img)
#cv.imshow("rescaled image", img2)
cv.waitKey(1000)
# recaling video with the same function
video=cv.VideoCapture(0)    # intance of video frame  # 0 here means the camera , else we need to give the filepath 
while True :
    isTrue , frame = video.read()
    frame2=rescale(frame)
    cv.imshow('Video',frame)
    cv.imshow('Videorescaled',frame2)
    if(cv.waitKey(20) & 0xFF==ord("d")):
        break 
video.release()
cv.destroyAllWindows()    

def changeres(width , height): # works only with live video and doesn't work with standalone images and videos 
    video.set(3,width)
    video.set(4,height)