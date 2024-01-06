import random
import pygame

class Passenger:
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.rect = pygame.Rect(x, y, 30, 50) 

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
    
    def collides_with(self, person):
        person_rect = pygame.Rect(person.x, person.y, person.current_image.get_width(), person.current_image.get_height())
        return self.rect.colliderect(person_rect)