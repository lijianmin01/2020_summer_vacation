# 学习如何读取网络摄像头和图像

import cv2
import numpy as np

# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# 如何导入视频
# cap=cv2.VideoCapture('Resources/test_video.mp4')
#
# while True:
#     success,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# 使用网络摄像头
# cap = cv2.VideoCapture(0)
# # 设置宽度
# cap.set(3,640)
# # 设置高度
# cap.set(4,480)
# # 设置亮度
# cap.set(0,10)
# while True:
#     success,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# # 一些基本功能
#
# ## 将图片转成灰度图片
# img = cv2.imread("Resources/lena.png")
#
# kernel = np.ones((5,5),np.uint8)
#
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # 让照片边的模糊
# imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
# # 边缘检测
# imgCanny = cv2.Canny(img,100,100)
# # 膨胀图像
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# # 图像侵蚀
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
#
# # cv2.imshow("Gray img",imgGray)
# # cv2.imshow("Blur img",imgBlur)
# cv2.imshow("Canny img",imgCanny)
# cv2.imshow("Dialation img",imgDialation)
# cv2.imshow("Eroded img",imgEroded)
# cv2.waitKey(0)


# 如何调整图像大小

# img = cv2.imread("Resources/lambo.png")
# print(img.shape) #(462, 623, 3)
#
# imgResize = cv2.resize(img,(300,200))
# print(imgResize.shape) # (200, 300, 3)
#
# cv2.imshow('Image',img)
# cv2.imshow('Image Resize',imgResize)
# cv2.waitKey(0)

# 如何裁剪图像
# img = cv2.imread("Resources/lambo.png")
# imgCropped = img[200:400,200:500]
#
# cv2.imshow('Image',img)
# cv2.imshow('Cropped Image',imgCropped)
#
# cv2.waitKey(0)


# 如何在图像上绘制形状，添加文本
# img = np.zeros((512,512,3),np.uint8)


# img[200:300,0:200]=255,0,0
#
# print(img)

#cv2.line(img,(0,0),(300,300),(0,255,0),3)# 起点终点颜色，线条宽度

# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(244,0,0),4)
# ## 加个矩形
# ##cv2.rectangle(img,(0,0),(250,350),(56,0,48),2)
# ### 填充矩形
# #cv2.rectangle(img,(0,0),(250,350),(255,255,255),cv2.FILLED)
#
#
# cv2.rectangle(img,(0,0),(250,350),(255,255,255),2)
# cv2.circle(img,(400,50),30,(255,255,0),1)
#
# cv2.putText(img," OPENCV ",(0,img.shape[1]),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
# cv2.imshow('Image',img)
#
# cv2.waitKey(0)


# 如何在图像上使用单词视角获取图像

# img = cv2.imread("Resources/cards.jpg")
#
# width , height = 250,360
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# # 返回由源图像中矩形到目标图像矩形变换的矩阵
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
# # 透视变换（单应性？）能提供更大的灵活性，但是一个透视投影并不是线性变换，因此所采用的映射矩阵是3*3，且控点变为4个，其他方面与仿射变换完全类似，
#
#
# cv2.imshow('Image',img)
# cv2.imshow('Output',imgOutput)
# cv2.waitKey(0)


# 将图像结合在一起

# img = cv2.imread("Resources/lena.png")
#
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
#
# cv2.waitKey(0)

## 将一组图像an按照比例放大和缩小
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread('Resources/lena.png')

imgStack = stackImages(0.4,([img,img,img],[img,img,img]))

cv2.imshow("imgStack",imgStack)

cv2.waitKey(0)