import pygame

class Goal:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), self.rect)  # Draw the goal as a green rectangle

    def collides_with(self, person):
        person_rect = pygame.Rect(person.x, person.y, person.current_image.get_width(), person.current_image.get_height())
        return self.rect.colliderect(person_rect)