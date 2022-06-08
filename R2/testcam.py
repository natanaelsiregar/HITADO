from collections import deque
import numpy as py
import cv2
import RPi.GPIO as GPIO
import time
import socket

cap = cv2.VideoCapture(0)

#cap.set(3, 480)
#cap.set(4, 320)

_, frame = cap.read()
rows, cols, _ = frame.shape

x_medium = int(cols / 2)
center = int(cols / 2)

GPIO.setmode(GPIO.BCM)  # set pi to use pin number when referencing GPIO pins
                        # can use GPIO.setmode(GPIO.BCM) instead to use
                        # Broadcom SOC channel names
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN)
GPIO.setup(22, GPIO.IN)

GPIO.setup(18, GPIO.OUT)    # set motor kanan
GPIO.setup(23, GPIO.OUT)    # set motor

GPIO.setup(24, GPIO.OUT)    # set motor belakang
GPIO.setup(25, GPIO.OUT)    # set motor

GPIO.setup(2, GPIO.OUT)    # set motor kiri
GPIO.setup(3, GPIO.OUT)    # set motor

pwm_1a = GPIO.PWM(18, 100)  # initialize PWM on pwmPin to 100 Hz freq
pwm_1b = GPIO.PWM(23, 100)

pwm_2a = GPIO.PWM(24, 100)
pwm_2b = GPIO.PWM(25, 100)

pwm_3a = GPIO.PWM(2, 100)
pwm_3b = GPIO.PWM(3, 100)


dc = 0      # variable for setting the duty cycle
pwm_1a.start(dc)
pwm_1b.start(dc)
pwm_2a.start(dc)
pwm_2b.start(dc)
pwm_3a.start(dc)
pwm_3b.start(dc)

def maju():
    pwm_1a.ChangeDutyCycle(20)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(20)
    
def stop():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(0)
    
def kanan():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(10)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(20)
    
def kiri():
    pwm_1a.ChangeDutyCycle(30)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(10)
    pwm_3b.ChangeDutyCycle(0)

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

# #Bergerak berputar mendeteksi bola
# if x_medium < center:
# 	kiri()
# 	break
# elif x_medium > center:
#     kanan()
# 	break
# elif x_medium == center:
#     maju()
# 	break
# # 	else:
# # 		while x_medium == 0:
# # 			stop()
# # 			sleep(0.25)
# # 			break
# # 		while cv.line == None:
# # 			stop()

while False:
	stop()
	sleep(2)
	cv2.imshow("Frame", frame)

cap.release()
cv2.destroyAllWindows()