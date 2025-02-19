from scene import Scene1

class SceneManager:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.current_scene = Scene1(screen, width, height)  # Start with Scene1

    def change_scene(self, scene):
        self.current_scene = scene

    def handle_event(self, event):
        next_scene = self.current_scene.handle_event(event)
        if next_scene:
            self.change_scene(next_scene)

    def render(self):
        self.current_scene.render()