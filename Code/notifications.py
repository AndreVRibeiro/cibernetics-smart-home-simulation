import pygame


class Notification:

    def __init__(self, text, duration):
        self.text = text
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

    def is_expired(self):
        return pygame.time.get_ticks() - self.start_time > self.duration
