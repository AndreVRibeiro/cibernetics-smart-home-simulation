from Code.smart_device import Device


class Light(Device):
    def __init__(self, image):
        super().__init__(image)
        self.on = False  # Lights start off by default

    # This function turns the lights on and off
    def action(self, smart_home):
        self.on = not self.on

        if self.on:
            smart_home.devices.append(self.image)
        else:
            smart_home.devices.remove(self.image)

