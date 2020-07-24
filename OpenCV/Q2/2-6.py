import cv2
import numpy as np

img=cv2.imread('T.png')

rows=img.shape[0]
cols=img.shape[1]

M=np.float32([[1,0,100],[0,1,-50]])

pts1 = np.float32([[130,262],[134,198],[203,203]])
pts2 = np.float32([[130,262],[134,198],[168,199]])

M = cv2.getAffineTransform(pts1,pts2)

#Affine Transformation
dst = cv2.warpAffine(img,M,(cols,rows))


cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

