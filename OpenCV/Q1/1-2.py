import cv2
from matplotlib import pyplot as plt

cap=cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	cv2.imshow('video', frame)

	if cv2.waitKey(1)==27:
		break

cv2.destroyAllWindows()