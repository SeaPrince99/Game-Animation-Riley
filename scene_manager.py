import pygame
import os
import cv2
import numpy as np

class SceneManager:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scenes = self.load_scenes()
        self.current_scene = "scene_1"
        self.current_background = self.scenes[self.current_scene]["background"]
        self.video_playing = True
        self.last_frame_image = None
        pygame.mixer.init()  # Initialize the mixer for sound

    def load_scenes(self):
        """Define and load all scenes."""
        return {
            "scene_1": {
                "video": "scene_1_video.mp4",  # Video for the first scene
                "audio": "scene_1_audio.mp3",  # Audio for the first scene
                "left_animation": pygame.image.load(os.path.join("assets", "left_effect.jpg")),
                "right_animation": pygame.image.load(os.path.join("assets", "right_effect.jpg")),
                "left": "scene_2",  # Next scene if left is clicked
                "right": "scene_3",  # Next scene if right is clicked
            },
            "scene_2": {
                "video": "scene_2_video.mp4",  # Video for scene 2
                "audio": "scene_2_audio.mp3",  # Audio for scene 2
                "left_animation": pygame.image.load(os.path.join("assets", "left_effect_2.jpg")),
                "right_animation": pygame.image.load(os.path.join("assets", "right_effect_2.jpg")),
                "left": "scene_4",  # Next scene if left is clicked
                "right": "scene_5",  # Next scene if right is clicked
            },
            "scene_3": {
                "video": "scene_3_video.mp4",  # Video for scene 3
                "audio": "scene_3_audio.mp3",  # Audio for scene 3
                "left_animation": pygame.image.load(os.path.join("assets", "left_effect_3.jpg")),
                "right_animation": pygame.image.load(os.path.join("assets", "right_effect_3.jpg")),
                "left": "scene_6",  # Next scene if left is clicked
                "right": "scene_7",  # Next scene if right is clicked
            },
            # Add more scenes as needed
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
            self.video_playing = True  # Reset video playing for the new scene

    def render(self):
        """Render the current scene."""
        self.screen.fill((0, 0, 0))  # Clear screen with black

        if self.video_playing:
            self.play_video(self.scenes[self.current_scene]["video"], self.scenes[self.current_scene]["audio"])

        # Display the background and hover effect
        self.screen.blit(self.current_background, (0, 0))

    def play_video(self, video_file, audio_file):
        """Play a video with its audio and capture the last frame."""
        cap = cv2.VideoCapture(os.path.join("assets", video_file))
        
        if not cap.isOpened():
            print("Error: Couldn't open video file.")
            return

        # Load and play the audio
        pygame.mixer.music.load(os.path.join("assets", audio_file))
        pygame.mixer.music.play()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert frame to RGB (pygame uses RGB, OpenCV uses BGR)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame_rgb)

            # Display the frame in pygame window
            self.screen.blit(frame_surface, (0, 0))
            pygame.display.flip()

            # Wait for a small amount of time to match video frame rate
            pygame.time.wait(10)

        # Capture the last frame of the video
        self.last_frame_image = pygame.surfarray.make_surface(frame_rgb)

        # Once the video finishes, stop playing the audio
        pygame.mixer.music.stop()

        # Once the video finishes, stop playing
        self.video_playing = False

        # Release the video capture object
        cap.release()

    def get_last_frame(self):
        """Return the last frame captured from the video."""
        return self.last_frame_image
