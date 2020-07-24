import cv2
import numpy as np

img=cv2.imread('T.png')

rows=img.shape[0]
cols=img.shape[1]

M=np.float32([[1,0,100],[0,1,-50]])

#Changed direction of rotation and changed scale to 0.5
N=cv2.getRotationMatrix2D((cols/2,rows/2),-45,0.5)


dst=cv2.warpAffine(img,N,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()