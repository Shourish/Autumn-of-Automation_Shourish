import cv2
import numpy as np

img=cv2.imread('T.png')

#Gaussian Blurring to remove noise
blur = cv2.GaussianBlur(img,(5,5),0)


cv2.imshow('img',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()