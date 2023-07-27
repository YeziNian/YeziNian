import pygame
from PIL import Image
import sys
from random import randint
import threading
import time
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
class My(pygame.sprite.Sprite):

    def __init__(self, filename, location):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = location

class Mythread(threading.Thread):
    step = 1
    def __init__(self):
        super().__init__()
        self.rand = randint(0, 500)
        self.zidan = My(r"C:\Users\40437\Desktop\feiji\model_3.png", (self.rand, 0))
        self.rect = self.zidan.rect

    def run(self):
        i = 1
        while True:
            clock.tick(20)
            self.rect = self.rect.move((0, 10))
            screen.fill("black")
            screen.blit(self.zidan.image, self.rect)
            pygame.display.flip()
            i += 1
            if i == 51:
                break

feiji = My(r"C:\Users\40437\Desktop\feiji\model_1.png", (210, 400))
zidan = My(r"C:\Users\40437\Desktop\feiji\model_3.png", (20, 0))
font = pygame.font.Font(r'C:/Windows/Fonts/simhei.ttf', 30)
score = 0
rec = zidan.rect
bullet = []
enemy = []
d = 10
screen.fill("black")
rect = feiji.rect
screen.blit(feiji.image, rect)
pygame.display.flip()
"""m = Mythread()
m.daemon = True
m.start()"""
pause = None
while True:
    clock.tick(40)
    size = [0, 0]
    screen.fill("black")
    rec = rec.move((0, d))
    #event = pygame.event.wait()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                size[1] -= 28
            elif event.key == pygame.K_s:
                size[1] += 28
            elif event.key == pygame.K_a:
                size[0] -= 28
            elif event.key == pygame.K_d:
                size[0] += 28
            elif event.key == pygame.K_SPACE:
                bullet.append([rect[0]+15, rect[1]-8, 20, 10])
        elif event.type == pygame.WINDOWFOCUSLOST:
            text = font.render("游戏已暂停!!", True, (255, 0, 0), (0, 0, 0))
            screen.blit(text, text.get_rect(center=(250, 250)))

    if len(enemy) <= 3:
        enemy.append([randint(0, 500), 0, 40, 40])
    if enemy:
        for k in enemy:
            k[1] += 1
            if k[1] >= 500:
                enemy.remove(k)
    for k in enemy:
        pygame.draw.rect(screen, (100, 100, 100), rect=k)
    rect = rect.move(size)
    for m in enemy:
        if bullet:
            if m[0] <= bullet[0][0] and bullet[0][0] <= (m[0] + 40):
                if m[1]+40 >= bullet[0][1]:
                    enemy.remove(m)
                    bullet.clear()
                    score += 1
    if bullet:
        pygame.draw.circle(screen, (0, 255, 0), center=bullet[0][:2], radius=5)
        bullet[0][1] -= 10
        if bullet[0][1] <= 0:
            bullet.clear()
    text = font.render("Score:" + str(score), True, (255, 0, 0), (0, 0, 0))
    screen.blit(text, (0, 0))
    screen.blit(feiji.image, rect)
    pygame.display.flip()