import cv2 as cv 
import numpy as np 

# Let's load a simple image with 3 black squares 
#used in shape analysis 

img= cv.imread('images/test.png') 


gray= cv.cvtColor(img , cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny= cv.Canny(blur , 125, 175 )
contours , heirarchies  = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)   
#HERE THE CONTOUR VARIABLE STORES THE LIST REPRESENTATION OF IMAGE WHICH IS USED TO DIPLAY THE CONTOURS
# THE HEERARCHIAL VARIABLE STORES THE HEIRARCHY OF THE COTOURS LIKE , EXAMPLE THERE IS A IRCLE WITHIN A SQUARE AND
#  STUFF LIKE THAT WHICH WILL BE USEFUL IN FURTHER LECTURES 
#the second paramater is the mode of contour detection 
###RETRTREE FOR HERARCHIAL CONTOURS 
#RETR EXTERNAL FOR EXTERNAL CONTOURS 
# RETR LIST FOR ALL THE CONTOURS 

#THE THIRD ARGUMENT IS FOR THE APPROXIMATION TECHNIQUE WHICH IS BEING USED () , chain approx none does nothing and returns all the contours ,
#  chain approx simple is something which more sense since it only identifies the rquired points only for eg if there is a line it will only 
# identify its end points  
print(f'{len(contours)} contours found using canny edge detection  ')



# instead of canny edge detection we can also use thresholding 
#thresholding is basic binarisin gof the image , lik in the following example if the intensity of the pixel is below 125 then it is set to 0 
# which means black , and if it is above 255 it is set to white 
ret , thres = cv.threshold(gray, 125, 255 , cv.THRESH_BINARY)
cv.imshow("thres ", thres )
contours , heirarchies  =cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)   
print(f'{len(contours)} contours found using THRESHOLD BINARISING ')


blank = np.zeros(img.shape[:2])

cv.waitKey(0) 

