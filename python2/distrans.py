#coding:utf8

'''
Distance transform sample.

Usage:
  distrans.py [<image>]

Keys:
  ESC   - exit
  v     - toggle voronoi mode
'''


import numpy as np
import cv2
import cv2.cv as cv
from common import make_cmap

fn = '../cpp/fruits.jpg'

if __name__ == '__main__':


    img = cv2.imread(fn, 0)
    cv2.imshow('winname', img)
    cm = make_cmap('jet')
    need_update = True
    voronoi = False

    def update(dummy=None):
        global need_update
        need_update = False
        thrs = cv2.getTrackbarPos('threshold', 'distrans')
        mark = cv2.Canny(img, thrs, 3*thrs)
        #CV_DIST_L2表示的是coarse distance estimation
        dist, labels = cv2.distanceTransformWithLabels(~mark, cv.CV_DIST_L2, 5)
        if voronoi:
            vis = cm[np.uint8(labels)]
        else:
            vis = cm[np.uint8(dist*2)]
        vis[mark != 0] = 255
        cv2.imshow('distrans', vis)

    def invalidate(dummy=None):
        global need_update
        need_update = True

    cv2.namedWindow('distrans')
    cv2.createTrackbar('threshold', 'distrans', 60, 255, invalidate)
    update()


    while True:
        ch = 0xFF & cv2.waitKey(50)
        if ch == 27:
            break
        if ch == ord('v'):
            voronoi = not voronoi
            print 'showing', ['distance', 'voronoi'][voronoi]
            update()
        if need_update:
            update()
    cv2.destroyAllWindows()
