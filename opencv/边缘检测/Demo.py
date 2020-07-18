import cv2
import numpy as np

img = cv2.imread("../imgs/lena.jpg",cv2.IMREAD_GRAYSCALE)

v1 = cv2.Canny(img,80,150)
v2 = cv2.Canny(img,50,100)

res = np.hstack((img,v1,v2))
cv2.imshow('res',res)
cv2.waitKey()