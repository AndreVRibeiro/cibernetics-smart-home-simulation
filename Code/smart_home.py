import pygame.image

from smart_door import Door
from automation_tab import Tab
from smart_tv import TV
from smart_blinds import Blinds
from smart_garage import Garage
from smart_ligths import Light
from smart_camera import Camera


class SmartHome:

    def __init__(self):
        self.devices = [pygame.image.load("Assets/HomeTest1.png")]

        # Add the Blinds to the Smart House
        self.blinds_bedroom = Blinds(pygame.image.load("Assets/Smart_Devices/Bedroom_Blinds.png"))
        self.blinds_bathroom = Blinds(pygame.image.load("Assets/Smart_Devices/Bathroom_Blinds.png"))
        self.devices.append(self.blinds_bedroom.image)
        self.devices.append(self.blinds_bathroom.image)

        # Add the Ceiling Lights to the Smart House
        self.ceiling_lights_bedroom = Light(pygame.image.load("Assets/Smart_Devices/Bedroom_Ceiling_Lights.png"))
        self.nightstand_lamp_bedroom = Light(pygame.image.load("Assets/Smart_Devices/Bedroom_Light.png"))
        self.ceiling_lights_livingroom = Light(pygame.image.load("Assets/Smart_Devices/Livingroom_Ceiling_Lights.png"))
        self.floor_lamp_livingroom = Light(pygame.image.load("Assets/Smart_Devices/Livingroom_Lamp.png"))
        self.ceiling_lights_kitchen = Light(pygame.image.load("Assets/Smart_Devices/Kitchen_Ceiling_Lights.png"))
        self.lights_bathroom = Light(pygame.image.load("Assets/Smart_Devices/Bathroom_Lights.png"))

        # Add the Garage Door
        self.garage_door = Garage(pygame.image.load("Assets/Smart_Devices/Garage_Door.png"))
        self.devices.append(self.garage_door.image)

        # Add the entrance Door
        self.entrance_door = Door(pygame.image.load("Assets/Smart_Devices/Entry_Door.png"))

        # Add the TV
        self.television = TV(pygame.image.load("Assets/Smart_Devices/Garage_Door.png"))

        # Add the camera
        self.garage_camera = Camera(None)

        # Add the Tab
        self.Tab = Tab(pygame.image.load("Assets/Buttons/g5.png"))

        # Add array for notifications
        self.notifications = []

    def draw(self, screen):
        for image in self.devices:
            screen.blit(image, (0, 0))

    def update_notification_array(self):
        self.notifications = [notif for notif in self.notifications if not notif.is_expired()]

    def draw_notifications(self, screen):
        # font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 50)
        font = pygame.font.Font(pygame.font.match_font('Segoe UI Emoji'), 50)
        y_position = 50
        background_color = (255, 255, 255)
        for notif in self.notifications:
            text_surface = font.render(notif.text, True, (0, 0, 0))

            text_rect = text_surface.get_rect()
            text_rect.topleft = (200, y_position)

            # Create a background rectangle
            background_rect = pygame.Rect(text_rect.left, text_rect.top, text_rect.width, text_rect.height)
            pygame.draw.rect(screen, background_color, background_rect)

            # Blit the background and text onto the screen
            screen.blit(text_surface, text_rect.topleft)

            #screen.blit(text_surface, (200, y_position))
            y_position += text_surface.get_height() + 5


