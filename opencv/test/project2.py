# 文档扫描

import cv2
import numpy as np
#################################
widthImg,heightImg = 640,480
##################################



frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    # 内核
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.dilate(imgDial,kernel,iterations=1)

    # 返回边界
    # return imgCanny
    # 返回图像的阈值
    return imgThres


while True:
    success , img = cap.read()
    # 重置图片大小
    cv2.resize(img,(widthImg,heightImg))

    imgThres = preProcessing(img)

    cv2.imshow("Result",imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
