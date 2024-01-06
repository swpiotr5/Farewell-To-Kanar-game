from Game import Game
import pygame
import sys

class MainMenu:
    def __init__(self):
        pygame.init()
        self.window_width = 600
        self.window_height = 700
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Farewell to Kanar")
        self.BLACK = (0, 0, 0)
        self.title_font = pygame.font.Font(None, 64)
        self.menu_font = pygame.font.Font(None, 32)
        self.title_text = self.title_font.render("Farewell to Kanar", True, self.BLACK)
        self.start_text = self.menu_font.render("Press SPACE to start", True, self.BLACK)
        self.quit_text = self.menu_font.render("Press Q to quit", True, self.BLACK)
        self.title_pos = self.title_text.get_rect(center=(self.window_width // 2, self.window_height // 8))
        self.start_pos = self.start_text.get_rect(center=(self.window_width // 2, self.window_height // 4))
        self.quit_pos = self.quit_text.get_rect(center=(self.window_width // 2, self.window_height * 2.5 // 8))
        self.background_image = pygame.image.load('assets/menu.jpg')
        self.FPS = 60

    def draw(self):
        self.window.blit(self.background_image, (0, 0))
        self.window.blit(self.title_text, self.title_pos)
        self.window.blit(self.start_text, self.start_pos)
        self.window.blit(self.quit_text, self.quit_pos)
        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game = Game()
                        game.play()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            self.draw()


if __name__ == '__main__':
    menu = MainMenu()
    menu.run()