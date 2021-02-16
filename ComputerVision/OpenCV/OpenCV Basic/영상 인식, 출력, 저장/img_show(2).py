import sys
import cv2

cat = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if cat is None:
    print("Image load failed")
    sys.exit()


cv2.imwrite('cat_gray.png', cat)
cv2.namedWindow('cat') # 영상의 사이즈를 조정할 필요 없는 경우 사용필요 없다.
cv2.imshow('cat', cat)
key = cv2.waitKey()
print(key)

# cv2.destroyWindow('cat')
cv2.destroyAllWindows()