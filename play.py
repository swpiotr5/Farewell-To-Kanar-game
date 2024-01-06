import pygame
import sys
import random


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
    player_speed = 0.3

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
        Rectangle(370, 145, 130, 1),
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
    SafeZone(350, 70, 130, 50),
    SafeZone(350, 0, 130, 20),
    SafeZone(350, 330, 130, 50),
    SafeZone(350, 400, 130, 50),
]

class Passenger:
    def __init__(self, x, y):
        self.image_path = random.choice(['passenger1.png', 'passenger2.png', 'passenger3.png', 'passenger4.png'])
        self.image = pygame.transform.scale(pygame.image.load(self.image_path), (30, 50))
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

class PassengerZone:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def center_position(self):
        x = self.x + self.width // 2;
        y = self.y + self.height // 2;
        return x, y

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

class Goal:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), self.rect)  # Draw the goal as a green rectangle

    def collides_with(self, person):
        person_rect = pygame.Rect(person.x, person.y, person.current_image.get_width(), person.current_image.get_height())
        return self.rect.colliderect(person_rect)

def play():
    pygame.init()

    background_image = pygame.image.load('interior.jpg')
    font = pygame.font.Font(None, 36)
    person = Person('front.png', 'back.png', 'left.png', window_width // 4, window_height // 1.35)
    ticket_controller = TicketController("kanar-left.png", "kanar-front.png", 200, 120)
    
    rectangles = create_rectangles()


    passenger_zones = [PassengerZone(360, -40, 50, 50), PassengerZone(430, -40, 50, 50), PassengerZone(360, 60, 50, 50), PassengerZone(430, 60, 50, 50), PassengerZone(360, 110, 50, 50), PassengerZone(430, 110, 50, 50), PassengerZone(360, 170, 50, 50), PassengerZone(430, 170, 50, 50), PassengerZone(360, 330, 50, 50), PassengerZone(430, 330, 50, 50), PassengerZone(360, 390, 50, 50), PassengerZone(430, 390, 50, 50), PassengerZone(360, 440, 50, 50), PassengerZone(430, 440, 50, 50), PassengerZone(360, 500, 50, 50), PassengerZone(430, 500, 50, 50), PassengerZone(70, 345, 50, 50), PassengerZone(120, 345, 50, 50), PassengerZone(70, 410, 50, 50), PassengerZone(120, 410, 50, 50)]  # Create passenger zones

    selected_zones = random.sample(passenger_zones, len(passenger_zones) // 3)

    passengers = []
    for zone in selected_zones:
        x, y = zone.center_position()
        passengers.append(Passenger(x, y))
    
    fixed_passenger = Passenger(150, 120)  # Replace with the desired coordinates
    passengers.append(fixed_passenger)

    goal = Goal(0, 0, 50, 100)

    font = pygame.font.Font(None, 36)  # Create a font
    spotted_text = font.render("You've been spotted by Kanar!", True, (255, 0, 0))  # Red text
    timeout_text = font.render("You didn't get off the bus in time. Kanar got you.", True, (255, 0, 0))  # Red text
    text_surface = font.render("Kanar was defeated", True, (0, 255, 0))  # White text

    spotted = False  # Flag to indicate whether the player has been spotted
    running = True
    start_ticks = pygame.time.get_ticks()  # Starter tick
    while running:
        window.blit(background_image, (0, 0))
        person.draw(window)
        if not spotted:
            ticket_controller.update()
        ticket_controller.draw(window)
        spotted = ticket_controller.check_person(person, safe_zones)
        if spotted:
            window.blit(spotted_text, (window.get_width() / 2 - spotted_text.get_width() / 2, window.get_height() / 2 - spotted_text.get_height() / 2))  # Draw the text in the center of the screen

        goal.draw(window)

        if goal.collides_with(person):
            # Calculate the position to center the text
            x = (window.get_width() - text_surface.get_width()) / 2
            y = (window.get_height() - text_surface.get_height()) / 2

            # Draw the text on the screen
            window.blit(text_surface, (x, y))

            pygame.display.update()  # Update the display to show the text
            pygame.time.wait(2000)  # Wait two seconds
            running = False

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Calculate how many seconds
        if seconds > 60:  # If more than 120 seconds
            window.blit(timeout_text, (window.get_width() / 2 - timeout_text.get_width() / 2, window.get_height() / 2 - timeout_text.get_height() / 2))  # Draw the text in the center of the screen
            pygame.display.update()
            pygame.time.wait(7000)  # Wait two seconds
            running = False

        timer_text = font.render(str(int(60 - seconds)), True, (255, 255, 255))  # White text
        window.blit(timer_text, (window.get_width() - timer_text.get_width(), 0))  # Draw the text in the top right corner

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and spotted:
                    running = False

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
        
        for passenger in passengers:
            passenger.draw(window)

        if not spotted:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                person.move('up', rectangles, passengers)
            if keys[pygame.K_s]:
                person.move('down', rectangles, passengers)
            if keys[pygame.K_a]:
                person.move('left', rectangles, passengers)
            if keys[pygame.K_d]:
                person.move('right', rectangles, passengers)

        pygame.display.update()