# -*- coding: cp936 -*-
##PILLOW
>>> from PIL import Image,ImageFilter
>>> im=Image.open('E:\Python27\humb.jpg')
>>> im2=im.filter(ImageFilter.BLUR )
>>> im2.save('E:\Python27\blur.jpeg')

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    im2.save('E:\Python27\blur.jpeg')
  File "E:\Python27\lib\site-packages\PIL\Image.py", line 1682, in save
    fp = builtins.open(filename, "wb")
IOError: [Errno 22] invalid mode ('wb') or filename: 'E:\\Python27\x08lur.jpeg'
>>> im2.save(r'E:\Python27\blur.jpeg')


##ͼ����֤��
# -*- coding: cp936 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# �����ĸ:
def rndChar():
    return chr(random.randint(65, 90))

# �����ɫ1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# �����ɫ2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# ����Font����:
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# ����Draw����:
draw = ImageDraw.Draw(image)
# ���ÿ������:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# �������:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# ģ��:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg'); 
