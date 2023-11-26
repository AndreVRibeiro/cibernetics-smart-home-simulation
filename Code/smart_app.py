import pygame

from Code.button import Button


class SmartApp:

    def __init__(self, smart_home):
        self.image = pygame.transform.scale(pygame.image.load(
            "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Phone.png"), (532, 1001))
        self.image_Extra = pygame.transform.scale(pygame.image.load(
            "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Extra.png"), (479, 792))
        self.visible_Start = False
        self.visible_Camera = False
        self.smart_home = smart_home
        self.buttons_Start = [
            Button("Bedroom Blinds", self.smart_home.blinds_bedroom,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds_pressed.png",
                   (1406.138, 641.480), smart_home),
            Button("Bathroom Blinds", self.smart_home.blinds_bathroom,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_blinds_pressed.png",
                   (1406.138, 769.791), smart_home),
            Button("Bedroom Ceiling Lights", self.smart_home.ceiling_lights_bedroom,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights_pressed.png",
                   (1549.288, 641.480), smart_home),
            Button("Livingroom Ceiling Lights", self.smart_home.ceiling_lights_livingroom,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights_pressed.png",
                   (1549.301, 384.858), smart_home),
            Button("Kitchen Ceiling Lights", self.smart_home.ceiling_lights_kitchen,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_ceiling_lights_pressed.png",
                   (1406.148, 513.239), smart_home),
            Button("Bathroom Lights", self.smart_home.lights_bathroom,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_sconces.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_sconces_pressed.png",
                   (1549.301, 769.791), smart_home),
            Button("Garage Door", self.smart_home.garage_door,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_garage.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_garage_pressed.png",
                   (1406.138, 898.102), smart_home),
            Button("Bedroom Nightstand Lamp", self.smart_home.nightstand_lamp_bedroom,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_nightstand.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_nightstand_pressed.png",
                   (1692.465, 641.480), smart_home),
            Button("Livingroom Floor Lamp", self.smart_home.floor_lamp_livingroom,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_floorlamp.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_floorlamp_pressed.png",
                   (1692.465, 384.858), smart_home),
            Button("Garage Camera", self.smart_home.garage_camera,
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_camera.png",
                   "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_camera.png",
                   (1549.301, 898.102), smart_home)
            # Button("TV", self.smart_home.television, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_tv.png", "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_tv_pressed.png", (1406.138, 385.289), smart_home)
            # Add more buttons as needed
        ]
        self.buttons_Camera = [
            Button("Exit", None, "C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Buttons/button_exit.png", None,
                   (1779.693, 246.525), smart_home)
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.visibility_start()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            # Home Menu is visible - Camera Menu is not
            if self.visible_Start and not self.visible_Camera:
                for button in self.buttons_Start:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "Garage Camera":
                            self.visibility_camera()
                        else:
                            button.perform_action()
            elif self.visible_Start and self.visible_Camera:
                for button in self.buttons_Camera:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "Exit":
                            self.visibility_camera()

    def draw(self, screen):
        if self.visible_Start:
            screen.blit(self.image, (1351, 42))  # Draw the image
            if self.visible_Camera:
                screen.blit(self.image_Extra, (1377.386, 220.390))
                for button in self.buttons_Camera:
                    screen.blit(button.image, button.position)
            else:
                for button in self.buttons_Start:
                    screen.blit(button.image, button.position)

    def visibility_start(self):
        self.visible_Start = not self.visible_Start

    def visibility_camera(self):
        self.visible_Camera = not self.visible_Camera
