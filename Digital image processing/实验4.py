import cv2
import numpy as np


# Robert算子
def Robert(img):
    h, w = img.shape
    rob = [[-1, -1], [1, 1]]
    for x in range(h):
        for y in range(w):
            if(y+2 <= w) and (x+2 <= h):
                imgChild = img[x:x+2, y:y+2]
                list_robert = rob*imgChild
                img[x, y] = abs(list_robert.sum())
    return img

# Sobel算子
def Sobel(img):
    h, w = img.shape
    image = np.zeros((h, w))
    imageX = np.zeros(img.shape)    # 初始化Gx、Gy和G;
    imageY = np.zeros(img.shape)
    sob_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sob_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    for i in range(h-2):
        for j in range(w-2):
            imageX[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3]*sob_x))
            imageY[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3]*sob_y))
            image[i+1, j+1] = (imageX[i+1, j+1]*imageX[i+1, j+1]+imageY[i+1, j+1]*imageY[i+1, j+1])**0.5
    return np.uint8(image)

# Laplace算子:
def Laplace(img, L):
    h, w = img.shape
    image = np.zeros((h, w))
    # L = np.array([0, -1, 0], [-1, 4, -1], [0, 1, 0])
    # L1 = np.array([-1, -1, -1], [-1, 8, -1], [-1, -1, -1])
    for i in range(h-2):
        for j in range(w-2):
            image[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3]*L))
    return np.uint8(image)


img = cv2.imread('image42.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('original', img)
out_robert = Robert(img)
cv2.imshow('Robert', out_robert)

out_sobel = Sobel(img)
cv2.imshow('Sobel', out_sobel)

L = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
out_laplace1 = Laplace(img, L)
cv2.imshow('Laplace_1', out_laplace1)
L1 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
out_laplace2 = Laplace(img, L1)
cv2.imshow('Laplace_2', out_laplace2)

cv2.waitKey(0)
cv2.destroyAllWindows()
