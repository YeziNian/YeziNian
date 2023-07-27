from PIL import Image
import os

def searchLeft(width, height, im):
    for w in range(width):
        for h in range(height):
            color = im.getpixel((w, h))
            if color != (255, 255, 255):
                return w
def searchRight(width, height, im):
    for w in range(width-1, -1, -1):
        for h in range(height):
            color = im.getpixel((w, h))
            if color != (255, 255, 255):
                return w
def searchTop(width, height, im):
    for h in range(height-1, -1, -1):
        for w in range(width):
            color = im.getpixel((w, h))
            if color != (255, 255, 255):
                return h
def searchBottom(width, height, im):
    for h in range(height):
        for w in range(width):
            color = im.getpixel((w, h))
            if color != (255, 255, 255):
                return h

im = Image.open(r"C:\Users\40437\Desktop\cc.png")
width, height = im.size
x0, x1 = searchLeft(width, height, im), searchRight(width, height, im)
y1, y0 = searchTop(width, height, im), searchBottom(width, height, im)
center = ((x0+x1)//2, (y1+y0)//2)
im.putpixel(center, (255, 0, 0))
im.show()