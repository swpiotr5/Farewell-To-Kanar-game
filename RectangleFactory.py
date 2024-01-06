from Rectangle import Rectangle


class RectangleFactory:
    @staticmethod
    def create_rectangle(x, y, width, height):
        return Rectangle(x, y, width, height)