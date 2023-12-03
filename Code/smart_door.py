import pygame
from playsound import playsound

from notifications import Notification
from smart_device import Device

path = "Assets/Sounds/dorm-door-opening-6038.mp3"
path2 = "Assets/Sounds/door-1-close.mp3"
# for playing note.wav file

class Door(Device):
    def __init__(self, image):
        self.image = image
        self.opened = False


    def action(self, smart_home):
        self.opened = not self.opened

        if self.opened:
            smart_home.devices.append(self.image)
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()

        else:
            smart_home.devices.remove(self.image)
            pygame.mixer.music.load(path2)
            pygame.mixer.music.play()

    def add_notification(self, name, place):
        if self.opened:
            text = "🔓 The Entrance Door opened"
            return Notification(text, 3000)
        if not self.opened:
            text = "🔒 The Entrance Door closed"
            return Notification(text, 3000)
