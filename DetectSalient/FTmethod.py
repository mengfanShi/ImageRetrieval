# -*- coding:utf-8 -*-
# @TIME     :2018/11/2 16:51
# @Author   :Fan
# @File     :FTmethod.py
import cv2
import numpy as np


class FTdetect():
    def __init__(self, filename):
        self.image = self.read_image(filename)

    def read_image(self, filename):
        if cv2.imread(filename) is None:
            print('please input the right image\n')
            exit()
        else:
            return cv2.imread(filename)

    def filter(self, image, ksize=(3, 3), sigmal=0):
        middle = image
        cv2.GaussianBlur(src=middle, ksize=ksize, sigmaX=sigmal, dst=middle)
        return middle

    def calLab(self, image):
        middle = image
        cv2.cvtColor(src=middle, code=cv2.COLOR_BGR2Lab, dst=middle)
        L, a, b = cv2.split(middle)
        result = np.sqrt((L - np.mean(L))**2 + (a - np.mean(a))**2 + (b - np.mean(b))**2)
        return result

    def normalize(self, image):
        max = np.max(image)
        min = np.min(image)
        return (image - min) / (max - min)

    def excute(self):
        image_fil = self.filter(self.image)
        image_fil = self.filter(image_fil, ksize=(5,5))
        result = self.calLab(image_fil)
        out = self.normalize(result)
        return out


if __name__ == '__main__':
    ft = FTdetect("F://cuple.jpg")
    origin_image = ft.read_image("F://cuple.jpg")
    result = ft.excute()
    cv2.namedWindow('origin', 0)
    cv2.namedWindow('result', 0)
    cv2.imshow('origin', origin_image)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




