import cv2
from matplotlib import pyplot as plt







img=cv2.imread("red.jpg")

#Grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canny=cv2.Canny(gray,100,200)
cannyinv=cv2.bitwise_not(canny)

#Simple Binary Thresholded BW image
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



#Adaptive Mean Thresholded BW image
thresh1 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

#Adaptive Gaussian Thresholded BW image
thresh2=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

blur1 = cv2.GaussianBlur(thresh1,(5,5),0)
blur2 = cv2.GaussianBlur(thresh2,(5,5),0)




#cv2.imshow('Grayscale image',gray)
#cv2.imshow('Simple Binary Thresholded BW image',thresh)
#cv2.imshow('Adaptive Mean Thresholded BW image',thresh1)
#cv2.imshow('Adaptive Gaussian Thresholded BW image',thresh2)

cv2.imshow('Adaptive mean',blur1)
cv2.imshow('Adaptive gaussian',blur2)
cv2.imshow('canny',cannyinv)

cv2.waitKey(0)
cv2.destroyAllWindows()