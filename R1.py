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

def gerak_garis():
    while True:
        sensor=GPIO.input(4)
        while sensor==1:
            kanan()
            print("BLACK")
            time.sleep(0.1)
            break
            #sleep(0.1)
        if sensor==0:
            stop_motor()
            print("WHITE")
            time.sleep(0.1)
            putar_kiri_awal()
            time.sleep(0.7)
            maju_motor_awal()
            time.sleep(3.5)
            stop_motor()
            time.sleep(0.1)

            break

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
	GPIO.output(In1, GPIO.LOW)
	GPIO.output(In2, GPIO.HIGH)

	GPIO.output(In3, GPIO.LOW)
	GPIO.output(In4, GPIO.HIGH)
	pwm1.ChangeDutyCycle(30)
	pwm2.ChangeDutyCycle(30)

def stop_penggiring():
	GPIO.output(In1, GPIO.LOW)
	GPIO.output(In2, GPIO.LOW)

	GPIO.output(In3, GPIO.LOW)
	GPIO.output(In4, GPIO.LOW)
	#pwm1.ChangeDutyCycle(50)
	#pwm2.ChangeDutyCycle(50)


def maju_motor():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(20)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(20)
    pwm_3b.ChangeDutyCycle(0)

def maju_motor_awal():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(35)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(35)
    pwm_3b.ChangeDutyCycle(0)


    # GPIO.cleanup()    # wait .05 sec at current LED brightness
    # time.sleep(0.5)

def mundur_motor():
    pwm_1a.ChangeDutyCycle(40)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(40)

def stop_motor():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(0)

def putar_kanan():
    pwm_1a.ChangeDutyCycle(7)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(7)
    pwm_3a.ChangeDutyCycle(7)
    pwm_3b.ChangeDutyCycle(0)

def min_putar_kanan():
    pwm_1a.ChangeDutyCycle(6)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(6)
    pwm_3a.ChangeDutyCycle(6)
    pwm_3b.ChangeDutyCycle(0)

def putar_kiri():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(7)
    pwm_2a.ChangeDutyCycle(7)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(7)

def min_putar_kiri():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(6)
    pwm_2a.ChangeDutyCycle(6)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(6)

def putar_kiri_awal():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(10)
    pwm_2a.ChangeDutyCycle(10)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(10)

def max_putar_kiri():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(20)
    pwm_2a.ChangeDutyCycle(20)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(20)

def max_putar_kanan():
    pwm_1a.ChangeDutyCycle(20)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(20)
    pwm_3a.ChangeDutyCycle(20)
    pwm_3b.ChangeDutyCycle(0)

def putar_kanan_awal():
    pwm_1a.ChangeDutyCycle(10)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(10)
    pwm_3a.ChangeDutyCycle(10)
    pwm_3b.ChangeDutyCycle(0)

def kanan():
    pwm_1a.ChangeDutyCycle(3)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(30)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(32)
    pwm_3b.ChangeDutyCycle(0)

def kiri():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(7)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(30)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(30)
    
def Gerak2():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(12)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(50)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(30)

def Gerak3():
    putar_kiri_awal()
    time.sleep(2.5)
    mundur_motor()
    time.sleep(1.15)
    stop_motor()
    time.sleep(0.1)

def Gerak2_kick_off_kiri():
    putar_kiri_awal()
    time.sleep(1.3)
    stop_motor()
    time.sleep(0.1)

def Gerak3_kick_off_kiri():
    pass

def Gerak_ke_gawang():
    putar_kiri_awal()
    time.sleep(1.4)
    maju_maju_motor()
    time.sleep(4)
    stop_motor()
    time.sleep(0.1)


