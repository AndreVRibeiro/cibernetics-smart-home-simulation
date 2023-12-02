from Code.notifications import Notification
from Code.smart_device import Device

import pygame
import random

tv_1 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV1.png')
tv_2 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV2.png')
tv_3 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV3.png')
arr = [tv_1, tv_2, tv_3]


class TV(Device):
    def __init__(self, image):
        super().__init__(image)
        self.on = False  # TV starts off as default

    # To be finished
    def action(self, smart_home):
        self.on = not self.on

        if self.on:
            random_index = random.randint(0, len(arr) - 1)
            image = arr[random_index]
            self.image = image
            smart_home.devices.append(self.image)
        else:
            smart_home.devices.remove(self.image)

    def add_notification(self, name, place):
        if self.on:
            text = "✅ The " + name + " turned on in the " + place
            return Notification(text, 3000)
        if not self.on:
            text = "⛔ The " + name + " turned off in the " + place
            return Notification(text, 3000)
