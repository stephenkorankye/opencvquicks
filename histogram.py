import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np  

img = cv.imread ( "../photos/cat3.jpg")
img = cv.resize ( img , ( 700 , 500 ) ) 

cv.imshow ( "New Window" , img ) 

blank = np.zeros ( img.shape[:2] , dtype = 'uint8' ) 


gray = cv.cvtColor ( img , cv.COLOR_BGR2GRAY ) 
# cv.imshow ( "Gray" , gray )  


mask = cv.circle ( blank , (
    img.shape[1] // 2 , img.shape[0] // 2
) , 100 , 255 , -1)


masked = cv.bitwise_and ( gray , gray , mask = mask )
cv.imshow ( "Masked" , masked ) 


# GrayScale histogram 
# gray_hist = cv.calcHist ([gray] , [0] , None , [256] , [0 , 256 ] ) 

# plt.figure() 
# plt.title ( "GrayScale Histogram") 
# plt.xlabel ( "Bins" ) 
# plt.ylabel ( "# of pixels" ) 
# plt.plot ( gray_hist ) 
# plt.xlim ( [0,256])
# plt.show() 


# Color Histogram 

plt.figure() 
plt.title ( "Color  Histogram") 
plt.xlabel ( "Bins" ) 
plt.ylabel ( "# of pixels" ) 


colors = ('b' , 'g' , 'r' ) 
for i , col in enumerate ( colors ) :
    hist = cv.calcHist ([img] , [i] , None , [256] , [0,256] )
    plt.plot ( hist , color = col ) 
    plt.xlim ( [0 , 256])

plt.show()


cv.waitKey(0)