def deteksi_warna_orange():
    cap = cv2.VideoCapture(0)
    _, frame  = cap.read()
    rows, cols, _ = frame.shape

    x_medium = int(cols / 2)
    center = int(cols / 2)
    #nilai = 1

    while True:#nilai == 1:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #orange color
        orange_low = (0, 176, 25)
        orange_high = (64, 255, 255)
        red_mask = cv2.inRange(hsv_frame, orange_low, orange_high)
        _, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
        
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            
            x_medium = int((x + x + w) / 2)
            break
        
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        
        cv2.imshow("Frame", frame)
        cv2.imshow("mask", red_mask)
        
        key = cv2.waitKey(1)
        
        if key == 27:
            break
        
        #Move robot
        while x_medium < center:
            penggiring()
            putar_kiri()
            print("Kiri", x_medium)
            print(center)
            break
        while x_medium > center:
            penggiring()
            putar_kanan()
            print("Kanan", x_medium)
            print(center)
            break
        if x_medium > (center-5) and x_medium < (center+5):
            stop_motor()
            print("stop", x_medium)
            print(center)
            print("Mengoper")
            break
    while False:
        putar_kiri()
        print("putar kiri")
        break
        
    cap.release()
    cv2.destroyAllWindows()


def deteksi_kawan():
    cap = cv2.VideoCapture(0)
    _, frame  = cap.read()
    rows, cols, _ = frame.shape

    x_medium = int(cols / 2)
    center = int(cols / 2)
    #nilai = 1

    while True:#nilai == 1:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #red color
        low_red = py.array([110, 110, 100])
        high_red = py.array([130, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        _, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
        
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            
            x_medium = int((x + x + w) / 2)
            break
        
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        
        cv2.imshow("Frame", frame)
        cv2.imshow("mask", red_mask)
        
        key = cv2.waitKey(1)
        
        if key == 27:
            break
        
        #Move robot
        while x_medium < center:
            penggiring()
            putar_kiri()
            print("Kiri", x_medium)
            print(center)
            break
        while x_medium > center:
            penggiring()
            putar_kanan()
            print("Kanan", x_medium)
            print(center)
            break
        if x_medium > (center-5) and x_medium < (center+5):
            stop_motor()
            print("stop", x_medium)
            print(center)
            print("Mengoper")
            break
    while False:
        putar_kiri()
        print("putar kiri")
        break
        
    cap.release()
    cv2.destroyAllWindows()



def deteksi_bola():
    orange_low = (0, 176, 25)
    orange_high = (64, 255, 255)
    pts = deque(maxlen=20)

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)     # set width of the frame
    cap.set(4, 480)     # set height of the frame
    central_x = 320

    # allow the camera or video file to warm up

    # keep looping
    while True:
        # grab the current frame
        ret, frame = cap.read()

        # blur it and convert it to the HSV color space
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # construct a mask for the color "green", then perform a series
        # of dilations and erosions to remove any small blobs left in the mask
        mask = cv2.inRange(hsv, orange_low, orange_high)
        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and initialize the current (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[1]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour of the mask, then use it to compute
            # the minimum enclosing circle and centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size
            if radius > 0:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 4)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                x_ball = int(x)
                y_ball = int(y)

        # update the points queue
        pts.appendleft(center)
        key = cv2.waitKey(1) & 0xFF

        # show the frame to our screen
        cv2.imshow("Frame", frame)
        cv2.imshow("Hasil HSV", mask)

        print("x, y", x_ball, y_ball)
        print("radius bola", radius)

        while y_ball < 410:
           # maju_motor()
            while x_ball > 310:
                  min_putar_kanan()
                  break
            while x_ball < 290:
                  min_putar_kiri()
                  break
            break
        while (x_ball > 300 and x_ball < 360):
            maju_motor()
            penggiring()
            break

        if y_ball >= 477:
            stop_motor()
            penggiring()
            break

    while False:
        stop_motor()

    #GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    

def kirim_terima_pesan():
    
    msgFromClient       = "Hello Server"

    bytesToSend         = str.encode(msgFromClient)

    serverAddressPort   = ("192.168.43.244", 20001)

    bufferSize          = 1024

     

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

     

    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

     

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

     

    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)

def terima_kirim_pesan():
    localIP = "192.168.43.119"
    localPort = 20001
    bufferSize = 1024

    msgFromServer = "Hello UDP Client"
    bytesToSend = str.encode(msgFromServer)

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip

    UDPServerSocket.bind((localIP, localPort))

     

    print("UDP server up and listening")

     

    # Listen for incoming datagrams

    if(True):

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientMsg)
        print(clientIP)

       

        # Sending a reply to client

        UDPServerSocket.sendto(bytesToSend, address)

