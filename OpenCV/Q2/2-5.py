import cv2
import numpy as np

img=cv2.imread('T.png')

rows=img.shape[0]
cols=img.shape[1]

M=np.float32([[1,0,100],[0,1,-50]])

#Rotating by 45 degrees
N=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)


dst=cv2.warpAffine(img,N,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()