from Code.notifications import Notification
from Code.smart_device import Device


class TV(Device):
    def __init__(self, image):
        super().__init__(image)
        self.on = False  # TV starts off as default

    # To be finished
    def action(self, smart_home):
        self.on = not self.on

        if self.on:
            smart_home.devices.append(self.image)
        else:
            smart_home.devices.remove(self.image)

    def add_notification(self, name, place):
        if self.on:
            text = "The " + name + " turned on in the " + place
            return Notification(text, 3000)
        if not self.on:
            text = "The " + name + " turned off in the " + place
            return Notification(text, 3000)
