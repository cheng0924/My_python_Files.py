import cv2
import matplotlib.pyplot as plt

def hist(img):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

img = cv2.imread("image42.jpg", 1)
cv2.imshow('origin', img)
hist(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("src", gray)
hist(gray)

dst = cv2.equalizeHist(gray)
cv2.imshow("dst", dst)
hist(dst)

cv2.waitKey(0)