import sys
import numpy as np
import cv2

# 미리 학습된 GoogLeNet 학습 모델 및 구성 파일 다운로드하여 이용

# 입출력 형식
# 입력 : (224 x 224), BGR, mean = (104, 117, 123)
# 출력 : 1000개의 노드


filename = 'beagle.jpg'

if len(sys.argv) > 1:
    filename = sys.argv[1]
    
img = cv2.imread(filename)

# Load Network
net = cv2.dnn.readNet('bvlc_googlenet.caffemodel', 'deploy.prototxt')

# Load class names
classNames = None
with open('classification_classes_ILSVRC2012.txt', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Inference
inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123))
net.setInput(inputBlob, 'data')
prob = net.forward()

# check results & Display
out = prob.flatten()
classId = np.argmax(out)
confidence = out[classId]

text = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)
cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 
            1, cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
