import cv2
import sys


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img1 is None or img2 is None:
    print("Image load failed")
    sys.exit()
    
print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

h, w = img1.shape[:2]
print('w x h = {} x {}'.format(w, h))

h, w = img2.shape[:2]
print('w x h = {} x {}'.format(w, h))

# 픽셀 값을 읽기
x = 20
y = 10
p1 = img1[y][x]
print(p1)

# 픽셀 값 수정하기
x = 20
y = 10
img1[y][x] = (255, 0, 0)
p2 = img1[y][x]
print(p2)


if len(img1.shape) == 2:
    print("img1 is a grayscale image")

'''
# 효율성이 매우 떨어진다. 다른 대체할 방법을 이용해야 한다.
end = False    
for i in range(w):
    for j in range(h):
        img1[j, i] = (0, 255, 0)
'''
img1[:, :] = (0, 255, 255)
img2[:, :] = 0
        
cv2.imshow('img', img1)
cv2.waitKey(1000)    
cv2.destroyAllWindows()
    
        