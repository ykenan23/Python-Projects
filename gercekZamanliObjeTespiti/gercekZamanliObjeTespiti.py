import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture("ucgenler.mp4")

font = cv2.FONT_HERSHEY_COMPLEX


while 1:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = 0
    ls = 0
    lv = 0
    uh = 0
    us = 0
    uv = 0

    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lower_color,upper_color)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area  = cv2.contourArea(cnt)
        
        epsilon = 0.01*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 15800:
            cv2.drawContours(frame,[approx],0,(255,255,255),9)
            
            if len(approx)==3:
                cv2.putText(frame,"Ucgen",(x,y),font,1,(255,255,255))

    cv2.imshow("frame",frame)

    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    

