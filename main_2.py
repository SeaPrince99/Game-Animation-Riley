import pygame
import sys
from scene_manager import SceneManager

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Story Game")

# Initialize SceneManager, passing the screen dimensions
scene_manager = SceneManager(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Update the background based on mouse position
            x, y = event.pos
            scene_manager.update_background(x, y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change scene on mouse click
            x, y = event.pos
            if x < SCREEN_WIDTH // 2:  # Left side click
                scene_manager.handle_choice("left")
            else:  # Right side click
                scene_manager.handle_choice("right")

    # Update and render the current scene
    scene_manager.render()

    pygame.display.flip()

pygame.quit()
sys.exit()
