import pygame
import sys
from play import play

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 600
window_height = 700
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Farewell to Kanar")

# Set up colors
BLACK = (0, 0, 0)

# Set up fonts
title_font = pygame.font.Font(None, 64)
menu_font = pygame.font.Font(None, 32)

# Render the text
title_text = title_font.render("Farewell to Kanar", True, BLACK)
start_text = menu_font.render("Press SPACE to start", True, BLACK)
quit_text = menu_font.render("Press Q to quit", True, BLACK)


# Set up menu position
title_pos = title_text.get_rect(center=(window_width // 2, window_height // 8))
start_pos = start_text.get_rect(center=(window_width // 2, window_height // 4))
quit_pos = quit_text.get_rect(center=(window_width // 2, window_height * 2.5 // 8))

background_image = pygame.image.load('menu.jpg')

FPS = 60

def draw():
    window.blit(background_image, (0, 0))
    window.blit(title_text, title_pos)
    window.blit(start_text, start_pos)
    window.blit(quit_text, quit_pos)
    pygame.display.update()

# Game loop

def main():
    clock = pygame.time.Clock()
    running = True
    in_game = False

    while running:
        clock.tick(FPS)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play()
                elif event.key == pygame.K_q:
                    # Quit the game
                    pygame.quit()
                    sys.exit()

        draw()

if __name__ == '__main__':
    main()