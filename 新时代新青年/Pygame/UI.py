import tkinter
import tkinter.messagebox
import tkinter.filedialog
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pygame
import sys
class GUI:

    def __init__(self):
        self.root = tkinter.Tk()
        self.width, self.height = 300, 300
        self.root.title("Yezi")
        self.root.geometry("{0}x{1}+{2}+{3}".format(self.width, self.height,
        (self.root.winfo_screenwidth()-self.width)//2,
        (self.root.winfo_screenheight()-self.height)//2))

        self.root.mainloop()
class Mysqrit(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.pos = image.get_rect()
        self.pos.x = x
        self.pos.y = y
    def update(self):
        pass

pygame.init()
screen = pygame.display.set_mode((500, 500), flags=pygame.RESIZABLE)
screen.fill("white")
f = pygame.font.Font(r'C:/Windows/Fonts/simhei.ttf', 20)
#f.set_bold(True) #加粗
f.set_italic(True) #倾斜
text = f.render("He", True, (0, 255, 0), (0, 0, 0))
surface = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
#surface.fill("pink")
surface.blit(text, (0, 0))
image = pygame.image.load(r"C:\Users\40437\Desktop\cc.bmp").convert()
image.fill((0,0,255),rect=(100,100,100,50),special_flags=0)

new_image = image.subsurface((0, 0, 20, 20)) #抠图
#surface.scroll(10, 20)
#surface.scroll(100, 20)
clock = pygame.time.Clock()
i = 0
def han():
    global i
    imag = pygame.image.load(r"C:\Users\40437\Desktop\aa\{0}.png".format(i)).convert()
    i += 1
    if i == 11:
        i = 0
    return pygame.transform.scale(imag, (300, 300))
while True:
    clock.tick(20)
    data = han()
    screen.blit(data, (100, 100))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(surface, (0, 0))
            #ee = pygame.transform.rotate(surface, 70)
            ee = pygame.transform.scale(surface, (100, 100))
            #ee = pygame.transform.rotozoom(surface, 0, 0.5)
            #t1 = pygame.time.wait(3000)
            #print(t1)
            #screen.blit(ee, (80, 80))
            #print(pygame.time.get_ticks())
            #screen.blit(image, (60, 60))
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(chr(event.key))
    pygame.display.flip()