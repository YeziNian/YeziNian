from PIL import Image, ImageFont, ImageDraw, ImageFilter
import os
import tkinter
import threading
import random
import numpy as np
import os
#im = Image.new("RGB", (500, 500), (0, 0, 0))
#im.show()
if not os.path.isdir("data"):
    os.mkdir("data")
i = 1
image1 = None
def con(event):
    global i, image1
    width = 500
    height = 500
    while True:
        h = np.random.randint(0, 256, 3)
        im = Image.new("RGB", (width, height), tuple(h))
        im.save(r"data\{0}.png".format(i))
        image1 = tkinter.PhotoImage(file=r"data\{0}.png".format(i))
        canva.create_image(0, 0, image=image1, anchor=tkinter.NW)
        width -= 1
        height -= 1
        if width == 100:
            break
        i += 1

root = tkinter.Tk()
root.geometry("700x700")
canva = tkinter.Canvas(root)
canva.pack(fill=tkinter.BOTH, expand=tkinter.YES)
v = tkinter.PhotoImage(file=r"data\1.png")
canva.create_image(0, 0, image=v, anchor=tkinter.NW)
root.bind("<KeyPress-W>", con)
root.mainloop()
