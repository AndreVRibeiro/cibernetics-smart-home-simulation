import pygame

from notifications import Notification
from smart_device import Device

error = "Assets/Sounds/stop.mp3"


class Fridge(Device):

    def __init__(self, image):
        super().__init__(image)
        self.fridge_temp = 2
        self.freezer_temp = -16
        self.fridge_temp_text = "2°C"
        self.freezer_temp_text = "-16°C"

    def action(self, smart_home):
        pass

    def change_temp(self, name):
        if name == "Minus Fridge":
            if not self.fridge_temp - 1 < 1:
                self.fridge_temp = self.fridge_temp - 1
                self.fridge_temp_text = "" + str(self.fridge_temp) + "°C"
                text = "[-] The Temperature of the Fridge was set to " + self.fridge_temp_text
                return Notification(text, 3000)
        elif name == "Minus Freezer":
            if not self.freezer_temp - 1 < -24:
                self.freezer_temp = self.freezer_temp - 1
                self.freezer_temp_text = "" + str(self.freezer_temp) + "°C"
                text = "[-] The Temperature of the Freezer was set to " + self.freezer_temp_text
                return Notification(text, 3000)
        elif name == "Plus Fridge":
            if not self.fridge_temp + 1 > 7:
                self.fridge_temp = self.fridge_temp + 1
                self.fridge_temp_text = "" + str(self.fridge_temp) + "°C"
                text = "[+] The Temperature of the Fridge was set to " + self.fridge_temp_text
                return Notification(text, 3000)
        else:
            if not self.freezer_temp + 1 > -14:
                self.freezer_temp = self.freezer_temp + 1
                self.freezer_temp_text = "" + str(self.freezer_temp) + "°C"
                text = "[+] The Temperature of the Freezer was set to " + self.freezer_temp_text
                return Notification(text, 3000)
        text = "[ERROR] Limit reached!"
        pygame.mixer.music.load(error)
        pygame.mixer.music.play()
        return Notification(text, 3000)

    def add_notification(self, name, place):
        pass


