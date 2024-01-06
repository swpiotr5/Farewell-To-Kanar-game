import pygame

class SafeZone:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def contains(self, x, y):
        return self.rect.collidepoint(x, y)