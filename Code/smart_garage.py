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

