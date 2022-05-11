from multiprocessing.connection import wait
import cv2 as cv 
import numpy as np 

img = cv.imread ( "../photos/cat1.jpg") 
img = cv.resize ( img , ( 950 , 700))
cv.imshow ( "New Window" , img ) 

blank = np.zeros(img.shape[:2] , dtype ='uint8' ) 

b , g , r = cv.split ( img ) 

blue = cv.merge ( [b , blank , blank ])
green = cv.merge ([ blank , g , blank ])
red = cv.merge ( [blank , blank , r ])

cv.imshow ( "Blue" , blue ) 
cv.imshow ( "Green" , green ) 
cv.imshow ( "Red" , red ) 

print ( img.shape ) 
print ( b.shape ) 
print ( g.shape ) 
print ( r.shape ) 


merge = cv.merge ([ b , g , r ])
cv.imshow ( "Merged Image " , merge ) 




cv.waitKey(0) 
