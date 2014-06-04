#coding:utf8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/49.jpg',0)

#这里故意给模糊了一下
img = cv2.medianBlur(img,3)

ret,th1 = cv2.threshold(img,220,255,cv2.THRESH_BINARY)

wb = cv2.cvtColor(th1, cv2.COLOR_GRAY2BGR)
cv2.imwrite('img/wb4.png', wb)

cv2.imshow('wb', wb)
cv2.waitKey(0)
