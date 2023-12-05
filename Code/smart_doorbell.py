from Code.smart_device import Device


class Doorbell(Device):
    def __init__(self, image):
        super().__init__(image)

    def action(self, smart_home):
        pass

    def add_notification(self, name, place):
        pass
