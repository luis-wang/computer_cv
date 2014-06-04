#!/usr/bin/env python
#coding=utf8

'''
Simple "Square Detector" program.

Loads several images sequentially and tries to find squares in each image.

找到多幅图片中的方块

函数 cvCanny 采用 CANNY 算法发现输入图像的边缘而且在输出图像中标识这些边缘。
threshold1和threshold2 当中的小阈值用来控制边缘连接，大的阈值用来控制强边缘的初始分割。
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt


def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    #先高斯模糊，5*5，去除noise
    img = cv2.GaussianBlur(img, (5, 5), 0)
    
    plt.subplot(122),plt.imshow(img),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()
    
    squares = []
    
    #split函数的主要功能是把一个彩色图像分割成3个通道，方便进一步的图像处理
    for gray in cv2.split(img):
        
        #每隔26取0到255中的数字 
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                #gray这里相应的参数应该是单通道的图片,aperture_size ,Sobel 算子内核大小 (见 cvSobel).
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                #对数组元素进行固定阈值操作,http://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#threshold
                # Python: cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
                #thrs – threshold value.
                #255 – maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
                #type – thresholding type ,here is cv2.THRESH_BINARY
                #使用Threshold检测边缘
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
                
                
            contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            
            for cnt in contours:
                #计算轮廓的周长(只计算封闭的周长True)，Calculates a contour perimeter or a curve length.
                cnt_len = cv2.arcLength(cnt, True)
                
                #多边形逼近轮廓 + 获取矩形和圆形边界框
                
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                #这里是只获得四个角的图形,并且面积大于1000的轮廓,并且检测一个轮廓是不是凸面
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    #重新排列成只有两列的数组
                    cnt = cnt.reshape(-1, 2)
                    
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares

if __name__ == '__main__':
    from glob import glob
    '''
    for fn in glob('../cpp/pic*.png'):
        img = cv2.imread(fn)
        squares = find_squares(img)
        cv2.drawContours( img, squares, -1, (0, 255, 0), 3 )
        cv2.imshow('squares', img)
        ch = 0xFF & cv2.waitKey()
        if ch == 27:
            break
    '''
      
    img = cv2.imread('../cpp/pic1.png')
    squares = find_squares(img)
    '''
     Python: cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) → None
    Parameters:    
    
        image – Destination image.
        contours – All the input contours. Each contour is stored as a point vector.
        contourIdx – Parameter indicating a contour to draw. If it is negative, all the contours are drawn.
        color – Color of the contours.
        thickness – Thickness of lines the contours are drawn with. If it is negative (for example, thickness=CV_FILLED ), the contour interiors are drawn.
        lineType – Line connectivity. See line() for details.
        hierarchy – Optional information about hierarchy. It is only needed if you want to draw only some of the contours (see maxLevel ).
        maxLevel – Maximal level for drawn contours. If it is 0, only the specified contour is drawn. If it is 1, the function draws the contour(s) and all the nested contours. If it is 2, the function draws the contours, all the nested contours, all the nested-to-nested contours, and so on. This parameter is only taken into account when there is hierarchy available.
        offset – Optional contour shift parameter. Shift all the drawn contours by the specified \texttt{offset}=(dx,dy) .
        contour – Pointer to the first contour.
        externalColor – Color of external contours.
        holeColor – Color of internal contours (holes).
     
    '''
    cv2.imshow('orignal img',img)
    cv2.drawContours( img, squares, -1, (0, 255, 0), 3 )
    cv2.imshow('squares', img)
    ch = 0xFF & cv2.waitKey()
            
    cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
