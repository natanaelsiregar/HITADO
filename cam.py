import cv2
import numpy as np
# import RPi.GPIO as GPIO
from time import sleep

cap = cv2.VideoCapture(2)

#cap.set(3, 480)
#cap.set(4, 320)

_, frame = cap.read()
rows, cols, _ = frame.shape

x_medium = int(cols / 2)
center = int(cols / 2)

while True:
	_, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#red color
	low_red = np.array([0, 176, 25])
	high_red = np.array([64, 255, 255])
	red_mask = cv2.inRange(hsv_frame, low_red, high_red)
	contours, _  = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

	for cnt in contours:
		(x, y, w, h) = cv2.boundingRect(cnt)

		x_medium = int((x + x + w) / 2)
		break

	cv2.line(frame, (x_medium, 0), (x_medium, 720), (0, 255, 0), 2)

	cv2.imshow("Frame", frame)

	key = cv2.waitKey(1)

	if key == ord("q"):
		break

def maju():

def kanan():

def kiri():


# 	#Bergerak berputar mendeteksi bola
# 	if x_medium < center:
# 		while x_medium < center:
# 			putar_kiri()
# 			sleep(0.25)
# 			maju()
# 			sleep(0.25)
# 			stop()
# 			break
# 	elif x_medium > center:
# 		while x_medium > center:
# 			putar_kanan()
# 			sleep(0.25)
# 			maju()
# 			sleep(0.25)
# 			stop()
# 			break
# 	elif x_medium == center:
# 		while x_medium == center:
# 			maju()
# 			sleep(0.25)
# 			break
# 	else:
# 		while x_medium == 0:
# 			stop()
# 			sleep(0.25)
# 			break
# 		while cv.line == None:
# 			stop()

# while False:
# 	stop()

#sleep(2)
	cv2.imshow("Frame", frame)

cap.release()
cv2.destroyAllWindows()