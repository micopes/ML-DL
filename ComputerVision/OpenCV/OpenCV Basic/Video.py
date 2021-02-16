import numpy as np
import cv2
def showVideo():
    try:
        cap = cv2.VideoCapture('C:\\Users\\user\\Downloads\\video.mp4')
        # cap = cv2.VideoCapture('video.mp4')
    except:
        return
    cap.set(3, 480)
    cap.set(4, 320)
    while True:
        ret, frame = cap.read()


        if not ret:
            break
        k = cv2.waitKey(1) & 0xFF

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('video', gray)


        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

showVideo()