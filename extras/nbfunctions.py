import pygame
import sys

pygame.init()

global default_cursor, pointer_cursor
default_cursor = pygame.cursors.tri_left
pointer_cursor = pygame.cursors.broken_x

def terminate():
    pygame.quit()
    sys.exit()

def get_text(text, font_size=30, display=True, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, font_size)
    txt = font.render(text, display,  color, None)
    return txt

def get_pointer_cursor():
    return pointer_cursor

def get_default_cursor():
    return default_cursor
