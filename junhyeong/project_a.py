#TODO: 컬러 사진을 흑백사진으로 변환하기
import sys
import cv2
import numpy as np
img = cv2.imread("./cat.jpg")
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

height, width, channels = img.shape

gray_img = np.zeros((height, width), dtype = np.uint8)

for i in range(height):
    for j in range(width):

        B,G,R = img[i, j]

        I = round(0.299*R+0.587*G+0.114*B)
        gray_img[i, j] = I

cv2.imshow('Grayscale Image', gray_img)


cv2.waitKey(0)
cv2.destroyAllWindows()