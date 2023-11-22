import pygame

from Code.button import Button
from Code.smart_ligths import Light


class SmartApp:

    def __init__(self, smart_home):
        self.image = pygame.transform.scale(pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Phone.png"), (532, 1001))
        self.visible = False
        self.smart_home = smart_home
        self.buttons = [
            Button("Bedroom Blinds", self.smart_home.blinds_bedroom, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds_pressed.png", (1406.138, 641.480), smart_home),
            Button("Bathroom Blinds", self.smart_home.blinds_bathroom, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds_pressed.png", (1406.138, 769.791), smart_home),
            Button("Bedroom Ceiling Lights", self.smart_home.ceiling_lights_bedroom, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights_pressed.png", (1549.288, 641.480), smart_home),
            Button("Livingroom Ceiling Lights", self.smart_home.ceiling_lights_livingroom, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights_pressed.png", (1549.301, 384.858), smart_home),
            Button("Kitchen Ceiling Lights", self.smart_home.ceiling_lights_kitchen, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights_pressed.png", (1406.148, 513.239), smart_home),
            Button("Bathroom Lights", self.smart_home.lights_bathroom, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_sconces.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_sconces_pressed.png", (1549.301, 769.791), smart_home),
            Button("Garage Door", self.smart_home.garage_door, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_garage.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_garage_pressed.png", (1406.138, 898.102), smart_home),
            #Button("TV", self.smart_home.television, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_tv.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_tv_pressed.png", (1406.138, 385.289), smart_home)
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
