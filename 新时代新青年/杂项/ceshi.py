import os

import ttkbootstrap as ttk
import threading
from PIL import ImageGrab, ImageTk
from ttkbootstrap.constants import *
import time
def che(canvas):
    i = 1
    while True:
        ImageGrab.grab().resize((400, 400)).save(f"image\{i}.png")
        image = ttk.PhotoImage(file=fr"image\{i}.png")
        #canvas.delete("all")
        canvas.create_image((0, 0), image=image, anchor=NW)
        time.sleep(0.1)
        i += 1
        root.update_idletasks()
root = ttk.Window(size=(400, 400), overrideredirect=False)
root.place_window_center()
canva = ttk.Canvas(root)
canva.pack(fill=BOTH, expand=YES)
t = threading.Thread(target=che, args=(canva, ))
t.daemon = True
t.start()
def closing():
    for k in os.listdir("image"):
        os.remove("image" + "\\" + k)
    root.destroy()
root.protocol("WM_DELETE_WINDOW", closing)
root.mainloop()

class Myde:
    def __init__(self, interval=0.1):
        self.root = ttk.Window()
        self.root.geometry("400x400")
        self.root.option_add("*tearOff", False)
        self.canvas = ttk.Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.photo = None  # 用于存储当前图像

        t = threading.Thread(target=self.heh)
        t.daemon = True
        t.start()

        self.root.mainloop()

    def heh(self):
        while True:
            image = ImageGrab.grab().resize((300, 300))
            photo = ImageTk.PhotoImage(image)

            self.canvas.delete("all")  # 清除画布上之前的内容
            self.canvas.create_image(0, 0, image=photo, anchor=NW)  # 在画布上放置新图像

            self.photo = photo  # 更新当前图像
            time.sleep(0.1)

