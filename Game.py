import random
from RectangleFactory import RectangleFactory
from SafeZone import SafeZone
import pygame
import sys
from Person import Person
from TicketController import TicketController
from Goal import Goal
from PassengersFactory import PassengersFactory
from PassengerZone import PassengerZone


window_width = 600
window_height = 700

class Game:
    def __init__(self):
        pygame.init()
        self.background_image = pygame.image.load('assets/interior.jpg')
        self.font = pygame.font.Font(None, 36)
        self.person = Person('assets/front.png', 'assets/back.png', 'assets/left.png', window_width // 4, window_height // 1.35)
        self.window = pygame.display.set_mode((window_width, window_height))
        self.ticket_controller = TicketController("assets/kanar-left.png", "assets/kanar-front.png", 200, 120)
        self.rectangles = self.create_rectangles()
        self.passenger_zones = self.create_passenger_zones()
        self.selected_zones = random.sample(self.passenger_zones, len(self.passenger_zones) // 3)
        self.passenger_factory = PassengersFactory()
        self.passengers = self.create_passengers()
        self.goal = Goal(0, 0, 50, 100)
        self.spotted_text = self.font.render("You've been spotted by Kanar!", True, (255, 0, 0))
        self.timeout_text = self.font.render("You didn't get off the bus in time. Kanar got you. ", True, (255, 0, 0))
        self.text_surface = self.font.render("Kanar has been defeated", True, (0, 255, 0))
        self.spotted = False
        self.running = True
        self.start_ticks = pygame.time.get_ticks()
        self.safe_zones  = [
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
    
    def create_rectangles(self):
        factory = RectangleFactory()
        return [
            factory.create_rectangle(70, 130, 1, 800),
            factory.create_rectangle(70, 0, 1, 30),
            factory.create_rectangle(520, 0, 1, 800),
            factory.create_rectangle(0, 0, 600, 1),
            factory.create_rectangle(0, 700, 600, 1),
            factory.create_rectangle(90, 280, 120, 1),
            factory.create_rectangle(90, 130, 110, 1),
            factory.create_rectangle(90, 360, 120, 1),
            factory.create_rectangle(92, 485, 110, 1),
            factory.create_rectangle(92, 580, 110, 1),
            factory.create_rectangle(360, 595, 150, 1),
            factory.create_rectangle(370, 467, 127, 1),
            factory.create_rectangle(365, 340, 130, 1),
            factory.create_rectangle(370, 263, 140, 1),
            factory.create_rectangle(370, 145, 130, 1),
        ]

    def create_passenger_zones(self):
        return [PassengerZone(360, -40, 50, 50), PassengerZone(430, -40, 50, 50), PassengerZone(360, 60, 50, 50), PassengerZone(430, 60, 50, 50), PassengerZone(360, 110, 50, 50), PassengerZone(430, 110, 50, 50), PassengerZone(360, 170, 50, 50), PassengerZone(430, 170, 50, 50), PassengerZone(360, 330, 50, 50), PassengerZone(430, 330, 50, 50), PassengerZone(360, 390, 50, 50), PassengerZone(430, 390, 50, 50), PassengerZone(360, 440, 50, 50), PassengerZone(430, 440, 50, 50), PassengerZone(360, 500, 50, 50), PassengerZone(430, 500, 50, 50), PassengerZone(70, 345, 50, 50), PassengerZone(120, 345, 50, 50), PassengerZone(70, 410, 50, 50), PassengerZone(120, 410, 50, 50)]  
   
    def create_passengers(self):
        passenger_zones = self.create_passenger_zones()
        selected_zones = random.sample(passenger_zones, len(passenger_zones) // 3)
        passenger_factory = PassengersFactory()  # Tworzenie fabryki pasażerów
        passengers = []
        for zone in selected_zones:
            x, y = zone.center_position()
            passengers.append(passenger_factory.create_passenger(x, y))
        
        fixed_passenger = passenger_factory.create_passenger(150, 120)
        passengers.append(fixed_passenger)
        return passengers

    def play(self):
        while self.running:
            self.handle_events()
            self.update_game_state()
            self.draw_game_state()
            self.check_game_over_conditions()
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.spotted:
                    self.running = False

    def update_game_state(self):
        if not self.spotted:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.person.move('up', self.rectangles, self.passengers)
            if keys[pygame.K_s]:
                self.person.move('down', self.rectangles, self.passengers)
            if keys[pygame.K_a]:
                self.person.move('left', self.rectangles, self.passengers)
            if keys[pygame.K_d]:
                self.person.move('right', self.rectangles, self.passengers)

    def draw_game_state(self):
        self.window.blit(self.background_image, (0, 0))
        self.person.draw(self.window)
        if not self.spotted:
            self.ticket_controller.update()
        self.ticket_controller.draw(self.window)
        self.goal.draw(self.window)
        for zone in self.safe_zones:
            if zone.contains(self.person.x, self.person.y):
                text = self.font.render("Safe Zone", True, (255, 255, 255))
                self.window.blit(text, (10, 10))  
                break
        for rectangle in self.rectangles:
            rectangle.draw(self.window)
        for passenger in self.passengers:
            passenger.draw(self.window)

    def check_game_over_conditions(self):
        self.spotted = self.ticket_controller.check_person(self.person, self.safe_zones)
        if self.spotted:
            self.window.blit(self.spotted_text, (self.window.get_width() / 2 - self.spotted_text.get_width() / 2, self.window.get_height() / 2 - self.spotted_text.get_height() / 2)) 
        if self.goal.collides_with(self.person):
            x = (self.window.get_width() - self.text_surface.get_width()) / 2
            y = (self.window.get_height() - self.text_surface.get_height()) / 2
            self.window.blit(self.text_surface, (x, y))
            pygame.display.update()  
            pygame.time.wait(2000)  
            self.running = False
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000 
        if seconds > 60:
            self.window.blit(self.timeout_text, (self.window.get_width() / 2 - self.timeout_text.get_width() / 2, self.window.get_height() / 2 - self.timeout_text.get_height() / 2)) 
            pygame.display.update()
            pygame.time.wait(7000)  
            self.running = False
        timer_text = self.font.render(str(int(60 - seconds)), True, (255, 255, 255))  
        self.window.blit(timer_text, (self.window.get_width() - timer_text.get_width(), 0))  