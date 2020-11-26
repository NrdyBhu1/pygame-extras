from extras import nbcolors, nbfunctions, nbclasses
import pygame
from pygame.locals import *

pygame.init()

nbfunctions.pointer_cursor = pygame.cursors.load_xbm("custom/dnd-move_1.xbm")

win = pygame.display.set_mode((1366, 768), FULLSCREEN)
pygame.display.set_caption("Pygame Extras")

test_button = nbclasses.Button(10, 650, 200, 100, nbfunctions.terminate, text="Quit", color=(100, 0, 0), intensity=50)
test_text = nbfunctions.get_text("hello world", 30, True, nbcolors.GREEN)

selected = False
mouse_pos = (0, 0)
text_pos = test_text.get_rect()

def draw():
    win.fill(nbcolors.BLACK)
    pygame.draw.rect(win, nbcolors.CYAN, text_pos)
    win.blit(test_text, text_pos)
    test_button.blit(win)

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                nbfunctions.terminate()
        elif event.type == MOUSEBUTTONDOWN:
            if text_pos.collidepoint(mouse_pos) and not selected:
                selected = True
            elif selected:
                selected = False
        elif event.type == pygame.MOUSEMOTION:
            if selected:
                text_pos.center = mouse_pos


    draw()
    test_button.update()
    pygame.display.flip()
