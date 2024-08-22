
import cv2 as cv 


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 


eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml') 

cap = cv.VideoCapture(0) 

while True: 

	
	ret, img = cap.read() # reads frames from a camera 
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 	# Detects faces of different sizes in the input image 


	for (x,y,w,h) in faces: 
		# To draw a rectangle in a face 
		cv.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
		roi_gray = gray[y:y+h, x:x+w] 
		roi_color = img[y:y+h, x:x+w] 

		eyes = eye_cascade.detectMultiScale(roi_gray) 

		#To draw a rectangle in eyes 
		for (ex,ey,ew,eh) in eyes: 
			cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),3) 

	cv.imshow('img',img) 

	
	k = cv.waitKey(30) & 0xff
	if k == 27: 
		break

cap.release() # Close the window 

# De-allocate any associated memory usage 
cv.destroyAllWindows() 
