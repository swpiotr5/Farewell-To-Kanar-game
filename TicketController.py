import pygame
import random

class TicketController:
    def __init__(self, left_image_path, front_image_path, x, y):
        self.left_image = pygame.transform.scale(pygame.image.load(left_image_path), (40, 60))
        self.front_image = pygame.transform.scale(pygame.image.load(front_image_path), (40, 60))
        self.current_image = self.left_image
        self.is_looking = False
        self.x = x
        self.y = y

    def draw(self, window):
        window.blit(self.current_image, (self.x, self.y))

    def update(self):
        # Randomly decide whether to look front or to the side
        if random.random() < 0.000347:  # 5% chance to change direction
            self.is_looking = not self.is_looking
            self.current_image = self.front_image if self.is_looking else self.left_image

    def check_person(self, person, safe_zones):
        if self.is_looking:
            for zone in safe_zones:
                if zone.contains(person.x, person.y):
                    return False  # Person is safe, do nothing
            return True  # Person is not in a safe zone, return True
