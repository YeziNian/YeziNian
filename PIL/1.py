from PIL import Image
import random
import os
os.mkdir("test")
def addNoise(filename, num):
    if not filename.endswith(".bmp"):
        print("Must be bmp.")
        return
    for i in range(num):
        im = Image.open(filename)
        width, height = im.size
        n = random.randint(1, 20)
        for j in range(n):
            w = random.randint(0, width-1)
            h = random.randint(0, height-1)
            im.putpixel((w,h), (0, 0, 0))
        im.save(filename[:-4]+"_"+str(i+1)+".bmp")
def mergeone(filename, num):
    if not filename.endswith(".bmp"):
        print("Must be bmp.")
        return
    ims = [Image.open(filename[:-4]+"_"+str(i+1)+".bmp") for i in range(num)]
    im = Image.new("RGB", ims[0].size, (255, 255, 255))
    for w in range(im.size[0]):
        for h in range(im.size[1]):
            r, g, b = [0] * 3
            for temp in ims:
                value = temp.getpixel((w,h))
                r += value[0]
                g += value[1]
                b += value[2]
            r = r//num
            g = g//num
            b = b//num
            im.putpixel((w,h), (r, g, b))
    im.save(filename[:-4]+"_result.bmp")

def compare(filename):
    im1 = Image.open(filename)
    im2 = Image.open(filename[:-4]+"_result.bmp")
    width, height = im1.size
    total = width*height
    right = 0
    expecteaedRatio = 0.05
    for w in range(width):
        for h in range(height):
            r1, g1, b1 = im1.getpixel((w, h))
            r2, g2, b2 = im2.getpixel((w, h))
            if (abs(r1-r2), abs(g1-g2), abs(b1-b2)) < (255*expecteaedRatio, )*3:
                right += 1
    return (total, right)
if __name__ == '__main__':
    addNoise(r"C:\Users\40437\Desktop\\cc.bmp", 32)
    mergeone(r"C:\Users\40437\Desktop\\cc.bmp", 32)
    result = compare(r"C:\Users\40437\Desktop\\cc.bmp")
    print("Total number of pixels:{0[0]}, right number{0[1]}".format(result))