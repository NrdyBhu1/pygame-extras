from extras import nbcolors, nbfunctions
import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame Extras")


def draw():
    win.fill(nbcolors.BLACK)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           nbfunctions.terminate()

    draw()
    pygame.display.flip()
