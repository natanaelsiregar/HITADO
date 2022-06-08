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

pwm_1a.ChangeDutyCycle(0)
pwm_1b.ChangeDutyCycle(0)
pwm_2a.ChangeDutyCycle(0)
pwm_2b.ChangeDutyCycle(0)
pwm_3a.ChangeDutyCycle(0)
pwm_3b.ChangeDutyCycle(0)

#Penggiring
Ena, In1, In2 = 13, 19, 26
Enb, In3, In4 = 5, 6, 12

GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)

pwm1 = GPIO.PWM(Ena, 100)
pwm2 = GPIO.PWM(Enb, 100)

pwm1.start(0)
pwm2.start(0)

def stop_penggiring():
	GPIO.output(In1, GPIO.LOW)
	GPIO.output(In2, GPIO.LOW)

	GPIO.output(In3, GPIO.LOW)
	GPIO.output(In4, GPIO.LOW)

stop_penggiring()

# camera.release()
# cv2.destroyAllWindows()

