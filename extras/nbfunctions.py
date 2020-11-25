import pygame
import sys

pygame.init()

global default_cursor, pointer_cursor
default_cursor = pygame.cursors.arrow
pointer_cursor = pygame.cursors.diamond

def terminate():
    pygame.quit()
    sys.exit()

def get_text(text, font_size=30, display=True, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, font_size)
    txt = font.render(text, display,  color, None)
    return txt

def set_default_cursor(cursor, mask):
    default_cursor = pygame.cursors.load_xbm(cursor, mask)

def set_pointer_cursor(cursor, mask):
    pointer_cursor = pygame.cursors.load_xbm(cursor, mask)

def get_pointer_cursor():
    return pointer_cursor

def get_default_cursor():
    return default_cursor
