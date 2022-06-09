from collections import deque
import numpy as np
import imutils
import RPi.GPIO as GPIO
import cv2

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

pwm_1a.ChangeDutyCycle(30)
pwm_1b.ChangeDutyCycle(0)
pwm_2a.ChangeDutyCycle(0)
pwm_2b.ChangeDutyCycle(30)
pwm_3a.ChangeDutyCycle(0)
pwm_3b.ChangeDutyCycle(0)

# camera.release()
# cv2.destroyAllWindows()