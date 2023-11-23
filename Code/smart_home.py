import pygame.image

from Code.smart_blinds import Blinds
from Code.smart_garage import Garage
from Code.smart_ligths import Light


class SmartHome:

    def __init__(self):
        self.devices = [pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/HomeTest1.png")]

        # Add the Blinds to the Smart House
        self.blinds_bedroom = Blinds(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bedroom_Blinds.png"))
        self.blinds_bathroom = Blinds(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bathroom_Blinds.png"))
        self.devices.append(self.blinds_bedroom.image)
        self.devices.append(self.blinds_bathroom.image)

        # Add the Ceiling Lights to the Smart House
        self.ceiling_lights_bedroom = Light(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bedroom_Ceiling_Lights.png"))
        self.nightstand_lamp_bedroom = Light(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bedroom_Light.png"))
        self.ceiling_lights_livingroom = Light(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Livingroom_Ceiling_Lights.png"))
        self.floor_lamp_livingroom = Light(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Livingroom_Lamp.png"))
        self.ceiling_lights_kitchen = Light(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Kitchen_Ceiling_Lights.png"))
        self.lights_bathroom = Light(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Bathroom_Lights.png"))



        # Add the Garage Door
        self.garage_door = Garage(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/Garage_Door.png"))
        self.devices.append(self.garage_door.image)

        # Add the TV
        #self.television = TV(pygame.image.load())


    def draw(self, screen):
        for image in self.devices:
            screen.blit(image, (0, 0))
