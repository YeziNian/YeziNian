from PIL import Image, ImageGrab, ImageTk
import tkinter
import random
root = tkinter.Tk()
width = 160
height = 160
im = ImageGrab.grab(bbox=(0, 0, 800, 800))
lie = [Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270]
mark = []
for m in range(0, 5):
    for i in range(0, 5):
        bbox = (i*width, m*height, width*(i+1), height*(m+1))
        ce = im.crop(bbox)
        Rotate = random.choice(lie)
        mark.append(lie.index(Rotate))
        de = ce.transpose(Rotate)
        im.paste(de, bbox)
def fanzhuan(event):
    global ma, im
    x = event.x
    y = event.y
    width, height = 160, 160
    X, Y = x // width, y // height
    box1 = (width*X, height*Y, width*(X+1), height*(Y+1))
    ce = im.crop(box1)
    ce = ce.transpose(Image.ROTATE_90)
    #canva.update()
    im.paste(ce, box1)
    ma = ImageTk.PhotoImage(im)
    canva.create_image(0, 0, image=ma, anchor=tkinter.NW)
    """    ma = ImageTk.PhotoImage(ce)
    canva.create_image(width*X, height*Y, image=ma, anchor=tkinter.NW)"""
root.bind("<Button-1>", fanzhuan)
show = ImageTk.PhotoImage(im)
canva = tkinter.Canvas(root)
canva.pack(fill=tkinter.BOTH, expand=tkinter.YES)
canva.create_image(0, 0, image=show, anchor=tkinter.NW)
root.geometry("800x800")
root.mainloop()