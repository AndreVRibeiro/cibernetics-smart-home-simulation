import pygame

from Code.button import Button


class SmartApp:

    def __init__(self, image_filename):
        self.image = pygame.transform.scale(pygame.image.load(image_filename), (532, 1001))
        self.visible = False
        self.buttons = [
            Button("Button 1", 1, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/button.png", (1410, 200))
            # Add more buttons as needed

        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.visibility()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if self.visible:
                for button in self.buttons:
                    if button.rect.collidepoint(event.pos):
                        button.perform_action()

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (1351, 42))  # Draw the image
            for button in self.buttons:
                screen.blit(button.image, button.position)

    def visibility(self):
        self.visible = not self.visible
