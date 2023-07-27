from PIL import Image
import matplotlib.pyplot as plt
im = Image.open(r"C:\Users\40437\Desktop\aa.png")
#im.show()
print(im.format, im.size, im.height, im.width)
#查看图像的直方图
c = im.histogram()
im.getpixel((150, 80)) #获取像素值 x，y的坐标
"""for i in range(200):
    for k in range(200):
        im.putpixel((i, k), (255, 255, 255))"""
#im.save("aa.png")
#im.resize((100, 100))

#im = im.rotate(90)
#im = im.transpose(Image.ROTATE_90)
#im = im.transpose(Image.FLIP_LEFT_RIGHT) #水平翻转
#im = im.transpose(Image.FLIP_TOP_BOTTOM) #垂直翻转

"""box = (120, 194, 220, 294)
region = im.crop(box) #裁剪
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)   #将裁剪的复制上去"""

# im.mode 返回格式
im = im.convert("RGB")
r, g, b = im.split()
"""for i in range(b.width):
    for m in range(b.height):
        b.putpixel((i, m), 0)"""
#r.show()
#imNew = Image.merge(im.mode, (r, g, b))
#imNew = Image.merge("RGBA", (r, g, b, 1))
#c1 = Image.new("RGBA", (100, 100), (255, 0, 0, 9))
#c1.show()
#imNew.show()

#创建缩略图
#im.thumbnail((20, 40))
#im.show()

#屏幕截图
from PIL import ImageGrab
#he = ImageGrab.grab((0, 0, 800, 200))
#he.show()

#图像增强
from PIL import ImageFilter
#im = im.filter(ImageFilter.DETAIL) #创建滤波器
#im = im.filter(ImageFilter.EDGE_ENHANCE)
#im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
#im.show()

#图像模糊
#im = im.filter(ImageFilter.BLUR)
# = im.filter(ImageFilter.GaussianBlur) #高斯模糊
#im.filter(ImageFilter.MedianFilter) #中止滤波
#im.show()

#图像边缘提取
#im = im.filter(ImageFilter.FIND_EDGES)
#im.show()

#图像的点原酸
#im = im.point(lambda x: x*1.1 if x<100 else x*0.2)
#im.show()

#对比度增强
from PIL import ImageEnhance
"""im = ImageEnhance.Contrast(im)
im = im.enhance(0.2)
im.show()"""

