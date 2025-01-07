import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Story Game")

# Colors
WHITE = (255, 255, 255)

# Load animations or images (replace these with your actual assets)
scene_animation = pygame.image.load("test.jpg")  # Single animation/image for the scene
left_effect = pygame.image.load("left.jpg")          # Effect for left choice
right_effect = pygame.image.load("right.jpeg")        # Effect for right choice

# Game scenes
scenes = {
    "start": {"image": scene_animation, "left": "left_path", "right": "right_path"},
}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if mouse is on the left or right side of the screen
    if mouse_x < SCREEN_WIDTH // 2:
        screen.blit(left_effect, (0, 0))
    else:
        screen.blit(right_effect, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()