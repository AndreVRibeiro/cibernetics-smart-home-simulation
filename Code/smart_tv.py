from notifications import Notification
from smart_device import Device

import pygame

# TV images
tv_1 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV1.png')
tv_2 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV2.png')
tv_3 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV3.png')
tv_4 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV4.png')
tv_5 = pygame.image.load('Assets/Smart_Devices/Livingroom_TV5.png')
arr = [tv_1, tv_2, tv_3, tv_4, tv_5]

# TV sounds
tv_1_sound = 'Assets/Sounds/livingroom_TV1_Sound.mp3'
tv_2_sound = 'Assets/Sounds/livingroom_TV2_Sound.mp3'
tv_3_sound = 'Assets/Sounds/livingroom_TV3_Sound.mp3'
tv_4_sound = 'Assets/Sounds/livingroom_TV4_Sound.mp3'
tv_5_sound = 'Assets/Sounds/livingroom_TV5_Sound.mp3'
arrSound = [tv_1_sound, tv_2_sound, tv_3_sound, tv_4_sound, tv_5_sound]


class TV(Device):
    def __init__(self, image):
        super().__init__(image)
        self.on = False  # TV starts off as default
        self.channel = 0
        self.sound = pygame.mixer.Sound(arrSound[self.channel])
        self.sound.set_volume(0.2)
        self.volume = self.sound.get_volume()

    # To be finished
    def action(self, smart_home):
        self.on = not self.on

        if self.on:
            image = arr[self.channel]
            self.image = image
            smart_home.devices.append(self.image)
            self.sound.play()
        else:
            smart_home.devices.remove(self.image)
            self.sound.stop()

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

                self.sound.stop()
                smart_home.devices.remove(self.image)
                image = arr[self.channel]
                self.image = image
                smart_home.devices.append(self.image)
                self.sound = pygame.mixer.Sound(arrSound[self.channel])
                self.sound.play()

            elif name == "Channel Down":
                if self.channel == 0:
                    self.channel = len(arr) - 1
                else:
                    self.channel = self.channel - 1
                self.sound.stop()
                smart_home.devices.remove(self.image)
                image = arr[self.channel]
                self.image = image
                smart_home.devices.append(self.image)
                self.sound = pygame.mixer.Sound(arrSound[self.channel])
                self.sound.play()

        text = "📺 The TV channel has been updated"
        return Notification(text, 3000)

    def change_volume(self, name, smart_home):
        if self.on:
            if name == "Volume Up":
                self.sound.set_volume(self.volume + 0.1)
                text = "➕ The Volume has been increased"
                return Notification(text, 3000)

            elif name == "Volume Down":
                self.sound.set_volume(self.volume - 0.1)
                text = "➖ The Volume has been decreased"
                return Notification(text, 3000)
