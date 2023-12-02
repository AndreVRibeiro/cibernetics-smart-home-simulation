import pygame


class Tab:
    def __init__(self, image):
        self.is_toggled = False
        self.image = image

    def action(self, smart_home):
        self.is_toggled = not self.is_toggled
