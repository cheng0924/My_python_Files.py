import numpy as np
from PIL import Image
import math
import copy
import matplotlib.pyplot as plt

img = np.array(Image.open('image42.jpg',).convert('RGB'))    # 打开图片转换为numpy数组
new_r = copy.deepcopy(img)                              # 进行拷贝，为后面的分量显示做铺垫
new_g = copy.deepcopy(img)
new_b = copy.deepcopy(img)
img = img/255                                           # 归一化

r = img[:, :, 0]
rows = len(r)
cols = len(r[1])
new = copy.deepcopy(img)                                # 用来储存HSI图像

for i in range(rows):
    for j in range(cols):
        II = (img[i, j, 0]+img[i, j, 1]+img[i, j, 2])/3  # HSI分量的I

        num = 0.5 * ((img[i, j, 0]-img[i, j, 1]) + (img[i, j, 0]-img[i, j, 2]))     # theta值的分子

        den = math.sqrt((img[i, j, 0]-img[i, j, 1]) ** 2 + (img[i, j, 0]-img[i, j, 2])*(img[i, j, 1]-img[i, j, 2]))     #theta值的分母
        if den == 0:    # 分母不为0
            theta = 0
        else:
            theta = math.acos(num/den)  # 求theta
        if img[i, j, 2] <= img[i, j, 1]:    # B<=G
            new[i, j, 0] = int(theta*255/(2*math.pi))
        else:
            new[i, j, 0] = int((2*math.pi-theta)*255/(2*math.pi))
        if II == 0:         # I为0时设置S为0
            new[i, j, 1] = 0
        else:
            new[i, j, 1] = int((1-min((img[i, j, 0], img[i, j, 1], img[i, j, 2]))/II)*255)
        new[i, j, 2] = int(II*255)
'''上面×255的操作也可以完成后再进行'''

imge = np.array(new)    # 把new转化成numpy数组

im = imge.astype(np.int)    # numpy数组转化为0-255的整数

new_r[:, :, 1] = 0
new_r[:, :, 2] = 0
RGB_R = new_r   # R分量显示，把GB设为0

new_g[:, :, 0] = 0
new_g[:, :, 2] = 0
RGB_G = new_g   # G分量显示，把RB设为0

new_b[:, :, 0] = 0
new_b[:, :, 1] = 0
RGB_B = new_b   # B分量显示，把RG设为0


plt.subplot(2, 2, 1)     # 一行四列第一个图
plt.imshow(im)
plt.title('HSI')
plt.axis('on')      # 不显示坐标


plt.subplot(2, 2, 2)
plt.imshow(RGB_R)
plt.title('R')
plt.axis('on')


plt.subplot(2, 2, 3)
plt.imshow(RGB_G)
plt.title('G')
plt.axis('on')

plt.subplot(2, 2, 4)
plt.imshow(RGB_B)
plt.title('B')
plt.axis('on')

#plt.savefig("HSI.jpg")   # 保存图片为HSI.jpg
plt.show()               # 显示图片





