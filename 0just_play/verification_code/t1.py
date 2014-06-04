#coding:utf-8
#基于python2.7
'''

'''
import sys
import Image
from pytesser import *


text = image_file_to_string('fonts_test.png', graceful_errors=True)
print 'png rec:',text
sys.exit()


try:
    text = image_file_to_string('fnord.tiff', graceful_errors=False)
except errors.Tesser_General_Exception, value:
    print "fnord.tif is incompatible filetype.  Try graceful_errors=True"
    print value

sys.exit()


im = Image.open('2.tiff')
text = image_to_string(im)
print text