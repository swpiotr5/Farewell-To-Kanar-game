import pygame
import sys


window_width = 600
window_height = 700
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Farewell to Kanar")

BLACK = (0, 0, 0)

class Rectangle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        pygame.draw.rect(window, BLACK, self.rect)

    def collides_with(self, person):
        person_rect = pygame.Rect(person.x, person.y, person.current_image.get_width(), person.current_image.get_height())
        return self.rect.colliderect(person_rect)

class Person:
    player_speed = 0.2

    def __init__(self, front_image_path, back_image_path, left_image_path, x, y):
        self.front_image = pygame.transform.scale(pygame.image.load(front_image_path), (30, 40))
        self.back_image = pygame.transform.scale(pygame.image.load(back_image_path), (30, 40))
        self.left_image = pygame.transform.scale(pygame.image.load(left_image_path), (30, 40))
        self.right_image = pygame.transform.flip(self.left_image, True, False)
        self.current_image = self.front_image
        self.x = x
        self.y = y

    def draw(self, window):
        window.blit(self.current_image, (self.x, self.y))

    def move(self, direction, rectangles):
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

def create_rectangles():
    return [
        Rectangle(70, 130, 1, 800),
        Rectangle(70, 0, 1, 30),
        Rectangle(520, 0, 1, 800),
        Rectangle(0, 0, 600, 1),
        Rectangle(0, 700, 600, 1),
        Rectangle(90, 280, 120, 1),
        Rectangle(90, 130, 110, 1),
        Rectangle(90, 360, 120, 1),
        Rectangle(92, 485, 110, 1),
        Rectangle(92, 580, 110, 1),
        Rectangle(360, 595, 150, 1),
        Rectangle(370, 467, 127, 1),
        Rectangle(365, 340, 130, 1),
        Rectangle(370, 263, 140, 1),
        Rectangle(370, 145, 130, 1)
    ]

class SafeZone:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def contains(self, x, y):
        return self.rect.collidepoint(x, y)

safe_zones = [
    SafeZone(90, 340, 110, 50),
    SafeZone(90, 420, 110, 50),
    SafeZone(370, 145, 130, 30),
    SafeZone(370, 185, 130, 40),
    SafeZone(360, 500, 150, 50),
    SafeZone(360, 430, 150, 50),
    SafeZone(92, 500, 110, 40),
]

def play():
    pygame.init()

    background_image = pygame.image.load('interior.jpg')
    font = pygame.font.Font(None, 36)
    person = Person('front.png', 'back.png', 'left.png', window_width // 4, window_height // 1.35)
    rectangles = create_rectangles()

    running = True
    while running:
        window.blit(background_image, (0, 0))
        person.draw(window)
        for zone in safe_zones:
            if zone.contains(person.x, person.y):
                text = font.render("Safe Zone", True, (255, 255, 255))
                window.blit(text, (10, 10))  
                break

        for rectangle in rectangles:
            rectangle.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            person.move('up', rectangles)
        if keys[pygame.K_s]:
            person.move('down', rectangles)
        if keys[pygame.K_a]:
            person.move('left', rectangles)
        if keys[pygame.K_d]:
            person.move('right', rectangles)

        pygame.display.update()