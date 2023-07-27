import pygame
import sys
from random import randint
pygame.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 20)
screen.blit(font.render("Jack", True, (255, 0, 0), (0, 0, 0)), (0, 0))
imag = pygame.image.load(r"C:\Users\40437\Desktop\aa\1.png").convert()
rect = imag.get_rect()
screen.blit(imag, (130, 130))
screen.blit(imag, (130, 230))

print(pygame.font.match_font(pygame.font.get_fonts()[1]))
while True:
    event = pygame.event.wait()
    site = [0, 0]
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pygame.display.flip()
        print(event)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            site[1] -= 8
            pygame.draw.aalines(screen, (255, 0, 0), True, [[100, 20], [200, 30], [400, 100]], blend=1) #closed 表示首位相连
            """ # 绘制一个灰色的矩形区域，以灰色填充区域
            pygame.draw.rect(screen, (155, 155, 155), (75, 10, 50, 20), 0)
            """#最后一个参数为width默认为0表示填充区域 否则为线框宽度
        """# 绘制一个圆弧,其中0表示弧线的开始位置，pi/2表示弧线的结束位置，2表示线宽
        pygame.draw.arc(screen, (255, 10, 0), (210, 75, 150, 125), 0, pi / 2, 2)"""
        if event.key == pygame.K_DOWN:
            site[1] += 8
        if event.key == pygame.K_LEFT:
            site[0] -= 8
        if event.key == pygame.K_RIGHT:
            site[0] += 8
    """if event.type == pygame.MOUSEMOTION:
        mx, my = event.pos
        # 随机生成 RGB 颜色值
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        pygame.draw.circle(screen, (r, g, b,), (mx, my), 50)
        # 处理完，更新显示
        pygame.display.update()"""

    rect = rect.move(site)
    #print(rect)
    #screen.fill("white")
    #screen.blit(imag, rect)
    pygame.display.flip()