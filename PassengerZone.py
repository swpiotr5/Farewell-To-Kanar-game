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