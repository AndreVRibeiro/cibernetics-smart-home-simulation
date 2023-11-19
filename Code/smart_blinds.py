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

