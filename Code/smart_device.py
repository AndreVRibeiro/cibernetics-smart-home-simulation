class Device:
    def __init__(self, image):
        self.image = image

    def action(self, smart_home):
        raise NotImplementedError("Subclasses must implement the action function")

    def add_notification(self, name, place):
        raise NotImplementedError("Subclasses must implement the action function")