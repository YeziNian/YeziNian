import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Querybox, Messagebox
db_config = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'xingxing',
        'port': 3306,
        'db': 'test'
}
import pymysql
"""root = ttk.Window(themename="darkly")
def close():
    ne = Messagebox.yesnocancel(message='sda')
    print(type(ne))
    if ne == "确认":
        root.destroy()
root.protocol("WM_DELETE_WINDOW", close)
root.place_window_center()
root.mainloop()"""
"""conn = pymysql.connect(**db_config)
with conn.cursor() as cur:
    cur.execute("SELECT admin FROM message")
    print(cur.fetchall())
conn.close()"""

#queue
"""import queue
import threading
que = queue.Queue(maxsize=1)
que.put(1, block=True, timeout=None)
def chang():
        que.put(4, block=True, timeout=None)
        que.put(3, block=True, timeout=None)
t = threading.Thread(target=chang)
t.daemon = True
#t.start()
print(que.get())
que.task_done()
que.join()
print(111)"""

import ttkbootstrap as ttk

class My_canvas(ttk.Canvas):

        def __init__(self, root):
                self.root = root
                super().__init__(root)
        def new_create(self, x1, y1, x2, y2, fill='pink'):
                lie = [x1, y1, x2, y2]
                self.create_line(*lie, fill='pink', width=10)
                return lie
import pygame
import sys
import os
from multiprocessing import Process
from PIL import Image, ImageGrab
def progress():
        root = ttk.Window(size=(400, 400), themename="darkly")
        root.place_window_center()
        root.mainloop()
if __name__ == '__main__':
        t = Process(target=progress)
        t.daemon = True
        t.start()
        pygame.init()
        screen = pygame.display.set_mode((400, 400))
        screen.fill("black")
        clock = pygame.time.Clock()
        i = 1
        while True:
                clock.tick(60)
                screen.fill("black")
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                files = os.listdir("image")
                                for file in files:
                                        os.remove("image" + fr"\{file}")
                                pygame.quit()
                                sys.exit()
                ImageGrab.grab().resize((400, 400)).save(fr"image\{i}.png")
                image = pygame.image.load(fr"image\{i}.png")
                screen.blit(image, (0, 0))
                i += 1
                pygame.display.flip()