import numpy as np
import cv2
def showApple():
    imgfile = 'C:\\Users\\user\\Downloads\\apple.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.imshow('apple', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showApple()