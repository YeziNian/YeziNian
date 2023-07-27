import pygame

print(pygame.font.get_fonts())
print(pygame.font.match_font(pygame.font.get_fonts()[2]))
font = pygame.font.SysFont(pygame.font.match_font(pygame.font.get_fonts()[2]), 12)
