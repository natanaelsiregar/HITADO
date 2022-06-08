import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)#belkang
GPIO.setup(25, GPIO.OUT)#belakamg
GPIO.setup(18, GPIO.OUT)#
GPIO.setup(23, GPIO.OUT)#
GPIO.setup(17, GPIO.OUT)#kanan
GPIO.setup(27, GPIO.OUT)#kanan

pwm_left1 = GPIO.PWM(17, 100)
pwm_right1 = GPIO.PWM(27, 100)

pwm_left2 = GPIO.PWM(18, 100)
pwm_right2 = GPIO.PWM(23, 100)

pwm_left3 = GPIO.PWM(24, 100)
pwm_right3 = GPIO.PWM(25, 100)

dc = 0
pwm_left1.start(dc)
pwm_right1.start(dc)
pwm_left2.start(dc)
pwm_right2.start(dc)
pwm_left3.start(dc)
pwm_right3.start(dc)

pwm_left1.ChangeDutyCycle(0)
pwm_right1.ChangeDutyCycle(0)
pwm_left2.ChangeDutyCycle(0)
pwm_right2.ChangeDutyCycle(0)
pwm_left3.ChangeDutyCycle(0)
pwm_right3.ChangeDutyCycle(0)

#pwm_left.ChangeDutyCycle(20)
#pwm_right.ChangeDutyCycle(0)
#time.sleep(2)
#pwm_left.ChangeDutyCycle(0)
#pwm_right.ChangeDutyCycle(20)