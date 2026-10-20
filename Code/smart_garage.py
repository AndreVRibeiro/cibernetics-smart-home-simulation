import pygame

from notifications import Notification
from smart_device import Device

path = "Assets/Sounds/garage_door_closing.mp3"
path2 = "Assets/Sounds/garage_door_opening.mp3"


class Garage(Device):
    def __init__(self, image):
        super().__init__(image)
        self.closed = True  # The Garage Door starts out closed

    # This function opens and closes the Garage Door
    def action(self, smart_home):
        self.closed = not self.closed

        if self.closed:
            smart_home.devices.append(self.image)
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        else:
            smart_home.devices.remove(self.image)
            pygame.mixer.music.load(path2)
            pygame.mixer.music.play()

    def add_notification(self, name, place):
        if not self.closed:
            text = "[OPEN] The Garage Door opened"
            return Notification(text, 3000)
        if self.closed:
            text = "[LOCK] The Garage Door closed"
            return Notification(text, 3000)

    def get_state(self):
        if not self.closed:
            state = "Active"
        else:
            state = "Inactive"
        return state
