import cv2
# 画图
import matplotlib.pyplot as plt
import numpy as np
import time

# img = cv2.imread('../imgs/cat1.jpg')
# img_gray = cv2.imread('../imgs/cat1.jpg',cv2.IMREAD_GRAYSCALE)
#
# ret,thresh1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO_INV)
#
# titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
#
# for i in range(6):
#     plt.subplot(2,3,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

img = cv2.imread('../imgs/opencv.png')

cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 均值滤液
# 简单的屏均处理
blur = cv2.blur(img,(3,3))

cv2.imshow('blur',blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 方框滤液
# 基本和均值一样，可以选择归一化
box = cv2.boxFilter(img,-1,(3,3),normalize=True)

cv2.imshow('box',box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 方框滤液
# 基本和均值一样，可以选择归一化,容易越界
box = cv2.boxFilter(img,-1,(3,3),normalize=False)

cv2.imshow('box',box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 高斯滤液
# 高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的
aussian = cv2.GaussianBlur(img,(5,5),1)

cv2.imshow('aussian',aussian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 中值滤液
# 相当于用中值代替
median = cv2.medianBlur(img,5)

cv2.imshow('median',median)
cv2.waitKey(0)
cv2.destroyAllWindows()





