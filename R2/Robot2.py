from collections import deque
import RPi.GPIO as GPIO
import time
import cv2
import socket
from PIL import Image, ImageFilter
import numpy as np


class Robot():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        #set motor 1
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
    
        #set motor2
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
        
        #set motor3
        GPIO.setup(22,GPIO.OUT)
        GPIO.setup(10,GPIO.OUT)
        
         #set pengiring
        GPIO.setup(13,GPIO.OUT)
        GPIO.setup(19,GPIO.OUT)
        GPIO.setup(26,GPIO.OUT)
        
        GPIO.setup(5,GPIO.OUT)
        GPIO.setup(6,GPIO.OUT)
        GPIO.setup(12,GPIO.OUT)
        
       #Initialize PWM on pwmPIN to 100 Hz frequency
        self.pwm_1a = GPIO.PWM(18, 100)
        self.pwm_1b = GPIO.PWM(23, 100)
        
        self.pwm_2a = GPIO.PWM(24, 100)
        self.pwm_2b = GPIO.PWM(25, 100)
        
        self.pwm_3a = GPIO.PWM(22, 100)
        self.pwm_3b = GPIO.PWM(10, 100)
        
        self.pwm1 = GPIO.PWM(13, 100)
        self.pwm2 = GPIO.PWM(5, 100)
        
        self.pwm_1a.start(0)
        self.pwm_1b.start(0)
        self.pwm_2a.start(0)
        self.pwm_2b.start(0)
        self.pwm_3a.start(0)
        self.pwm_3b.start(0)
        self.pwm1.start(0)
        self.pwm2.start(0)
        
        
    def get_frame_video(self):
        cap = cv2.VideoCapture(0)
        while(1):
            ret, frame = cap.read()
            if ret:
                cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
    def check(self):
        print("hello")
        self.pwm_1a.ChangeDutyCycle(90)
        self.pwm_1b.ChangeDutyCycle(0)
        self.pwm_2a.ChangeDutyCycle(90)
        self.pwm_2b.ChangeDutyCycle(0)
        self.pwm_3a.ChangeDutyCycle(90)
        self.pwm_3b.ChangeDutyCycle(0)
    
    def stop(self):
        self.pwm_1a.ChangeDutyCycle(0)
        self.pwm_1b.ChangeDutyCycle(0)
        self.pwm_2a.ChangeDutyCycle(0)
        self.pwm_2b.ChangeDutyCycle(0)
        self.pwm_3a.ChangeDutyCycle(0)
        self.pwm_3b.ChangeDutyCycle(0)
    
    def penggiring(self):
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)

        GPIO.output(12, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        self.pwm1.ChangeDutyCycle(90)
        self.pwm2.ChangeDutyCycle(90)
    
    def stop_penggiring(self):
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)

        GPIO.output(6, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)

    def stop_all(self):
        pass

R2 = Robot()
R2.get_frame_video()
#R2.stop_all()
        
