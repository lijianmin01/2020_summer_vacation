# Haar级联方法可以被口占应用于各种对象的检测

import cv2
import numpy as np

# 加载人脸、眼睛、和鼻子级联文件
face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')

eye_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_eye.xml')

nose_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_mcs_nose.xml')

# 确定级联文件是否正确加载
if face_cascade.empty():
    raise  IOError('Unable to load the face cascade classifier xml file')

if eye_cascade.empty():
    raise  IOError('Unable to load the eye cascade classifier xml file')

if nose_cascade.empty():
    raise  IOError('Unable to load the nose cascade classifier xml file')

# 初始化视频采集对象并定义比例系数
cap = cv2.VideoCapture(0)
# 定义比例系数
scaling_factor = 0.5

while True:
    # 读取当前画面，调整大小，转为灰度
    ret,frame = cap.read()
    # 调整帧的大小+
    frame = cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
    # 将图像转为灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 在灰度图像上运行人脸检测器
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    # 每张脸的矩形区域运行眼睛和鼻子检测器
    for(x,y,w,h) in faces:
        # 从色彩与灰度图中提取人脸ROI信息
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = gray[y:y+h,x:x+w]
        # 在灰度图ROI信息中检测眼睛
        eye_rects = eye_cascade.detectMultiScale(roi_gray)
        # 鼻子
        nose_rects = nose_cascade.detectMultiScale(roi_gray,1.3,5)

        # 在眼睛周围画圈
        for(x_eye,y_eye,w_eye,h_eye) in eye_rects:
            center = (int(x_eye+0.5*w_eye),int(y_eye+0.5*h_eye))
            radius = int(0.3*(w_eye+h_eye))
            color=(0,255,0)
            thickness = 3
            cv2.circle(roi_color,center,radius,color,thickness)

        # 在鼻子周围画矩形’
        for (x_nose,y_nose,w_nose,h_nose) in nose_rects:
            cv2.rectangle(roi_color,(x_nose,y_nose),(x_nose+w_nose,y_nose+h_nose),(0,255,0),3)
            break

    # 展示该图像
    cv2.imshow('Eye and Nose detector',frame)
    # esc
    c= cv2.waitKey(1)
    if c == 27:
        break
# 在代码结束之前，释放素有对象
cap.release()
cap.destroyAllWindows()