def kick_of_kanan():
    #terima_kirim_pesan()
    #gerak_garis()
    #time.sleep(0.2)
    #deteksi_bola()
    #deteksi_kawan()
    #stop_penggiring()
    #kirim_terima_pesan()
    #terima_kirim_pesan()
    penendang()
    kirim_terima_pesan()
    Gerak2()
    time.sleep(1.7)
    maju_motor()
    time.sleep(0.3)
    putar_kanan()
    time.sleep(1.5)
    stop_motor()
    time.sleep(0.1)
    penggiring()
    kirim_terima_pesan()
    terima_kirim_pesan()
    deteksi_warna_orange()
    kirim_terima_pesan()
    terima_kirim_pesan()
    stop_penggiring()
    Gerak3()
    kirim_terima_pesan()
    terima_kirim_pesan()
    deteksi_kawan()
    stop_penggiring()
    penendang()
    kirim_terima_pesan()
    
def kick_off_kiri():
    gerak_garis()
    mundur_motor()
    time.sleep(1.2)
    stop_motor()
    time.sleep(0.001)
    penggiring()
    terima_kirim_pesan()
    deteksi_warna_orange()
    kirim_terima_pesan()
    terima_kirim_pesan()
    putar_kiri_awal()
    time.sleep(1.8)
    maju_motor_awal()
    time.sleep(0.4)
    stop_motor()
    time.sleep(0.01)
    kirim_terima_pesan()
    deteksi_kawan()
    kirim_terima_pesan()
    terima_kirim_pesan()
    stop_penggiring()
    penendang()
    kirim_terima_pesan()
    putar_kanan_awal()
    time.sleep(1.6)
    kiri()
    time.sleep(2.3)
    maju_motor_awal()
    time.sleep(0.3)
    stop_motor()
    time.sleep(0.01)
    terima_kirim_pesan()
    deteksi_warna_orange()
    kirim_terima_pesan()
    terima_kirim_pesan()
    putar_kiri_awal()
    time.sleep(4.3)
    maju_motor_awal()
    time.sleep(4)
    stop_motor()
    time.sleep(0.01)
    stop_penggiring()
    penendang()
    
    
    
    #terima_kirim_pesan()
    #deteksi_kawan()
    #kirim_terima_pesan()
    #terima_kirim_pesan()
    #penendang()
    #kirim_terima_pesan()
    #kiri()
    #time.sleep(2.5)
    #maju_motor_awal()
    #time.sleep(0.7)
    #stop_motor()
    #time.sleep(0.01)
    #kirim_terima_pesan()
    #terima_kirim_pesan()
    #deteksi_warna_orange()
    #kirim_terima_pesan()
    #terima_kirim_pesan()
    #putar_kiri_awal()
    #time.sleep(1)
    #maju_motor_awal()
    #time.sleep(4)
    #stop_motor()
    #time.sleep(0.01)
    #penendang()

def corner_kick_kanan():
    max_putar_kiri()
    time.sleep(1.4)
    maju_motor_awal()
    time.sleep(2.3)
    stop_motor()
    time.sleep(0.01)
    putar_kiri_awal()
    time.sleep(1)
    deteksi_warna_orange()
    kirim_terima_pesan()
    terima_kirim_pesan()
    max_putar_kanan()
    time.sleep(1.2)
    stop_motor()
    time.sleep(0.001)
    terima_kirim_pesan()
    deteksi_kawan()
    kirim_terima_pesan()
    terima_kirim_pesan()
    penendang()
    kirim_terima_pesan()


n = 2
try:
    while n < 3:
        kick_of_kanan()
        n += 2
except KeyboardInterrupt:
    stop_motor()
finally:
    GPIO.cleanup()
    cv2.destroyAllWindows()
terima_kirim_pesan()
stop_motor()

    #cap.release()
#corner_kick_kanan()
#penendang()
#penggiring()
#kick_of_kanan()
#kick_off_kiri()
"""kiri()
time.sleep(2.5)
maju_motor_awal()
time.sleep(0.7)
stop_motor()
time.sleep(0.1)"""
