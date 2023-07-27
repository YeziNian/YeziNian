import pygame
import sys
from PIL import Image
pygame.init()
screen = pygame.display.set_mode((500, 500))
feiji = pygame.image.load(r"C:\Users\40437\Desktop\feiji\model_1.png").convert()
feiji = pygame.transform.scale(feiji, (30, 30))
#data = Image.open(r"C:\Users\40437\Desktop\feiji\model_1.png").resize((30, 30))
#data.save(r"C:\Users\40437\Desktop\heh.png")
size = feiji.get_rect()
size.center = (250, 250)
screen.blit(feiji, size)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                size[1] -= 28
            elif event.key == pygame.K_DOWN:
                size[1] += 28
            elif event.key == pygame.K_LEFT:
                size[0] -= 28
            elif event.key == pygame.K_RIGHT:
                size[0] += 28

        elif event.type == pygame.ACTIVEEVENT:
            pass
    screen.fill("black")
    screen.blit(feiji, size)
    pygame.display.flip()