

from TicketStrategy import TicketStrategy


class TicketControllerDecorator(TicketStrategy):
    def __init__(self, decorated_strategy):
        self.decorated_strategy = decorated_strategy

    def update(self):
        pass