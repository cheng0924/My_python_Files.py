import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops


def get_inputs(s):  # s为图像路径
    input = cv2.imread(s, cv2.IMREAD_GRAYSCALE)  # 读取图像，灰度模式

    # 得到共生矩阵，参数：图像矩阵，距离，方向，灰度级别，是否对称，是否标准化
    glcm = greycomatrix(
        input, [
            2, 8, 16], [
            0, np.pi / 4, np.pi / 2, np.pi * 3 / 4], 256, symmetric=True, normed=True)

    print('GLCM:', glcm)

    # 得到共生矩阵统计值，
    for prop in {'contrast', 'dissimilarity',
                 'homogeneity', 'energy', 'correlation', 'ASM'}:
        temp = greycoprops(glcm, prop)
        # temp=np.array(temp).reshape(-1)
        print(prop, temp)

    plt.imshow(input, cmap="gray")
    plt.show()


if __name__ == '__main__':
    get_inputs(r"image42.jpg")

