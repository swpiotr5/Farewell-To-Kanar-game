import random
from TicketStrategy import TicketStrategy


class LookFrontStrategy(TicketStrategy):
    def __init__(self, controller):
        self.controller = controller

    def update(self):
        self.controller.current_image = self.controller.front_image
