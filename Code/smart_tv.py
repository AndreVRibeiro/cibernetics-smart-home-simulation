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
