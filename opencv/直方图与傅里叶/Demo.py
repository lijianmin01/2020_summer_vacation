import cv2
import matplotlib.pyplot as plt
import numpy as np

# img = cv2.imread('../imgs/cat.jpg',0)
# cv2.imshow('None',img)
# cv2.waitKey(0)

# hist = cv2.calcHist([img],[0],None,[256],[0,256])
# print(hist.shape)
# (256, 1)

# img = cv2.imread('../imgs/cat.jpg',0)
# plt.hist(img.ravel(),256)
# plt.show()


# # 默认读取彩色图片
# img = cv2.imread('../imgs/cat.jpg')
# color = ('b','g','r')
# # 枚举，画出每个通道的颜色分布
# for i ,col in enumerate(color):
#     histr = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color=col)
#     plt.xlim([0,256])
#
# plt.show()


def cv_show(img,name='None'):
    cv2.imshow(name,img)
    #cv2.waitKey()
    # cv2.destroyAllWindows()

def cv_end():
    cv2.waitKey()
    cv2.destroyAllWindows()

# # mask操作
# img = cv2.imread('../imgs/cat.jpg')
# mask = np.zeros(img.shape[:2],np.uint8)
# print(mask.shape)
# mask[100:300,100:400]=255
# # cv_show(mask,'mask')
#
# img = cv2.imread('../imgs/cat.jpg',0)
# cv_show(img,'img')
#
# # 与操作
# masked_img = cv2.bitwise_and(img,img,mask=mask)
# cv_show(masked_img,'masked_img')
#
# hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
# hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
#
# plt.subplot(221)
# plt.imshow(img,'gray')
# plt.subplot(222)
# plt.imshow(mask,'gray')
# plt.subplot(223)
# plt.imshow(masked_img,'gray')
# plt.subplot(224)
# plt.plot(hist_full)
# plt.plot(hist_mask)
# plt.xlim([0,256])
# plt.show()

# 图像均衡化
# plt.subplot(121)
# img = cv2.imread('../imgs/cat.jpg',0) # 0 表示灰度图
# plt.hist(img.ravel(),256)
# plt.title('原图像')
# # 使用均衡化函数来实现
# plt.subplot(122)
# equ = cv2.equalizeHist(img)
# plt.hist(equ.ravel(),256)
# plt.title('均衡化之后的图像')
# plt.show()
#
# res = np.hstack((img,equ))
# cv_show(res)
# cv_end()


# 自适应均衡化
# img = cv2.imread('../imgs/clahe.jpg',0)
#
# plt.hist(img.ravel(),256)
# # plt.hist(img.ravel(),256)
# plt.show()
# equ = cv2.equalizeHist(img)
# # res = np.hstack((img,equ))
#
# ## 自适应直方图均衡化
# clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
#
# res_clahe = clahe.apply(img)
# res = np.hstack((img,equ,res_clahe))
# cv_show(res,'res')
# cv_end()


# img = cv2.imread('../imgs/lena.jpg',0)
#
# img_float32 = np.float32(img)
#
# dft = cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
#
# # 得到灰度图能表示的形式
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#
# plt.subplot(121)
# plt.imshow(img,cmap='gray')
# plt.title('Input Image')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(magnitude_spectrum,cmap='gray')
# plt.title('Magnitude Spectrum')
# plt.xticks([])
# plt.yticks([])
# plt.show()


# img = cv2.imread('../imgs/lena.jpg',0)
#
# img_float32 = np.float32(img)
#
# dft = cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
#
# rows,cols = img.shape
# crow,ccol = int(rows/2),int(cols/2)  # 中心位置
#
# # 低波通道
# mask = np.zeros((rows,cols,2),np.uint8)
# mask[crow-30:crow+30,ccol-30:ccol+30]=1
#
# # IDFT
# fshift = dft_shift*mask
# f_ishift = np.fft.ifftshift(fshift)
# img_back = cv2.idft(f_ishift)
# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
#
# plt.subplot(121)
# plt.imshow(img,cmap='gray')
# plt.title('Input Image')
# plt.xticks([])
# plt.yticks([])
#
# plt.subplot(122)
# plt.imshow(img_back,cmap='gray')
# plt.title('Result')
# plt.xticks([])
# plt.yticks([])
# plt.show()

img = cv2.imread('../imgs/lena.jpg',0)

img_float32 = np.float32(img)

dft = cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows,cols = img.shape
crow,ccol = int(rows/2),int(cols/2)  # 中心位置

# 高通滤波
mask = np.ones((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30]=0

# IDFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('Input Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(img_back,cmap='gray')
plt.title('Result')
plt.xticks([])
plt.yticks([])
plt.show()








