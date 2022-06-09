# import the necessary package
from collections import deque
import numpy as py
import cv2
#import RPi.GPIO as GPIO
import time

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
    #if len(cnts) > 0:
        # find the largest contour of the mask, then use it to compute
        # the minimum enclosing circle and centroid
    c = max(cnts, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)

    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    # only proceed if the radius meets a minimum size
    #if radius > 0:
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