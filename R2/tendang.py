# import the necessary package
from collections import deque
import numpy as py
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

LPWM = 20
RPWM = 21

GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(RPWM, GPIO.OUT)

L = GPIO.PWM(LPWM, 100)
R = GPIO.PWM(RPWM, 100)

L.start(0)
R.start(0)

def aktif():
    
    L.ChangeDutyCycle(10)
    R.ChangeDutyCycle(0)

def pasif():
    L.ChangeDutyCycle(0)
    R.ChangeDutyCycle(90)

def stop():
    L.ChangeDutyCycle(0)
    R.ChangeDutyCycle(0)

def penendang():
    time.sleep(0.5)
    pasif()
    time.sleep(0.35)
    aktif()
    time.sleep(3)
    stop()
    time.sleep(0.01)

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

def penggiring():
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.HIGH)

    pwm1.ChangeDutyCycle(30)
    pwm2.ChangeDutyCycle(30)
    
penendang()
#penggiring()