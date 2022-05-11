import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread ( "../photos/cat1.jpg") 
img = cv.resize ( img , ( 950 , 700))
cv.imshow ( "New Window" , img ) 


# # BGR to Grayscale 
# gray = cv.cvtColor ( img , cv.COLOR_BGR2GRAY ) 
# cv.imshow ( "Gray" , gray ) 

# BGR TO HSV 
hsv = cv.cvtColor ( img , cv.COLOR_BGR2HSV ) 
cv.imshow ( "HSV" , hsv ) 

# # BRR to L * A * B 
# lab = cv.cvtColor ( img , cv.COLOR_BGR2LAB ) 
# cv.imshow ( "LAB" , lab ) 

# BGR to RGB 
rgb = cv.cvtColor ( img , cv.COLOR_BGR2RGB ) 
cv.imshow ( "RGB" , rgb ) 


# HSV to BGR 
hsv_bgr = cv.cvtColor ( hsv , cv.COLOR_HSV2BGR ) 
cv.imshow ( "HSV to BGR" , hsv_bgr ) 


plt.imshow ( rgb ) 
plt.show () 


# NB CONVERTING FROM GRAYSCALE TO THE OTHERS DOES NOT HAVE A DIRECT METHOD 
# CONVERT GRASCALE TO BGR , AND THE BGR TO ANY OF THE OTHERS 


cv.waitKey(0) 
