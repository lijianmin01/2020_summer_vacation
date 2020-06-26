import cv2

# 初始化网络摄像头
cap = cv2.VideoCapture(0)
# 定义网络摄像头采集图像的比例系数
scaling_factor = 0.5
# 启动一个无限循环来采集帧，直到按下esc键，从网络摄像头读取帧

while True:
    # 采集当前画面
    ret, frame = cap.read()
    # 调整帧的大小
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # 显示帧
    cv2.imshow('Webcam', frame)
    # 等待1ms,然后采集下一帧
    c = cv2.waitKey(1)
    if c == 27:
        break
# 释放视频采集对象
cap.release()
# 关闭所有活动窗体
cv2.destoryAllWindows()