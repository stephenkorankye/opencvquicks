import cv2 as cv 

img = cv.imread ( "../photos/cat3.jpg")
img = cv.resize ( img , ( 650 , 500 ) ) 
cv.imshow ( "New Window" , img ) 

# IMMA COME BACK TO YOU LATER 

cv.waitKey(0)