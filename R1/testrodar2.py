# import the necessary package
from collections import deque
# import numpy as py
import cv2
import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BCM)  # set pi to use pin number when referencing GPIO pins
                        # can use GPIO.setmode(GPIO.BCM) instead to use
                        # Broadcom SOC channel names
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN)
GPIO.setup(22, GPIO.IN)

GPIO.setup(18, GPIO.OUT)    # set motor
GPIO.setup(23, GPIO.OUT)    # set motor

GPIO.setup(24, GPIO.OUT)    # set motor
GPIO.setup(25, GPIO.OUT)    # set motor

GPIO.setup(17, GPIO.OUT)    # set motor
GPIO.setup(27, GPIO.OUT)    # set motor

pwm_1a = GPIO.PWM(18, 100)  # initialize PWM on pwmPin to 100 Hz freq
pwm_1b = GPIO.PWM(23, 100)  # kiri

pwm_2a = GPIO.PWM(24, 100)  # belakang
pwm_2b = GPIO.PWM(25, 100)

pwm_3a = GPIO.PWM(17, 100)   # kanan
pwm_3b = GPIO.PWM(27, 100)


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
    pwm_3a.ChangeDutyCycle(20)
    pwm_3b.ChangeDutyCycle(0)
    
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
    pwm_3a.ChangeDutyCycle(20)
    pwm_3b.ChangeDutyCycle(0)
    
def kiri():
    pwm_1a.ChangeDutyCycle(20)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(10)

def putar():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(10)
    pwm_2a.ChangeDutyCycle(10)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(10)
    pwm_3b.ChangeDutyCycle(0)
    
def geser_kanan():
    pwm_1a.ChangeDutyCycle(60)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(30)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(0)

geser_kanan()
#putar()
# time.sleep(3)
# maju()
# time.sleep(3)
# kanan()
# time.sleep(3)
# kiri()
# time.sleep(3)
# stop()