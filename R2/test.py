import cv2
import cvlib as cv

im = cv2.imread("people.jpeg")
im2 = cv2.resize(im, (640,480))

x,y,z = cv.detect_common_objects(im2)

print(y)

cv2.imshow("Image", im2)
cv2.waitKey(0)
cv2.destroyAllWindows()
