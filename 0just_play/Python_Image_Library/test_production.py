#coding:utf-8
#基于python2.7
'''

'''
import os
import Image
import ImageFilter

global ext
ext = ".jpg"

imageFile = "img/box1.png"
im1 = Image.open(imageFile)


def filterFindEdges(im):
    im1 = im.filter(ImageFilter.FIND_EDGES)
    
    new_imageFile = imageFile.split('.')[0] + '_edges' + '.' + imageFile.split('.')[1]
    im1.save(new_imageFile)

filterFindEdges(im1)



