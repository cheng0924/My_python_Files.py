
import numpy as np
import cv2

#图像读入
img = cv2.imread('./image42.jpg', 0)

# Canny边缘检测原图像
canny_origin_img = cv2.Canny(img,100,200)

# Sobel边缘检测原图像
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobel_combined_origin = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Laplace边缘检测原图像
tmp_img = cv2.Laplacian(img,cv2.CV_64F)
Laplace_origin_img = cv2.convertScaleAbs(tmp_img)

# 对原图像添加 Gauss noise

mean = 0    #选取均值为
var = 0.001       #方差为0.005
img = np.array(img/255,dtype=float)
noise = np.random.normal(mean,var ** 0.5,img.shape)
Gauss_noise_img = img + noise
if Gauss_noise_img.min() < 0:
    low_clip = -1
else:
    low_clip = 0
noisy_img = np.clip(Gauss_noise_img,low_clip,1.0)
noisy_img = np.uint8(Gauss_noise_img*255)


#Sobel边缘检测噪声图像
sobelx = cv2.Sobel(noisy_img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(noisy_img, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobel_combined_noisy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

#Laplace边缘检测噪声图像
tmp_img = cv2.Laplacian(noisy_img,cv2.CV_64F)
Laplace_noisy_img = cv2.convertScaleAbs(tmp_img)

#Canny边缘检测噪声图像
canny_noisy_img = cv2.Canny(noisy_img,100,200)


#图像输出

#原图像的边缘检测
#cv2.imshow("original image",img)
#cv2.imshow("Canny",canny_origin_img)
#cv2.imshow("Laplace",Laplace_origin_img)
#cv2.imshow("Sobel",sobel_combined_origin)

#加噪后的边缘检测
cv2.imshow("image",img)
cv2.imshow("Gauss noised image",noisy_img)
cv2.imshow("Canny Edge Detector,noisy image",canny_noisy_img)
cv2.imshow("Laplace Edge Detector,noisy image",Laplace_noisy_img)
cv2.imshow("Sobel Edge Detector,noisy image",sobel_combined_noisy)

#等待关闭
cv2.waitKey(0)
cv2.destroyAllWindows()
