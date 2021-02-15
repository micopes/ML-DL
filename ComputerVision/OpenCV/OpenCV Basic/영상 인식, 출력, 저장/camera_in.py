import sys
import cv2

cap = cv2.VideoCapture('vtest.avi')

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # edge 검출하는 것
    edge = cv2.Canny(frame, 50, 150)
    
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
