from LookFrontStrategy import LookFrontStrategy
from LookSideStrategy import LookSideStrategy
import pygame
import random

class TicketController:
    def __init__(self, left_image_path, front_image_path, x, y):
        self.left_image = pygame.transform.scale(pygame.image.load(left_image_path), (40, 60))
        self.front_image = pygame.transform.scale(pygame.image.load(front_image_path), (40, 60))
        self.is_looking = False
        self.x = x
        self.y = y

        self.strategy = LookSideStrategy(self) if not self.is_looking else LookFrontStrategy(self)
        self.current_image = self.strategy.update()

    def draw(self, window):
        window.blit(self.current_image, (self.x, self.y))

    def update(self):
        if random.random() < 0.000347:  
            self.is_looking = not self.is_looking
            if self.is_looking:
                self.strategy = LookFrontStrategy(self)
            else:
                self.strategy = LookSideStrategy(self)
        self.strategy.update()

    def check_person(self, person, safe_zones):
        if self.is_looking:
            for zone in safe_zones:
                if zone.contains(person.x, person.y):
                    return False  
            return True  
