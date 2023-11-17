import pygame


class Button:
    def __init__(self, text, action, image, position):
        self.text = text
        self.action = action
        self.image = pygame.transform.scale(pygame.image.load(image), (135, 93))
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def perform_action(self):
        print(f"Button clicked: {self.text}")
        # Add your button action logic here