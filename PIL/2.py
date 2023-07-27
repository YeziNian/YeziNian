from PIL import Image

def qipan(filename, width, height, color1, color2):
    im = Image.new("RGB", (width, height))
    for h in range(height):
        for w in range(width):
            if (int(h/height*8)+int(w/width*8)) % 2 == 0:
                im.putpixel((w,h), color1)
            else:
                im.putpixel((w, h), color2)
    im.save(filename)
if __name__ == '__main__':
    filename = r"C:\Users\40437\Desktop\aa.png"
    qipan(filename, 500, 500, (128, 128, 128), (10, 10, 10))