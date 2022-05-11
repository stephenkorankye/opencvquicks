import cv2 as cv 
import numpy as np 


blank = np.zeros ( ( 500 , 500 , 3 ) , dtype='uint8' )
# cv.imshow ( "Blank" , blank ) 

# Paint the Image 
# blank[100:200 , 200:300] = 0 , 255 , 0 
# cv.imshow ( "New Color " , blank ) 


# Draw a Rectangle 
# cv.rectangle(blank , ( 0 , 0 ) ,  
#     ( blank.shape[1] // 2 , blank.shape[0] // 2 )  
#     , ( 0 , 255 , 0 ) , thickness=cv.FILLED)
# cv.imshow("Rectangle" , blank )

# Draw a Circle 
# cv.circle ( blank , 
#     ( blank.shape[1] // 2 , blank.shape[0] // 2 )  , 
#     40 , ( 255 , 0 , 0 ) , thickness=cv.FILLED
# )
# cv.imshow ( "Circle" , blank ) 


# Draw a line ; 
# cv.line ( blank , ( 0 , 0 ) , 
#     ( blank.shape[1] // 2 , blank.shape[0] // 2 ) , ( 255  , 255 , 255 ) , 
#     thickness=3
# )
# cv.imshow("Line" , blank) 

# Write Text 

text = "I am a Text!!!" 
cv.putText ( blank , text , ( 100 , 225 ) , 
    cv.FONT_HERSHEY_TRIPLEX , 1.0 , 
    ( 0 , 255 , 0 )  , 2 
)
cv.imshow("Text" , blank ) 



cv.waitKey(0) ; 