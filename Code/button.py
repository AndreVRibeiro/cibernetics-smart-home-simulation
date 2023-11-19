import pygame


class Button:
    def __init__(self, text, device, image, image_pressed, position, smart_home):
        self.text = text
        self.device = device
        self.image = pygame.transform.scale(pygame.image.load(image), (135.474, 70.853))
        self.image_pressed = pygame.transform.scale(pygame.image.load(image_pressed), (135.474, 70.853))
        self.position = position
        self.smart_home = smart_home
        self.rect = self.image.get_rect(topleft=position)
        self.pressed = False

    def perform_action(self):
        print(f"Button clicked: {self.text}")
        # Add your button action logic here
        self.device.action(self.smart_home)
        self.pressed = not self.pressed
        self.pressed_image()

    def pressed_image(self):
        save = self.image
        self.image = self.image_pressed
        self.image_pressed = save
