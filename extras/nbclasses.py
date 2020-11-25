import pygame
from . import nbfunctions, nbcolors
pygame.init()

class Button():
    def __init__(self, x, y, width, height, function, text="button", color=(180, 180, 180), intensity=20):
        self.is_pressed = False
        self.is_hovered = False
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.function = function
        self.normal = color
        self.hover = (color[0]+intensity, color[1]+intensity, color[2]+intensity)
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.rendered_text = nbfunctions.get_text(self.text, self.rect.height-2, True, nbcolors.WHITE)
        self.rendered_textbox = self.rendered_text.get_rect()


    def blit(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        self.rendered_textbox.center = self.rect.center
        win.blit(self.rendered_text, self.rendered_textbox)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover
            self.is_hovered = True
            pygame.mouse.set_cursor(*nbfunctions.get_pointer_cursor())
        else:
            self.is_hovered = False
            self.color = self.normal
            pygame.mouse.set_cursor(*nbfunctions.get_default_cursor())


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_hovered:
                    self.function()

