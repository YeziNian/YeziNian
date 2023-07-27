import pygame

pygame.init()

# 创建一个窗口和 surface 对象
WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
surface = pygame.Surface((300, 100))
screen.fill("white")
# 创建一个字体对象
font = pygame.font.SysFont("arial", 32)

# 创建一个文本 surface 对象
text_surface = font.render("Hello, world!", True, (255, 255, 255))

# 将文本 surface 绘制到我们创建的 surface 上
surface.blit(text_surface, (0, 0))
surface.fill("black")
# 将 surface 对象绘制到屏幕上
screen.blit(surface, (170, 190))

# 刷新屏幕
pygame.display.flip()

# 等待退出
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()