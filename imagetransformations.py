import cv2 as cv
import sys
import numpy as np

# reading an image 
img=cv.imread("images/ironman.png")
cv.imshow("original",img)


#translation    moving image up down left right    # https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html  documentation 
#all parallel lines in the original image will still be parallel in the output image
def translate(img, x , y):
    transmat=np.float32([[1,0,x],[0,1,x]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img, transmat , dimensions)
translated=translate(img,-100,100)
cv.imshow("translated",translated)
# -x --> left
#  x --> right
#-y --> up
# y --> down 


#rotation 
def rotate(img , angle , rotPoint= None):
    (height, width)=img.shape[:2]
    if rotPoint is None :
        rotPoint=(width//2,height//2)
    dimensions=(width, height)    
rotated= rotate(img,45)    
# positive angle is anticlockwise and other is clockwise 

cv.waitKey(0)

#resizing an image 


resized= cv.resize(img , (500,500),interpolation=cv.INTER_CUBIC )  #interpolation is a process of estimating values between known data points. # INTER_NEAREST − A nearest-neighbor interpolation.

#INTER_LINEAR − A bilinear interpolation (used by default)

#INTER_AREA − Resampling using pixel area relation. It is a preferred method for image decimation but when the image is zoomed, it is similar to the INTER_NEAREST method.

#INTER_CUBIC − A bicubic interpolation over 4x4 pixel neighborhood

#INTER_LANCZOS4 − A Lanczos interpolation over 8x8 pixel neighborhood


### flipping an image 

flipped = cv.flip(img, 0) # 0 means vertically and 1 means horizontally and -1 means both vertically and horizontally 


#cropping which is simple arrray slicing 

cropped = img[200:400 , 300:400]
cv.imshow("croppped ", cropped )
cv.waitKey(0)
