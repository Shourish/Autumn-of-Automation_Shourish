import cv2
import numpy as np



#start the video
cap = cv2.VideoCapture('messi.mp4')

while (cap.isOpened()):
	ret,frame = cap.read()

	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	blur = cv2.bilateralFilter(gray,9,75,75)
	#blur= cv2.blur(gray, (3, 3))
	circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,70,param1=50,param2=30,minRadius=0,maxRadius=50)


	if circles is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)



	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

