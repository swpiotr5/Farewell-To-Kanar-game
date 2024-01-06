import random
import pygame
from Passenger import Passenger

class PassengersFactory:
    @staticmethod
    def create_passenger(x, y):
        image_path = random.choice(['assets/passenger1.png', 'assets/passenger2.png', 'assets/passenger3.png', 'assets/passenger4.png'])
        image = pygame.transform.scale(pygame.image.load(image_path), (30, 50))
        return Passenger(x, y, image)