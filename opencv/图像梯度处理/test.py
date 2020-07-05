import cv2
import numpy as np

def cv_show(img,name='None'):
    cv2.imshow(name,img)
    #cv2.waitKey()
    # cv2.destroyAllWindows()

def cv_end():
    cv2.waitKey()
    cv2.destroyAllWindows()

img = cv2.imread('../imgs/pie.png',cv2.IMREAD_GRAYSCALE)

# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# cv_show(img)
# cv_show(sobelx,'sobelx')
# cv_end()

# 绝对值转换
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)
# cv_show(sobelx,'sobelx')
#
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
# sobely = cv2.convertScaleAbs(sobely)
# cv_show(sobely,'sobely')
#
# # 分别计算x和y，在求和
# sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
# cv_show(sobelxy,'sobelxy')
# cv_end()


# img = cv2.imread('../imgs/lena.jpg',cv2.IMREAD_GRAYSCALE)
# cv_show(img,'img')
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)
# cv_show(sobelx,'sobelx')
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
# sobely = cv2.convertScaleAbs(sobely)
# cv_show(sobely,'sobely')
# sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
# cv_show(sobelxy,'sobelxy')
# cv_end()

# 不同算子的差异
img = cv2.imread('../imgs/lena.jpg',cv2.IMREAD_GRAYSCALE)
cv_show(img)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)
# sobely = cv2.convertScaleAbs(sobely)
# sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
#
# scharrx = cv2.Scharr(img,cv2.CV_64F,1,0)
# scharry = cv2.Scharr(img,cv2.CV_64F,0,1)
# scharrx = cv2.convertScaleAbs(scharrx)
# scharry = cv2.convertScaleAbs(scharry)
# scharrxy = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)
#
# laplacian = cv2.Laplacian(img,cv2.CV_64F)
# laplacian = cv2.convertScaleAbs(laplacian)
#
# res = np.hstack((sobelxy,scharrxy,laplacian))
#
# cv_show(res,'res')
cv_end()

