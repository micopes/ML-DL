import numpy as np
import cv2
def showAppleRed():
    imgfile = 'C:\\Users\\user\\Downloads\\apple.jpg'
    img = cv2.imread(imgfile, cv2. IMREAD_COLOR)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([-10, 100, 100])
    upper_red = np.array([15, 255, 255])

    mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
    res = cv2.bitwise_and(img, img, mask=mask_red)

    cv2.imshow('apple_red', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


showAppleRed()