import pygame

from notifications import Notification
from smart_device import Device

off = "Assets/Sounds/light_off.mp3"
on = "Assets/Sounds/light_on.mp3"


class Light(Device):
    def __init__(self, image):
        super().__init__(image)
        self.on = False  # Lights start off by default

    # This function turns the lights on and off
    def action(self, smart_home):
        self.on = not self.on

        if self.on:
            smart_home.devices.append(self.image)
            pygame.mixer.music.load(on)
            pygame.mixer.music.play()
        else:
            smart_home.devices.remove(self.image)
            pygame.mixer.music.load(off)
            pygame.mixer.music.play()

    def add_notification(self, name, place):
        if self.on:
            text = "✅ The " + name + " turned on in the " + place
            return Notification(text, 3000)
        if not self.on:
            text = "⛔ The " + name + " turned off in the " + place
            return Notification(text, 3000)
