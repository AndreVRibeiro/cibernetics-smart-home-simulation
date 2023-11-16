import pygame


class SmartApp:

    def __init__(self, image_filename):
        i = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(i, (532, 1001))
        self.visible = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            SmartApp.visibility(self)

        '''if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if self.button_visible:
                button_rect = self.button.get_rect(topleft=self.position)
                if button_rect.collidepoint(event.pos):
                    print("Button Clicked!")
                    # Add your button click logic here'''

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (1351, 42))  # Draw the image

    def visibility(self):
        self.visible = not self.visible
