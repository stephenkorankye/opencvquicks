import cv2 as cv 
import numpy as np 

img = cv.imread ( "../photos/cat1.jpg")
img = cv.resize ( img , ( 950 , 750 ) )

cv.imshow ( "New Window" , img ) 


blank = np.zeros ( img.shape , dtype = 'uint8')
# cv.imshow ( "" , blank ) 

gray = cv.cvtColor( img , cv.COLOR_BGR2GRAY ) 
# cv.imshow ( "" , gray )

# blur = cv.GaussianBlur ( gray , ( 5 , 5 ) , cv.BORDER_DEFAULT ) 

# canny = cv.Canny ( blur ,  125 , 175  ) 
# cv.imshow ( "Canny Edges" , canny ) 



ret , thresh = cv.threshold ( gray , 125 , 255 , cv.THRESH_BINARY ) 
cv.imshow ( "Thresh" , thresh )


contours , hierarchies = cv.findContours(thresh , cv.RETR_LIST , cv.CHAIN_APPROX_NONE ) 
print ( f'{len(contours)} contour(s) found' )

cv.drawContours(blank , contours , -1 , ( 0 , 0 , 255) , 2 )
cv.imshow ( "Contours Drawn" , blank )  



cv.waitKey(0) 