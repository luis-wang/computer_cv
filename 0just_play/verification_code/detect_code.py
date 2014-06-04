#coding:utf-8
#基于python2.7
'''
http://blog.csdn.net/nwpulei/article/details/8457738
'''
import Image
from pytesser import image_to_string

im = Image.open('1.jpg')

#把彩色图像转化为灰度图像。彩色图像转化为灰度图像的方法很多，这里采用RBG转化到HSI彩色空间，采用I分量
imgry = im.convert('L')

# 需要把图像中的噪声去除掉。这里的图像比较简单，直接阈值化就行了。我们把大于阈值threshold的像素置为1，
#其他的置为0。对此，先生成一张查找表，映射过程让库函数帮我们做。

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = imgry.point(table,'1')  

#Step 4 把图片中的字符转化为文本。采用pytesser 中的image_to_string函数
text = image_to_string(out)  

print 'result:',text


#根据观察，验证码中只有数字，并且上面的文字识别程序经常把8识别为S。
#因此，对于识别结果，在进行一些替换操作。
#由于都是数字 对于识别成字母的 采用该表进行修正
rep={'O':'0',
    'I':'1','L':'1',
    'Z':'2',
    'S':'8'
    };

for r in rep:
    text = text.replace(r,rep[r])

print 'new result:',text



