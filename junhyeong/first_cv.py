import sys
import cv2

img = cv2.imread("./cat.jpg")
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv2.imshow("Image Display", img)
cv2.waitKey()
cv2.destroyAllWindows()