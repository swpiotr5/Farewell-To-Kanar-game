import pygame

class Person:
    _instance = None
    player_speed = 0.3

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Person, cls).__new__(cls)
        return cls._instance

    def __init__(self, front_image_path, back_image_path, left_image_path, x, y):
        self.front_image = pygame.transform.scale(pygame.image.load(front_image_path), (30, 40))
        self.back_image = pygame.transform.scale(pygame.image.load(back_image_path), (30, 40))
        self.left_image = pygame.transform.scale(pygame.image.load(left_image_path), (30, 40))
        self.right_image = pygame.transform.flip(self.left_image, True, False)
        self.current_image = self.front_image
        self.x = x
        self.y = y
        self.initialized = True

    def draw(self, window):
        window.blit(self.current_image, (self.x, self.y))

    def move(self, direction, rectangles, passengers):
        old_x, old_y = self.x, self.y

        if direction == 'up':
            self.current_image = self.back_image
            self.y -= self.player_speed
        elif direction == 'down':
            self.current_image = self.front_image
            self.y += self.player_speed
        elif direction == 'left':
            self.current_image = self.left_image
            self.x -= self.player_speed
        elif direction == 'right':
            self.current_image = self.right_image
            self.x += self.player_speed

        if any(rectangle.collides_with(self) for rectangle in rectangles):
            self.x, self.y = old_x, old_y

        if any(passenger.collides_with(self) for passenger in passengers):
            self.x, self.y = old_x, old_y