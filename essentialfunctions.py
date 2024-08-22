import cv2 as cv 
import numpy as np 


# making a image grayscale 
img= cv.imread("images/test.png")
cv.imshow("original",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#blurring an image 
blur=cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT ) # (3,3) is kernel size 


#how to do edge cascade (edge detection)
canny=cv.Canny(img,125,175)


#here we apply the canny edge detection on the blurred image so that minute edges are not detected 
canny2=cv.Canny(blur,125,175)
cv.imshow("edge detection",canny2)


cv.waitKey(0)

#dilating an image (which is adding pixels to the boundry of an image )
dilated= cv.dilate(canny2 ,(7,7),iterations=3)

# eroding an image (direct opposite of dilating , that is thinning out pixels of boundry of an image)
erode= cv.erode(canny2 ,(7,7),iterations=3)


#resizing (using cv.resize)

resized=(img,(400,400))


#image cropping 
cropped=img[50:200,200:400]  # 50 to 199 rows and 200 to 399 columns  just list slicing 

