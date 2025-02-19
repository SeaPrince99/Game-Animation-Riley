import pygame
import sys
from scene_manager import SceneManager

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
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
        else:
            # Delegate event handling to the scene manager
            scene_manager.handle_event(event)

    # Update and render the current scene
    scene_manager.render()

    pygame.display.flip()

pygame.quit()
sys.exit()
