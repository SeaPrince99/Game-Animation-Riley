import pygame
import os

class SceneManager:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scenes = self.load_scenes()
        self.current_scene = "start"
        self.current_background = self.scenes[self.current_scene]["background"]

    def load_scenes(self):
        """Define and load all scenes."""
        return {
            "start": {
                "background": pygame.image.load(os.path.join("assets", "animation.jpg")),
                "left_animation": pygame.image.load(os.path.join("assets", "left_effect.jpg")),
                "right_animation": pygame.image.load(os.path.join("assets", "right_effect.jpg")),
                "left": "left_path",
                "right": "right_path",
            },
            "left_path": {
                "background": pygame.image.load(os.path.join("assets", "left_effect.jpg")),
                "left": None,
                "right": None,
            },
            "right_path": {
                "background": pygame.image.load(os.path.join("assets", "right_effect.jpg")),
                "left": None,
                "right": None,
            },
        }

    def update_background(self, mouse_x, mouse_y):
        """Update the background based on mouse position."""
        if mouse_x < self.screen_width // 2:
            self.current_background = self.scenes[self.current_scene]["left_animation"]
        else:
            self.current_background = self.scenes[self.current_scene]["right_animation"]

    def handle_choice(self, choice):
        """Handle the player's choice and update the current scene."""
        next_scene = self.scenes[self.current_scene].get(choice)
        if next_scene:
            self.current_scene = next_scene
            self.current_background = self.scenes[self.current_scene]["background"]

    def render(self):
        """Render the current scene."""
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.screen.blit(self.current_background, (0, 0))
