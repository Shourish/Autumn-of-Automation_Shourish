import cv2
import numpy as np

img=cv2.imread('T.png')

#Bilateral Filtering (Edges are preserved while removing other noises)
blur = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('img',blur)
cv2.waitKey(0)