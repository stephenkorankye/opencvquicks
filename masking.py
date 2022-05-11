import cv2 as cv
import numpy as np 


img = cv.imread("../photos/cat2.jpg") 
img = cv.resize ( img , ( 700 , 500 ) ) 

cv.imshow ( "New Window" , img ) 

blank = np.zeros ( img.shape[:2] , dtype = 'uint8' ) 


# mask = cv.circle ( blank , 
#     (img.shape[1] // 2 , img.shape[0] // 2 ) , 100 , 255 , -1  
# )

# mask = cv.rectangle ( blank , 
#     ( img.shape[1] // 2 , img.shape[0] // 2 ) , 
#     ( img.shape[1] // 2 + 100 , img.shape[0] // 2 + 100 ) ,
#     255 , -1  
# )

# cv.imshow ( "Masked" , mask ) 



circle = cv.circle ( blank.copy() , 
    ( img.shape[1] // 2 , img.shape[0] // 2 ) , 
    100 , 255 , -1 
)

rectangle = cv.rectangle ( blank.copy() , 
    ( 30 , 30 ) , ( 370 , 370 ) , 255 , -1 
)

wierd_shape = cv.bitwise_and( circle , rectangle )

masked = cv.bitwise_and ( img , img , mask = wierd_shape ) 
cv.imshow ( "Wierd Shaped Masked Image" , masked ) 



cv.waitKey(0) 