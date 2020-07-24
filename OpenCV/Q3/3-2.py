import cv2
from matplotlib import pyplot as plt

cap=cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	thresh1 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

	blur1 = cv2.GaussianBlur(thresh1,(5,5),0)



	canny=cv2.Canny(frame,100,200)
	cannyinv=cv2.bitwise_not(canny)

	cv2.imshow('Adaptive mean',blur1)

	cv2.imshow('canny',cannyinv)


	


	if cv2.waitKey(1)==27:
		break

cv2.destroyAllWindows()