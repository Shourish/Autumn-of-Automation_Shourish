import cv2
import numpy as np

img=cv2.imread("shapes2.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)


contours,hierarchy=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



for i in range(0,len(contours)):
    cnt=contours[i]
    
    if cv2.contourArea(cnt)>1000 and cv2.contourArea(cnt)<100000 :

        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(img,(cx,cy),5,[0,255,0],-1)

        epsilon = 0.01*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        
        print(len(approx))

        img=cv2.drawContours(img,contours,i,(0,255,0),2)

        
        x,y,w,h = cv2.boundingRect(cnt)

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        if len(approx)==3:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'Triangle',(x,y+h+15), font, 0.5,(255,0,0),1,cv2.LINE_AA)
        if len(approx)==4:

            if w==h and w*h-cv2.contourArea(cnt)<0.1*w*h:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,'Square',(x,y+h+15), font, 0.5,(255,0,0),1,cv2.LINE_AA)
            if w!=h and w*h-cv2.contourArea(cnt)<0.1*w*h:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,'Rectangle',(x,y+h+15), font, 0.5,(255,0,0),1,cv2.LINE_AA)
            if w*h-cv2.contourArea(cnt)>0.1*w*h:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,'Rhombus',(x,y+h+15), font, 0.5,(255,0,0),1,cv2.LINE_AA)      
        if len(approx)>5:
            if w==h:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,'Circle',(x,y+h+15), font, 0.5,(255,0,0),1,cv2.LINE_AA)
            if w!=h:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,'Ellipse',(x,y+h+15), font, 0.5,(255,0,0),1,cv2.LINE_AA)




        #rect = cv2.minAreaRect(cnt)
        #box = cv2.boxPoints(rect)
        #box = np.int0(box)
        #img = cv2.drawContours(img,[box],0,(0,0,255),2)


cv2.imshow('image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()


    

