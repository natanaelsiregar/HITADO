import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(6, GPIO.OUT)#belkang
GPIO.setup(13, GPIO.OUT)#belakamg
GPIO.setup(19, GPIO.OUT)#kanan
GPIO.setup(26, GPIO.OUT)#kanan
GPIO.setup(20, GPIO.OUT)#kiri
GPIO.setup(21, GPIO.OUT)#kiri

pwm_left1 = GPIO.PWM(20, 100)
pwm_right1 = GPIO.PWM(21, 100)

pwm_left2 = GPIO.PWM(19, 100)
pwm_right2 = GPIO.PWM(26, 100)

pwm_left3 = GPIO.PWM(6, 100)
pwm_right3 = GPIO.PWM(13, 100)

dc = 0
pwm_left1.start(dc)
pwm_right1.start(dc)
pwm_left2.start(dc)
pwm_right2.start(dc)
pwm_left3.start(dc)
pwm_right3.start(dc)

pwm_left1.ChangeDutyCycle(0)
pwm_right1.ChangeDutyCycle(0)
pwm_left2.ChangeDutyCycle(20)
pwm_right2.ChangeDutyCycle(0)
pwm_left3.ChangeDutyCycle(0)
pwm_right3.ChangeDutyCycle(0)


#pwm_left.ChangeDutyCycle(20)
#pwm_right.ChangeDutyCycle(0)
#time.sleep(2)
#pwm_left.ChangeDutyCycle(0)
#pwm_right.ChangeDutyCycle(20)

