import pygame

from Code.notifications import Notification


class Button:
    def __init__(self, name, place, device, image, image_pressed, position, smart_home):
        self.name = name
        self.place = place
        self.device = device
        if self.name == "Exit":
            self.image = pygame.transform.scale(pygame.image.load(image), (41, 41))
        elif self.name == "TV2":
            self.image = pygame.transform.scale(pygame.image.load(image), (136, 136))
            self.image_pressed = pygame.transform.scale(pygame.image.load(image_pressed), (136, 136))
        elif self.name == "Volume Up" or self.name == "Channel Up":
            self.image = pygame.transform.scale(pygame.image.load(image), (121, 84))
        elif self.name == "Volume Down" or self.name == "Channel Down":
            self.image = pygame.transform.scale(pygame.image.load(image), (121, 86))

        else:
            self.image = pygame.transform.scale(pygame.image.load(image), (135.474, 70.853))
            self.image_pressed = pygame.transform.scale(pygame.image.load(image_pressed), (135.474, 70.853))
        self.position = position
        self.smart_home = smart_home
        self.rect = self.image.get_rect(topleft=position)
        self.pressed = False

    def perform_action(self):
        print(f"Button clicked: {self.name}")

        if self.name == "Channel Up" or self.name == "Channel Down" or self.name == "Volume Up" or self.name == "Volume Down":
            self.device.change_channel(self.name, self.smart_home)
        elif self.device is not None:
            self.device.action(self.smart_home)
            self.smart_home.notifications.append(self.device.add_notification(self.name, self.place))
            self.pressed_image()

    def pressed_image(self):
        self.pressed = not self.pressed
        save = self.image
        self.image = self.image_pressed
        self.image_pressed = save
