from Code.notifications import Notification
from Code.smart_device import Device

import pygame
import random

tv_1 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV1.png')
tv_2 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV2.png')
tv_3 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV3.png')
tv_4 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV4.png')
arr = [tv_1, tv_2, tv_3, tv_4]


class TV(Device):
    def __init__(self, image):
        super().__init__(image)
        self.on = False  # TV starts off as default
        self.channel = 0

    # To be finished
    def action(self, smart_home):
        self.on = not self.on

        if self.on:
            image = arr[self.channel]
            self.image = image
            smart_home.devices.append(self.image)
        else:
            smart_home.devices.remove(self.image)

    def add_notification(self, name, place):
        if self.on:
            text = "✅ The TV turned on in the " + place
            return Notification(text, 3000)
        if not self.on:
            text = "⛔ The TV turned off in the " + place
            return Notification(text, 3000)

    def change_channel(self, name, smart_home):
        if self.on:
            if name == "Channel Up":
                if self.channel == len(arr) - 1:
                    self.channel = 0
                else:
                    self.channel = self.channel + 1
                smart_home.devices.remove(self.image)
                image = arr[self.channel]
                self.image = image
                smart_home.devices.append(self.image)
            elif name == "Channel Down":
                if self.channel == 0:
                    self.channel = len(arr) - 1
                else:
                    self.channel = self.channel - 1
                smart_home.devices.remove(self.image)
                image = arr[self.channel]
                self.image = image
                smart_home.devices.append(self.image)
