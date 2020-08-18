import cv2
import numpy as np

# 导入人脸检测级联文件
face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')

# 确定级联文件是否正确地加载
if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

# 初始化视频采集对象
cap = cv2.VideoCapture(0)
# 定义图像向下采样的比例系数
scaling_factor = 0.8

cap.set(3,2000)
cap.set(4,2000)
# 循环采集直到按下Esc键
while True:
    # 采集当前帧并进行调整
    ret,frame = cap.read()
    # 调整帧的大小
    frame = cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
    # 将图像转化为灰度图（这里需要灰度图来运行人脸检测器）
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 在灰度图上运行人脸检测器。参数是1.3是指每个阶段的乘积系数
    # 参数5是指每个候选矩形应该拥有最小近邻数量
    # 在灰度图上进行人脸检测
    face_rects = face_cascade.detectMultiScale(gray,1.3,5)

    # 在脸部画出矩形
    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    # 展示输出图像
    cv2.imshow('Face Detector',frame)

    # 检查是否按下esc件
    c = cv2.waitKey(1)
    if c==27:
        break
# 释放视频采样对象并关闭窗口
cap.release()
cv2.destroyAllWindows()
