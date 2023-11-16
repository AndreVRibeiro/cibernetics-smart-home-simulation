class Blinds:
    def __init__(self):
        self.closed = False  # Blinds start closed by default

    # This function opens the blinds and prints the image of an open blind
    def open(self):
        self.closed = False

    # This function closes the blinds and prints the image of a closed blind
    def close(self):
        self.closed = True

