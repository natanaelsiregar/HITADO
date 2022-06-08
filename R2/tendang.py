import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(4, GPIO.OUT)#right
GPIO.setup(18, GPIO.OUT)#left

pwm_left1 = GPIO.PWM(18, 100)
pwm_right1 = GPIO.PWM(4, 100)

dc = 0
pwm_left_tendang.start(dc)
pwm_right_tendang.start(dc)

pwm_left_tendang.ChangeDutyCycle(10)
pwm_right_tendang.ChangeDutyCycle(0)
time.sleep(1)
pwm_left_tendang.ChangeDutyCycle(0)
pwm_right_tendang.ChangeDutyCycle(0)


