from Code.notifications import Notification
from Code.smart_device import Device


class Garage(Device):
    def __init__(self, image):
        super().__init__(image)
        self.closed = True  # The Garage Door starts out closed

    # This function opens and closes the Garage Door
    def action(self, smart_home):
        self.closed = not self.closed

        if self.closed:
            smart_home.devices.append(self.image)
        else:
            smart_home.devices.remove(self.image)

    def add_notification(self, name, place):
        if self.closed:
            text = "The Garage Door opened"
            return Notification(text, 3000)
        if not self.closed:
            text = "The Garage Door closed"
            return Notification(text, 3000)
