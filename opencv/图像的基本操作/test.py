
# opencv 读取的格式是BRG格式
import cv2
# 画图
import matplotlib.pyplot as plt
import numpy as np
import time


# 读取图像
# # img = cv2.imread('../imgs/cat1.jpg')
# img = cv2.imread('../imgs/cat1.jpg',cv2.IMREAD_GRAYSCALE)
# # 展示图像
# cv2.imshow('img',img)
# # 设置等待时间，毫秒级，0表示任意键终止图像显示
# cv2.waitKey(0)
# # 关闭所有窗口
# cv2.destroyAllWindows()


# # 读取视频（一个帅气的小哥哥）
# vc = cv2.VideoCapture('../videos/sqdxgg.mp4')
# # 检查文件路径是否正确
# if vc.isOpened():
#     open,frame = vc.read()
# else:
#     open = False
#
# while open:
#     ret,frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('reslut',gray)
#         # esc
#         if cv2.waitKey(1000) & 0xFF==27:
#             break
#
# # 释放
# vc.release()
# # 关闭所有窗口
# cv2.destroyAllWindows()

# 创建一个窗口展示图像

# def cv_show(name,img):
#     cv2.imshow(name,img)
#     cv2.waitKey(5000)
#     cv2.destroyAllWindows()
#
# img = cv2.imread('../imgs/cat2.jpg')
# # 原图像
# cv_show('cat',img)
# img = cv2.imread('../imgs/cat2.jpg')
# cat = img[0:200,0:200]
# # 部分图像
# cv_show('cat',cat)



# # 颜色通道的提取
# img = cv2.imread('../imgs/cat2.jpg')
# # blue,green,red = cv2.split(img)
# cv_show('img',img)
# b,g,r = cv2.split(img)
# cv_show('blue',b)
# cv_show('green',g)
# cv_show('red',r)
# # 将图片通道组合起来
# img = cv2.merge((b,g,r))
#
# time.sleep(10)

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(5000)

img = cv2.imread('../imgs/cat2.jpg')
cv_show('img',img)
# 只保留R
imgr = img.copy()
imgr[:,:,0]=0
imgr[:,:,1]=0
cv_show('R',imgr)

# 只保留G
imgg = img.copy()
imgg[:,:,0]=0
imgg[:,:,2]=0
cv_show('G',imgg)

# 只保留B
imgb = img.copy()
imgb[:,:,1]=0
imgb[:,:,2]=0
cv_show('B',imgb)

time.sleep(10)
