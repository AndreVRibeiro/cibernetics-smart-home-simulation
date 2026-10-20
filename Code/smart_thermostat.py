import pygame

from notifications import Notification
from smart_device import Device

error = "Assets/Sounds/stop.mp3"


class Thermostat(Device):

    def __init__(self, image):
        super().__init__(image)
        self.bedroom_temp = 18
        self.bathroom_temp = 23
        self.livingroom_temp = 21
        self.kitchen_temp = 22
        self.bedroom_temp_text = "18°C"
        self.bathroom_temp_text = "23°C"
        self.livingroom_temp_text = "21°C"
        self.kitchen_temp_text = "22°C"

    def action(self, smart_home):
        pass

    def add_notification(self, name, place):
        pass

    def change_temp(self, name):
        if name == "Minus Bathroom":
            if not self.bathroom_temp - 1 < 20:
                self.bathroom_temp = self.bathroom_temp - 1
                self.bathroom_temp_text = "" + str(self.bathroom_temp) + "°C"
                text = "[-] The Temperature of the Bathroom was set to " + self.bathroom_temp_text
                return Notification(text, 3000)
        elif name == "Minus Livingroom":
            if not self.livingroom_temp - 1 < 18:
                self.livingroom_temp = self.livingroom_temp - 1
                self.livingroom_temp_text = "" + str(self.livingroom_temp) + "°C"
                text = "[-] The Temperature of the Living Room was set to " + self.livingroom_temp_text
                return Notification(text, 3000)
        elif name == "Plus Livingroom":
            if not self.livingroom_temp + 1 > 26:
                self.livingroom_temp = self.livingroom_temp + 1
                self.livingroom_temp_text = "" + str(self.livingroom_temp) + "°C"
                text = "[+] The Temperature of the Living Room was set to " + self.livingroom_temp_text
                return Notification(text, 3000)
        elif name == "Plus Bathroom":
            if not self.bathroom_temp + 1 > 28:
                self.bathroom_temp = self.bathroom_temp + 1
                self.bathroom_temp_text = "" + str(self.bathroom_temp) + "°C"
                text = "[+] The Temperature of the Bathroom was set to " + self.bathroom_temp_text
                return Notification(text, 3000)
        elif name == "Minus Bedroom":
            if not self.bedroom_temp + 1 < 16:
                self.bedroom_temp = self.bedroom_temp - 1
                self.bedroom_temp_text = "" + str(self.bedroom_temp) + "°C"
                text = "[-] The Temperature of the Bedroom was set to " + self.bedroom_temp_text
                return Notification(text, 3000)
        elif name == "Minus Kitchen":
            if not self.kitchen_temp + 1 < 18:
                self.kitchen_temp = self.kitchen_temp - 1
                self.kitchen_temp_text = "" + str(self.kitchen_temp) + "°C"
                text = "[-] The Temperature of the Kitchen was set to " + self.kitchen_temp_text
                return Notification(text, 3000)
        elif name == "Plus Bedroom":
            if not self.bedroom_temp + 1 > 24:
                self.bedroom_temp = self.bedroom_temp + 1
                self.bedroom_temp_text = "" + str(self.bedroom_temp) + "°C"
                text = "[+] The Temperature of the Bedroom was set to " + self.bedroom_temp_text
                return Notification(text, 3000)
        else:
            if not self.kitchen_temp + 1 > 26:
                self.kitchen_temp = self.kitchen_temp + 1
                self.kitchen_temp_text = "" + str(self.kitchen_temp) + "°C"
                text = "[+] The Temperature of the Kitchen was set to " + self.kitchen_temp_text
                return Notification(text, 3000)
        text = "❌ Limit reached!"
        pygame.mixer.music.load(error)
        pygame.mixer.music.play()
        return Notification(text, 3000)

