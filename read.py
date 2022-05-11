import cv2 as cv 

# Reading Images 

# img = cv.imread ( "../photos/madrid.png") 

# cv.imshow ( "New Window" , img ) 

# cv.waitKey(0) 


# Reading Videos 

capture = cv.VideoCapture("../videos/Maquire_1.mp4")

while True : 
    isTrue , frame = capture.read() 
    cv.imshow("Video", frame) 

    if ( cv.waitKey(20) & 0xFF == ord('d') ):
        break ; 

capture.release() 
cv.destroyAllWindows()

