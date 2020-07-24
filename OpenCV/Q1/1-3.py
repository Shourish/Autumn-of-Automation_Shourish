import cv2
from matplotlib import pyplot as plt

img=cv2.imread("red.jpg")

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower=(150,70,50)
upper=(200,255,255)

mask=cv2.inRange(hsv,lower,upper)
maskinv=cv2.bitwise_not(mask,mask=None)


result=cv2.bitwise_and(img,img,mask=mask)
result2=cv2.bitwise_and(img,img,mask=maskinv)
resultinv=cv2.cvtColor(result,cv2.COLOR_BGR2RGB)
red_removed=cv2.bitwise_or(result2,resultinv,mask=None)

cv2.imshow('red_removed',red_removed)
cv2.imshow('original_image',img)


#inv=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#cv2.imshow('inv',inv)



cv2.waitKey(0)
cv2.destroyAllWindows()