import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Crosshair with Space in the Middle")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Draw vertical lines with space in the middle
    pygame.draw.line(screen, white, (width // 2 - 20, height // 2), (width // 2 - 5, height // 2), 2)
    pygame.draw.line(screen, white, (width // 2 + 5, height // 2), (width // 2 + 20, height // 2), 2)

    # Draw horizontal lines with space in the middle
    pygame.draw.line(screen, white, (width // 2, height // 2 - 20), (width // 2, height // 2 - 5), 2)
    pygame.draw.line(screen, white, (width // 2, height // 2 + 5), (width // 2, height // 2 + 20), 2)

    # Update the display
    pygame.display.flip()
