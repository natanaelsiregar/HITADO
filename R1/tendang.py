from collections import deque
import numpy as np
import imutils
import RPi.GPIO as GPIO
import cv2
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

LPWM = 20
RPWM = 21

GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(RPWM, GPIO.OUT)

L = GPIO.PWM(LPWM, 100)
R = GPIO.PWM(RPWM, 100)

L.start(0)
R.start(0)

def penendang():
    L.ChangeDutyCycle(90)
    R.ChangeDutyCycle(0)
    
def penendang_reverse():
    L.ChangeDutyCycle(0)
    R.ChangeDutyCycle(90)
    
penendang()
penendang_reverse()

# #Penggiring
# Ena, In1, In2 = 13, 19, 26
# Enb, In3, In4 = 5, 6, 12
# 
# GPIO.setup(Ena, GPIO.OUT)
# GPIO.setup(In1, GPIO.OUT)
# GPIO.setup(In2, GPIO.OUT)
# 
# GPIO.setup(Enb, GPIO.OUT)
# GPIO.setup(In3, GPIO.OUT)
# GPIO.setup(In4, GPIO.OUT)
# 
# pwm1 = GPIO.PWM(Ena, 100)
# pwm2 = GPIO.PWM(Enb, 100)
# 
# pwm1.start(0)
# pwm2.start(0)
# 
# def penggiring():
# 	GPIO.output(In1, GPIO.LOW)
# 	GPIO.output(In2, GPIO.HIGH)
# 
# 	GPIO.output(In3, GPIO.HIGH)
# 	GPIO.output(In4, GPIO.LOW)
# 	pwm1.ChangeDutyCycle(50)
# 	pwm2.ChangeDutyCycle(50)
# 
# def stop_penggiring():
# 	GPIO.output(In1, GPIO.LOW)
# 	GPIO.output(In2, GPIO.LOW)
# 
# 	GPIO.output(In3, GPIO.LOW)
# 	GPIO.output(In4, GPIO.LOW)
	
penendang()
#penggiring()

# def pasif():
#     L.ChangeDutyCycle(0)
#     R.ChangeDutyCycle(90)
# 
# def stop():
#     L.ChangeDutyCycle(0)
#     R.ChangeDutyCycle(0)
# 
# def penendang():
#     time.sleep(0.5)
#     pasif()
#     time.sleep(0.35)
#     aktif()
#     time.sleep(3)
#     stop()
#     time.sleep(0.01)
#     
# penendang()
# aktif()