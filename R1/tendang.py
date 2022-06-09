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

# GPIO.setup(4, GPIO.IN)
# GPIO.setup(22, GPIO.IN)

LPWM = 20
RPWM = 21

GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(RPWM, GPIO.OUT)

L = GPIO.PWM(LPWM, 100)
R = GPIO.PWM(RPWM, 100)

L.start(0)
R.start(0)

def aktif():
    L.ChangeDutyCycle(90)
    R.ChangeDutyCycle(0)

def balik():
    L.ChangeDutyCycle(0)
    R.ChangeDutyCycle(90)
    
def pasif():
    L.ChangeDutyCycle(0)
    R.ChangeDutyCycle(10)

def stop():
    L.ChangeDutyCycle(0)
    R.ChangeDutyCycle(0)

def penendang():
    time.sleep(0.5)
    pasif()
    time.sleep(0.35)
    aktif()
    #time.sleep(3)
    stop()
    #time.sleep(0.01)
 
# penendang()
#aktif()
#balik()
stop()
#balik()