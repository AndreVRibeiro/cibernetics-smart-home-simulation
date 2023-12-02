from playsound import playsound
from smart_device import Device

# for playing note.wav file

door_bell_sound = "Assets/Sounds/doorbell-shortened-100308.mp3"
door_opened_sound = "Assets/Sounds/dorm-door-opening-6038.mp3"
door_closed_sound = "Assets/Sounds/door-1-close.mp3"

# add image
door_opened_image = "    "


class Door(Device):
    def __init__(self, image):
        self.image = image
        self.image_closed = image
        self.opened = False

    def ring(self, smart_home):
        playsound(door_bell_sound)

    def open(self, smart_home):
        self.opened = True
        self.image = door_opened_image
        playsound(door_opened_sound)

    def close(self, smart_home):
        self.opened = False
        self.image = self.image_closed
        playsound(door_closed_sound)
