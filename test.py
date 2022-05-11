from hashlib import new
import cv2 as cv
from cv2 import INTER_AREA 


def rescaleImage ( frame , scale = 0.5 ):
    width = int ( frame.shape[1] * scale ) 
    height = int ( frame.shape[0] * scale ) 

    dimensions = ( width , height ) 

    return cv.resize( frame , dimensions , interpolation=cv.INTER_AREA)




img = cv.imread ("../photos/madrid.png") ; 
new_img = rescaleImage ( img ) 
cv.imshow( "New Window" , new_img )  
cv.waitKey(0) 


