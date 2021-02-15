import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('lenna.bmp')
# cv2.imread로 받은 것은 BGR 순이므로 
# matplotlib에 출력하기 위해서는 RGB 순서로 바꿔줘야 한다.
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(imgGray, cmap = 'gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap = 'gray')
plt.show()