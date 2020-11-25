from extras import nbcolors, nbfunctions, nbclasses
import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((1366, 768), FULLSCREEN)
pygame.display.set_caption("Pygame Extras")

player_rect = pygame.Rect(20, 700, 100, 25)

test_button = nbclasses.Button(300, 400, 200, 100, intensity=45)
test_text = nbfunctions.get_text("hello world", 30, True, nbcolors.GREEN)

def draw():
    win.fill(nbcolors.BLACK)
    pygame.draw.rect(win, nbcolors.CYAN, player_rect)
    win.blit(test_text, (20, 20))
    test_button.blit(win)
    test_button.update()

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                nbfunctions.terminate()

    draw()
    pygame.display.flip()
