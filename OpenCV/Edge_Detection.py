import numpy as np
import cv2
def showAppleEdge():
    imgfile = 'C:\\Users\\user\\Downloads\\apple.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 170, 200)

    cv2.imshow('canny1', edge1)
    cv2.imshow('canny2', edge2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showAppleEdge()