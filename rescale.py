import cv2 as cv


# THE RESIZE / RESCALE FUNCTION 
def rescaleFrame ( frame , scale = 0.5 ) : 
    width = int ( frame.shape[1] * scale ) 
    height = int ( frame.shape[0] * scale ) 
    
    dimensions = ( width , height ) 

    return cv.resize ( frame , dimensions , interpolation=cv.INTER_AREA)


# img = cv.imread("../photos/madrid.png") 
# resized_image = rescaleFrame(img)
# cv.imshow("New Image" , resized_image ) 

# cv.waitKey(0) 



# FOR VIDEOS 
capture = cv.VideoCapture("../videos/Maquire_1.mp4") ; 

while True:
    isTrue , frame = capture.read()

    resized_frame = rescaleFrame(frame , scale = 0.5) 

    cv.imshow("New Video" , resized_frame)


    if ( cv.waitKey(20) & 0xFF == ord('d') ) :
        break 


capture.release()
cv.destroyAllWindows()







