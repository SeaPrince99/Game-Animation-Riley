import pygame

class Scene:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.selection_areas = []  # List to hold multiple selection areas

    def handle_event(self, event):
        pass

    def render(self):
        pass

    def add_selection_area(self, x, y, width, height, next_scene_class):
        self.selection_areas.append((pygame.Rect(x, y, width, height), next_scene_class))

def create_scene_class(scene_number, next_scene_class):
    class CustomScene(Scene):
        def __init__(self, screen, width, height):
            super().__init__(screen, width, height)
            self.image = pygame.image.load(f'assets/scene{scene_number}.png')
            self.image = pygame.transform.scale(self.image, (1280, 720))
            self.add_selection_area(0, 0, 1280, 720, next_scene_class)  # Example area

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                for area, next_scene in self.selection_areas:
                    if area.collidepoint(event.pos):
                        return next_scene(self.screen, self.width, self.height)
            return None

        def render(self):
            self.screen.blit(self.image, (0, 0))
            for area, _ in self.selection_areas:
                pygame.draw.rect(self.screen, (255, 0, 0), area, 2)

    return CustomScene

# Create scene classes dynamically
Scene1 = create_scene_class(1, lambda screen, width, height: Scene2(screen, width, height))

class Scene2(Scene):
    def __init__(self, screen, width, height):
        super().__init__(screen, width, height)
        self.image = pygame.image.load('assets/scene2.png')
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.selection_area = pygame.Rect(230, 350, 200, 240)  # Example area

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.selection_area.collidepoint(event.pos):
                return Scene3(self.screen, self.width, self.height)
        return None

    def render(self):
        self.screen.blit(self.image, (0, 0))
        pygame.draw.rect(self.screen, (255, 0, 0), self.selection_area, 2)
#Scene2 = create_scene_class(2, lambda screen, width, height: Scene3(screen, width, height))

Scene3 = create_scene_class(3, lambda screen, width, height: Scene4(screen, width, height))
Scene4 = create_scene_class(4, lambda screen, width, height: Scene5(screen, width, height))
Scene5 = create_scene_class(5, lambda screen, width, height: Scene6(screen, width, height))
Scene6 = create_scene_class(6, lambda screen, width, height: Scene7(screen, width, height))
Scene7 = create_scene_class(7, lambda screen, width, height: Scene8(screen, width, height))
Scene8 = create_scene_class(8, lambda screen, width, height: Scene9(screen, width, height))
Scene9 = create_scene_class(9, lambda screen, width, height: Scene10(screen, width, height))
Scene10 = create_scene_class(10, lambda screen, width, height: Scene11(screen, width, height))
Scene11 = create_scene_class(11, lambda screen, width, height: Scene12(screen, width, height))
Scene12 = create_scene_class(12, lambda screen, width, height: Scene13(screen, width, height))
Scene13 = create_scene_class(13, lambda screen, width, height: Scene14(screen, width, height))

# Custom Scene14 with multiple selection areas
class Scene14(Scene):
    def __init__(self, screen, width, height):
        super().__init__(screen, width, height)
        self.image = pygame.image.load('assets/scene14.png')
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.add_selection_area(60, 450, 350, 150, Scene97)  # Area leading to Scene1
        self.add_selection_area(450, 450, 350, 150, Scene98)  # Area leading to Scene2
        self.add_selection_area(900, 450, 350, 150, Scene99)  # Area leading to Scene3

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for area, next_scene in self.selection_areas:
                if area.collidepoint(event.pos):
                    return next_scene(self.screen, self.width, self.height)
        return None

    def render(self):
        self.screen.blit(self.image, (0, 0))
        for area, _ in self.selection_areas:
            pygame.draw.rect(self.screen, (255, 0, 0), area, 2)
            
class Scene97(Scene):
    def __init__(self, screen, width, height):
        super().__init__(screen, width, height)
        self.image = pygame.image.load('assets/kill.png')
        self.image = pygame.transform.scale(self.image, (1280, 720))

    def handle_event(self, event):
        # No further transitions
        return None

    def render(self):
        self.screen.blit(self.image, (0, 0))
        
class Scene98(Scene):
    def __init__(self, screen, width, height):
        super().__init__(screen, width, height)
        self.image = pygame.image.load('assets/spare.png')
        self.image = pygame.transform.scale(self.image, (1280, 720))

    def handle_event(self, event):
        # No further transitions
        return None

    def render(self):
        self.screen.blit(self.image, (0, 0))
        
class Scene99(Scene):
    def __init__(self, screen, width, height):
        super().__init__(screen, width, height)
        self.image = pygame.image.load('assets/forget.png')
        self.image = pygame.transform.scale(self.image, (1280, 720))

    def handle_event(self, event):
        # No further transitions
        return None

    def render(self):
        self.screen.blit(self.image, (0, 0))
