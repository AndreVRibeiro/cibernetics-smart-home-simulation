from Code.notifications import Notification
from Code.smart_device import Device


class Blinds(Device):
    def __init__(self, image):
        super().__init__(image)
        self.closed = True  # Blinds start closed by default

    # This function opens the blinds and prints the image of an open blind
    def action(self, smart_home):
        self.closed = not self.closed

        if self.closed:
            smart_home.devices.append(self.image)
        else:
            smart_home.devices.remove(self.image)

    def add_notification(self, name, place):
        if not self.closed:
            text = "✅ The " + name + " opened in the " + place
            return Notification(text, 3000)
        if self.closed:
            text = "⛔ The " + name + " closed in the " + place
            return Notification(text, 3000)

