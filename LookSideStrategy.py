from TicketStrategy import TicketStrategy


class LookSideStrategy(TicketStrategy):
    def __init__(self, controller):
        self.controller = controller

    def update(self):
        self.controller.current_image = self.controller.left_image
