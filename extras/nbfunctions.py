import pygame
import sys

pygame.init()

def terminate():
    pygame.quit()
    sys.exit()

def get_text(text, font_size=30, display=True, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, font_size)
    txt = font.render(text, display,  color, None)
    return txt
