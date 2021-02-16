import matplotlib.pyplot as plt
import sys
import cv2

imgBGR = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
if imgBGR is None:
    print("Image load failed")
    sys.exit()

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)    

plt.subplot(121); plt.axis('off'); plt.imshow(imgRGB)
plt.subplot(122); plt.axis('off'); plt.imshow(imgGray, cmap = 'gray')
plt.show()

while True:
    if cv2.waitKey() == 27:
        break
    
cv2.destroyWindow('cat')

    

