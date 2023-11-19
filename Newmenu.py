import pygame
import sys
from main import Game
from settings import *
# Add this import statement in Newmenu.py




# Constants for colors
WHITE = (0, 0, 0)
RED = (255, 0, 0)

# Constants for menu states
MAIN_MENU = 0
GAME_PLAY = 1
ONLINE = 2
OPTIONS = 3
EXIT = 4

# Initialize Pygame
pygame.init()

# Set up the display
width, height = RES
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Menu Selection')

# Menu options and their positions
menu_images = {
    MAIN_MENU: "resources\\font family\\1.png",
    GAME_PLAY: "resources\\font family\\2.png",
    ONLINE: "resources\\font family\\3.png",
    OPTIONS: "resources\\font family\\4.png",
    EXIT: "resources\\font family\\5.png",
}

# Fixed positions for menu options
menu_position = {
    MAIN_MENU: (width // 2, height // 2 - 200),
    GAME_PLAY: (width // 2, height // 2),
    ONLINE: (width // 2, height // 2 + 100),
    OPTIONS: (width // 2, height // 2 + 200),
    EXIT: (width // 2, height // 2 + 300),
}

current_option = GAME_PLAY  # Starting menu option

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_option -= 1
                if current_option < GAME_PLAY:
                    current_option = EXIT
            elif event.key == pygame.K_DOWN:
                current_option += 1
                if current_option > EXIT:
                    current_option = GAME_PLAY
            elif event.key == pygame.K_RETURN:
                if current_option == MAIN_MENU:
                    print("Selected Main Menu")
                elif current_option == GAME_PLAY:
                    game = Game()
                    game.run()
                elif current_option == ONLINE:
                    print("Selected Online")
                elif current_option == OPTIONS:
                    print("Selected Options")
                elif current_option == EXIT:
                    print("Exiting the application")
                    running = False

    # Render the menu options with PNG images
    for option, image_path in menu_images.items():
        image = pygame.image.load(image_path)
        image_rect = image.get_rect(center=menu_position[option])
        screen.blit(image, image_rect)

    # Add a highlight rectangle behind the selected option
    highlight_rect = pygame.Rect(0, 0, 700, 100)  # Adjust the rectangle size based on your images
    highlight_rect.center = menu_position[current_option]
    pygame.draw.rect(screen, RED, highlight_rect, 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
