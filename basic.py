from email import iterators
import cv2 as cv
from cv2 import INTER_CUBIC 


def rescaleImage ( frame , scaleX = 0.6 , scaleY = 0.5 ) :
    width = int ( frame.shape[1] * scaleX ) 
    height = int ( frame.shape[0] * scaleY ) 

    dimensions = ( width , height ) 
    return cv.resize ( frame , dimensions , interpolation=cv.INTER_AREA)





img = cv.imread ( "../photos/cat1.jpg") 
img = rescaleImage ( img ) 

cv.imshow ( "Original" , img ) 

# Converting to Grayscale 
gray = cv.cvtColor ( img , cv.COLOR_BGR2GRAY )
# cv.imshow ( "GrayScale" , gray ) 

# Blur 
blur = cv.GaussianBlur(img , (7 , 7) , cv.BORDER_DEFAULT ) 
# cv.imshow ( "Blur" , blur ) 

# Edge Cascade 
canny = cv.Canny ( blur , 125 , 175 ) 
# cv.imshow ( "Canny" , canny )


# Dilating the Image 
dilated = cv.dilate ( canny , ( 7 , 7 ) , iterations=2)
# cv.imshow ( "Dilated" , dilated ) 

eroded = cv.erode ( dilated , ( 3 , 3 ) , iterations = 1 ) 
# cv.imshow ( "Eroded" , eroded ) 


# Resize 
resized = cv.resize ( img , ( 500 , 400 ) , interpolation=INTER_CUBIC) 
cv.imshow ( "Resized " , resized )


# Cropping 
cropped = img[50:200 , 200:400] 
cv.imshow ( "Cropped" , cropped) 



cv.waitKey(0) 