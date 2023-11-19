class Device:
    def __init__(self, image):
        self.image = image

    def action(self, smart_home):
        raise NotImplementedError("Subclasses must implement the action function")
