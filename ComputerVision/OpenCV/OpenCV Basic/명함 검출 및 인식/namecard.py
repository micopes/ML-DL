import sys
import os
import cv2
import numpy as np
from reorder import reorderPts
# import pytesseract

src = cv2.imread('namecard1.jpg') 

if src is None:
    print('image is None')
    sys.exit()
    
src = cv2.resize(src, (0, 0), fx = 0.5, fy = 0.5)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(th)

contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours)) # 각각의 객체의 개수

for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue
    
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True) # 0.02는 margin
    
    if len(approx) != 4:
        continue
    
    cv2.polylines(src, pts, True, (0, 0, 255))
    
    w, h = 900, 500
    '''
    # 순서는 좌, 우, 상, 하를 고려해서 바꿔야 한다. resize 시에도 변할 수 있다.
    srcQuad = np.array([[approx[0, 0, :]], [approx[1, 0, :]], 
                        [approx[2, 0, :]], [approx[3, 0, :]]]).astype(np.float32)
    '''
    # 자동 보정 되도록 함수 사용
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))
    
    dstQuad = np.array([[0, 0], [0, h], [w, h], [w, 0]]).astype(np.float32)
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    
    dst = cv2.warpPerspective(src, pers, (w, h), flags = cv2.INTER_CUBIC)
    '''
    dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(dst_rgb, lang = 'Hangul+eng'))
    '''

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()

    