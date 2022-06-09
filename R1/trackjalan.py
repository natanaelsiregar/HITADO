from collections import deque
import numpy as py
import cv2
import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)    # set motor
GPIO.setup(23, GPIO.OUT)    # set motor

GPIO.setup(24, GPIO.OUT)    # set motor
GPIO.setup(25, GPIO.OUT)    # set motor

GPIO.setup(17, GPIO.OUT)    # set motor
GPIO.setup(27, GPIO.OUT)    # set motor

pwm_1a = GPIO.PWM(18, 100)  # initialize PWM on pwmPin to 100 Hz freq
pwm_1b = GPIO.PWM(23, 100)

pwm_2a = GPIO.PWM(24, 100)
pwm_2b = GPIO.PWM(25, 100)

pwm_3a = GPIO.PWM(17, 100)
pwm_3b = GPIO.PWM(27, 100)


dc = 0      # variable for setting the duty cycle
pwm_1a.start(dc)
pwm_1b.start(dc)
pwm_2a.start(dc)
pwm_2b.start(dc)
pwm_3a.start(dc)
pwm_3b.start(dc)

# orangeLower = (0, 91, 45)
# orangeUpper = (37, 255, 255)
# 
# camera = cv2.VideoCapture(0)
# position = 90
# while True:
#     (grabbed, frame) = camera.read()
# 
#     frame = imutils.resize(frame, width=720)
#     blurred = cv2.GaussianBlur(frame, (11, 11), 0)
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 
#     mask = cv2.inRange(hsv, orangeLower, orangeUpper)
#     mask = cv2.erode(mask, None, iterations=2)
#     mask = cv2.dilate(mask, None, iterations=2)
# 
#     cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     center = None
# 
#     if len(cnts) > 0:
#         c = max(cnts, key=cv2.contourArea)
#         ((x, y), radius) = cv2.minEnclosingCircle(c)
# 
#         M = cv2.moments(c)
#         center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
# 
#         if radius > 10:
#             cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
#             cv2.circle(frame, center, 5, (0, 0, 255), -1)
# 
#         if x < 170:
#             position += 1
#         elif x > 230:
#             position -= 1
#         print(radius)
# 
#     if position > 119:
#         position = 120
#     elif position < 1:
#         position = 0
#         
#     print(position)
# 
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Mask", mask)
# 
#     key = cv2.waitKey(1) & 0xFF
#     
#     if key == ord("q"):
#         break
# 
# camera.release()
# cv2.destroyAllWindows()

# def deteksi_warna_orange():
#     cap = cv2.VideoCapture(0)
#     _, frame  = cap.read()
#     rows, cols, _ = frame.shape
# 
#     x_medium = int(cols / 2)
#     center = int(cols / 2)
#     #nilai = 1
# 
#     while True:#nilai == 1:
#         _, frame = cap.read()
#         hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         
#         #orange color
#         orange_low = (0, 176, 25)
#         orange_high = (64, 255, 255)
#         red_mask = cv2.inRange(hsv_frame, orange_low, orange_high)
#         _, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
#         
#         for cnt in contours:
#             (x, y, w, h) = cv2.boundingRect(cnt)
#             
#             x_medium = int((x + x + w) / 2)
#             break
#         
#         cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
#         
#         cv2.imshow("Frame", frame)
#         cv2.imshow("mask", red_mask)
#         
#         key = cv2.waitKey(1)
#         
#         if key == ord("q"):
#             break
#         
#         #Move robot
#         while x_medium < center:
#             print("Kiri", x_medium)
#             print(center)
#             pwm_1a.ChangeDutyCycle(0)
#             pwm_1b.ChangeDutyCycle(0)
#             pwm_2a.ChangeDutyCycle(0)
#             pwm_2b.ChangeDutyCycle(0)
#             pwm_3a.ChangeDutyCycle(0)
#             pwm_3b.ChangeDutyCycle(10)
#             break
#         while x_medium > center:
#             print("Kanan", x_medium)
#             pwm_1a.ChangeDutyCycle(10)
#             pwm_1b.ChangeDutyCycle(0)
#             pwm_2a.ChangeDutyCycle(0)
#             pwm_2b.ChangeDutyCycle(0)
#             pwm_3a.ChangeDutyCycle(0)
#             pwm_3b.ChangeDutyCycle(0)
#             print(center)
#             break
#         if x_medium > (center-5) and x_medium < (center+5):
#             print("stop", x_medium)
#             print(center)
#             print("Mengoper")
#             pwm_1a.ChangeDutyCycle(10)
#             pwm_1b.ChangeDutyCycle(0)
#             pwm_2a.ChangeDutyCycle(0)
#             pwm_2b.ChangeDutyCycle(0)
#             pwm_3a.ChangeDutyCycle(0)
#             pwm_3b.ChangeDutyCycle(10)
#             break
#     while False:
#         print("putar kiri")
#         break
#     
#     cap.release()
#     cv2.destroyAllWindows()
# 
# deteksi_warna_orange()



# define the lower and upper boundaries of the "yellow"
# ball in the HSV color space then initialize the list of tracked points
orange_low = (0, 176, 25)
orange_high = (64, 255, 255)
pts = deque(maxlen=20)

cap = cv2.VideoCapture(0)
cap.set(3, 640)     # set width of the frame
cap.set(4, 480)     # set height of the frame
central_x = 320

# allow the camera or video file to warm up

# keep looping
while True:
    # grab the current frame
    ret, frame = cap.read()

    # blur it and convert it to the HSV color space
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "green", then perform a series
    # of dilations and erosions to remove any small blobs left in the mask
    mask = cv2.inRange(hsv, orange_low, orange_high)
    mask = cv2.erode(mask, None, iterations=4)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour of the mask, then use it to compute
        # the minimum enclosing circle and centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 0:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 4)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            x_ball = int(x)
            y_ball = int(y)

    # update the points queue
    pts.appendleft(center)
    key = cv2.waitKey(1) & 0xFF

    # show the frame to our screen
    cv2.imshow("Frame", frame)
    cv2.imshow("Hasil HSV", mask)

    print("x, y", x_ball, y_ball)
    print("radius bola", radius)
    if x_ball < 200:
        print("kiri")
    elif x_ball > 500:
        print("kanan")
    elif x_ball >= 200 and x_ball <= 500:
        print("Robot Maju")

while False:
    to_right()

GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()