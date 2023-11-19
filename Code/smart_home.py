import pygame.image

from Code.smart_blinds import Blinds
from Code.smart_ligths import Light


class SmartHome:

    def __init__(self):
        self.devices = [pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/HomeTest1.png")]

        self.blinds_bedroom = Blinds(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bedroom_Blinds.png"))
        self.blinds_bathroom = Blinds(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bathroom_Blinds.png"))
        self.devices.append(self.blinds_bedroom.image)
        self.devices.append(self.blinds_bathroom.image)

        self.ceiling_ligths_bedroom = Light(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bedroom_Ceiling_Lights.png"))


    def draw(self, screen):
        for image in self.devices:
            screen.blit(image, (0, 0))
