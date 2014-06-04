#coding:utf-8
#基于python2.7
'''

'''
import Image
import ImageFilter

global ext
ext = ".jpg"

imageFile = "test.jpg"
im1 = Image.open(imageFile)


def imgResize(im):

    div = 2
    width = im.size[0] / div
    height = im.size[1] / div

    im2 = im.resize((width, height), Image.NEAREST) # use nearest neighbour
    im3 = im.resize((width, height), Image.BILINEAR) # linear interpolation in a 2x2 environment
    im4 = im.resize((width, height), Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    im5 = im.resize((width, height), Image.ANTIALIAS) # best down-sizing filter
    
    im2.save("NEAREST" + ext)
    im3.save("BILINEAR" + ext)
    im4.save("BICUBIC" + ext)
    im5.save("ANTIALIAS" + ext)


def imgCrop(im):
    
    box = (50, 50, 200, 300)
    region = im.crop(box)
    region.save("CROPPED" + ext)


def imgTranspose(im):
    
    box = (50, 50, 200, 300)
    region = im.crop(box)
    
    region = region.transpose(Image.ROTATE_180)
    im.paste(region, box)
    
    im.save("TRANSPOSE" + ext)

def bandMerge(im):
    
    r, g, b = im.split()
    im = Image.merge("RGB", (g,g,g))
    
    im.save("MERGE" + ext)




def filterBlur(im):
    
    im1 = im.filter(ImageFilter.BLUR)
    
    im1.save("BLUR" + ext)


def filterContour(im):
    
    im1 = im.filter(ImageFilter.CONTOUR)
    
    im1.save("CONTOUR" + ext)


def filterFindEdges(im):
    
    im1 = im.filter(ImageFilter.FIND_EDGES)
    
    im1.save("EDGES" + ext)

filterFindEdges(im1)


#filterContour(im1)


#filterBlur(im1)

#bandMerge(im1)

#imgTranspose(im1)

#imgCrop(im1)

#imgResize(im1)



