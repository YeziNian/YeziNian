#from PIL import Image
#import os

#gifFilename = r"C:\Users\40437\Desktop\aa.gif"
#im = Image.open(gifFilename)
# = gifFilename[:-4]
#os.mkdir(pngDir)
#try:
    #while True:
       # current = im.tell()
        #im.save(pngDir+"\\"+str(current)+".png")
        #im.seek(current+1)
#except EOFError:
    #pass

"""import images2gif
import os
from PIL import Image"""
"""
def png(gifname, path, duration=0.1, np=0.1):
    pngfiles = [f for f in os.listdir(path)]
    pngfiles.sort(key=lambda f: int(f[:-4]))
    pngfiles = [os.path.join(path, f) for f in pngfiles]
    images = []
    for f in pngfiles:
        images.append(Image.open(f))
    images2gif.writeGif(gifname, images, duration, np)
png("cc.gif", r"C:\\Users\40437\Desktop\aa")"""

from PIL import Image
from math import floor

def textture(srcText, dstSurface, dstWidth, dstHeight):
    srcTextFile = Image.open(srcText)
    dstSur = Image.new("RGB", (dstWidth, dstHeight))
    srcWidth, srcHeight = srcTextFile.size
    for w in range(dstWidth):
        for h in range(dstHeight):
            x, y = floor(w/dstWidth*srcWidth), floor(h/dstHeight*srcHeight)
            dstSur.putpixel((w,h), srcTextFile.getpixel((x,y)))
    dstSur.save(dstSurface)
    dstSur.close()
    srcTextFile.close()

textture("result.jpg", r"new.jpg", 200, 250)
