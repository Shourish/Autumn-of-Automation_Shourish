import cv2
import numpy as np

img=cv2.imread('T.png')

rows=img.shape[0]
cols=img.shape[1]

M=np.float32([[1,0,100],[0,1,-50]])

#Changed centre of rotation
N=cv2.getRotationMatrix2D((50+cols/2,100+rows/2),45,1)


dst=cv2.warpAffine(img,N,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()