from extras import nbcolors, nbfunctions, nbclasses
import pygame
from pygame.locals import *

pygame.init()

nbfunctions.set_pointer_cursor("xbm-cursors/cursor-mouse.xbm", "xbm-cursors/cursor-mouse-mask.xbm")

win = pygame.display.set_mode((1366, 768), FULLSCREEN)
pygame.display.set_caption("Pygame Extras")

test_button = nbclasses.Button(10, 650, 200, 100, nbfunctions.terminate, text="Quit", color=(100, 0, 0), intensity=50)
test_text = nbfunctions.get_text("hello world", 30, True, nbcolors.GREEN)

def draw():
    win.fill(nbcolors.BLACK)
    win.blit(test_text, (20, 20))
    test_button.blit(win)

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                nbfunctions.terminate()

    draw()
    test_button.update()
    pygame.display.flip()
