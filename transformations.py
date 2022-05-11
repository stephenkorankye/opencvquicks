import cv2 as cv
from cv2 import INTER_CUBIC 
import numpy as np 




img = cv.imread ( "../photos/cat2.jpg")
img = cv.resize ( img , ( 850 , 650 ))  

cv.imshow ( "New Window" , img ) 


# Translation 
def translate ( img , x , y ) :
    transMat = np.float32 ([ [1,0,x] , [0,1,y] ])
    dimensions = (img.shape[1] , img.shape[0] ) 
    return cv.warpAffine( img , transMat , dimensions ) 

# -x --> left 
# -y --> up 
# x --> right 
# y --> down 


translated = translate ( img , 100 , 100 ) 
# cv.imshow ( "Translated" , translated )


# Rotation

def rotate ( img , angle , rotPoint = None ) :
    ( height , width ) = img.shape[:2]

    if rotPoint is None :
        rotPoint = ( width // 2 , height // 2 ) 

        rotMat = cv.getRotationMatrix2D(rotPoint , angle , 1.0 )
        dimensions = ( width , height ) 

        return cv.warpAffine( img , rotMat , dimensions ) 


rotated = rotate ( img , 20 ) 
cv.imshow ( "Rotated" , rotated ) 

new_rotated = rotate ( rotated , 20 ) 
# cv.imshow ( "Rotated Again" , new_rotated)


# Resize

resized = cv.resize ( img , ( 500 , 500 ) , interpolation=INTER_CUBIC)
# cv.imshow( "Resized" , resized ) 

# Flipping 

# 0 -> Flipping Vertically 
# 1 -> Flipping Horizontally 
# -1 -> Flipping both Vertically and Horizontally 

flip = cv.flip ( img , -1 )
cv.imshow ( "Flipping" , flip )



# Cropping 
cropped = img[100:200 , 100:200] 
cv.imshow ( "Cropped" , cropped )










cv.waitKey(0) 