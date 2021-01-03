import cv2
import numpy as np

img = cv2.imread('image42.jpg')
rows, cols, dims = img.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

# 均值滤波
result = cv2.blur(img, (3, 3))

# 中值滤波
mdB = cv2.medianBlur(img, 5)

# 高斯滤波
Gauss = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow('img', img)
cv2.imshow('blur', result)
cv2.imshow("img_median", mdB)
cv2.imshow('img_Gauss', Gauss)
cv2.waitKey()
cv2.destroyAllWindows()
