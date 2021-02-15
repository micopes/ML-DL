import cv2
import sys

#img = cv2.imread('cat.bmp')
# 흑백
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread(img1, cv2.IMREAD_COLOR)


# 예외처리
if img is None:
    print("Image load failed!")
    sys.exit()
    
print(type(img))
print(img.shape)
print(img.dtype)

cv2.namedWindow('image') # image라는 것을 화면에 띄워라.
cv2.imshow('image', img) # img를 보여준다.
cv2.waitKey() # 기다리는 시간(키보드 아무거나 입력하면 꺼진다.)
'''
# ESC 눌러서 종료하게 하려면 ESC에 해당하는 ASCII인 27로 설정
while True:
    if cv2.waitKey() == 27:
        break
'''
cv2.destroyAllWindows() # 이걸 누르는게 낫다.

# 매우 단순화 한 코드
'''
import cv2

img = cv2.imread('cat.bmp')

cv2.imshow('image', img)
cv2.waitKey()
'''