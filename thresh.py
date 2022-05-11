import cv2 as cv 

img = cv.imread ( "../photos/11.jpg") 
img = cv.resize( img , ( 600 , 400 ) ) 
cv.imshow ( "First Image" , img  )

gray = cv.cvtColor ( img , cv.COLOR_BGR2GRAY ) 

# Simple Thresholding 
threshold , thresh = cv.threshold( gray , 150 , 255 , cv.THRESH_BINARY ) 
cv.imshow ( "Simple Thresholded" , thresh ) 

# Inverse of Thresholding value 
# threshold , thresh_inv = cv.threshold( gray , 150 , 255 , cv.THRESH_BINARY_INV ) 
# cv.imshow ( "Simple Thresholded Inverse" , thresh_inv ) 

# Adaptive Thresholding 
adaptive_thresh = cv.adaptiveThreshold( 
    gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY_INV , 
    11 , 9
)
cv.imshow ("Adaptive Thresholding" , adaptive_thresh ) 



cv.waitKey(0) 