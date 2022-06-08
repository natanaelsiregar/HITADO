import cv2
from PIL import Image, ImageFilter
import numpy as np
cap = cv2.VideoCapture(0)
#cap.set(3, 1920)
#cap.set(4, 1080)
i = 1
ret, frame = cap.read()
while True:
    
    if ret:
        cv2.imshow('Original Image', frame)
        #cv2.imshow("asli", frame)
    #if cv2.waitKey(1) & 0xFF == ord('s'):
     #   cv2.imwrite("dataset/frame_" + str(i) + ".png", frame)
      #  i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("dataset/frame_1.png", frame)
        break
cap.release()
cv2.destroyAllWindows()


