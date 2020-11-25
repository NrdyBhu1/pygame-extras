import pygame
pygame.init()

class Button():
    def __init__(self, x, y, width, height, color=(180, 180, 180), intensity=20):
        self.is_pressed = False
        self.is_hovered = False
        self.x = x
        self.y = y
        self.color = color
        self.normal = color
        self.hover = (color[0]+intensity, color[1]+intensity, color[2]+intensity)
        self.rect = pygame.Rect(self.x, self.y, width, height)

    def blit(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover
            self.is_hovered = True
        else:
            self.is_hovered = False
            self.color = self.normal

