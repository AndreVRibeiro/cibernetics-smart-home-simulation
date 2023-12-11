import pygame

from Code.notifications import Notification
from automation_menu import AutomationMenu
from button import Button


class SmartApp:

    def __init__(self, smart_home):
        self.image = pygame.transform.scale(pygame.image.load("Assets/Phone.png"), (532, 1001))
        self.image_Camera_Menu = pygame.transform.scale(pygame.image.load("Assets/Menus/Camera_Menu.png"), (479, 792))
        self.image_TV_Menu = pygame.transform.scale(pygame.image.load("Assets/Menus/TV_Menu.png"), (479, 792))
        self.image_Fridge_Menu = pygame.transform.scale(pygame.image.load("Assets/Menus/Fridge_Menu.png"), (479, 792))
        self.image_Thermostat_Menu = pygame.transform.scale(pygame.image.load("Assets/Menus/Thermostat_Menu.png"), (479, 792))
        self.image_Doorbell_Menu = pygame.transform.scale(pygame.image.load("Assets/Menus/Doorbell_Menu.png"), (479, 792))
        # self.visible_Start = False
        self.visible_Camera = False
        self.visible_TV = False
        self.visible_Fridge = False
        self.visible_Thermostat = False
        self.visible_Doorbell = False

        self.smart_home = smart_home
        self.automation = AutomationMenu(self.smart_home)
        self.buttons_Start = [
            Button("Blinds", "Bedroom", self.smart_home.blinds_bedroom, "Assets/Buttons/button_blinds.png",
                   "Assets/Buttons/button_blinds_pressed.png", (1406.138, 641.480), smart_home),
            Button("Blinds", "Bathroom", self.smart_home.blinds_bathroom, "Assets/Buttons/button_blinds.png",
                   "Assets/Buttons/button_blinds_pressed.png", (1406.138, 769.791), smart_home),
            Button("Ceiling Lights", "Bedroom", self.smart_home.ceiling_lights_bedroom,
                   "Assets/Buttons/button_ceiling_lights.png", "Assets/Buttons/button_ceiling_lights_pressed.png",
                   (1549.288, 641.480), smart_home),
            Button("Ceiling Lights", "Living Room", self.smart_home.ceiling_lights_livingroom,
                   "Assets/Buttons/button_ceiling_lights.png", "Assets/Buttons/button_ceiling_lights_pressed.png",
                   (1549.301, 384.858), smart_home),
            Button("Ceiling Lights", "Kitchen", self.smart_home.ceiling_lights_kitchen,
                   "Assets/Buttons/button_ceiling_lights.png", "Assets/Buttons/button_ceiling_lights_pressed.png",
                   (1406.148, 513.239), smart_home),
            Button("Lights", "Bathroom", self.smart_home.lights_bathroom, "Assets/Buttons/button_sconces.png",
                   "Assets/Buttons/button_sconces_pressed.png", (1549.301, 769.791), smart_home),
            Button("Garage Door1", "Garage", self.smart_home.garage_door, "Assets/Buttons/button_garage.png",
                   "Assets/Buttons/button_garage_pressed.png", (1406.138, 898.102), smart_home),
            Button("Nightstand Lamp", "Bedroom", self.smart_home.nightstand_lamp_bedroom,
                   "Assets/Buttons/button_nightstand.png", "Assets/Buttons/button_nightstand_pressed.png",
                   (1692.465, 641.480), smart_home),
            Button("Floor Lamp", "Living Room", self.smart_home.floor_lamp_livingroom,
                   "Assets/Buttons/button_floorlamp.png", "Assets/Buttons/button_floorlamp_pressed.png",
                   (1692.465, 384.858), smart_home),
            Button("Camera", "Garage", self.smart_home.garage_camera, "Assets/Buttons/button_camera.png",
                   "Assets/Buttons/button_camera.png", (1549.301, 898.102), smart_home),
            Button("TV", "Living Room", self.smart_home.television, "Assets/Buttons/button_tv.png",
                   "Assets/Buttons/button_tv_pressed.png", (1406.138, 385.289), smart_home),
            Button("Automation", "None", None, "Assets/Buttons/button_automation.png",
                   "Assets/Buttons/button_automation.png", (1744.983, 135.679), smart_home),
            Button("Door1", "Entrance", self.smart_home.entrance_door, "Assets/Buttons/button_door.png",
                   "Assets/Buttons/button_door_pressed.png", (1406.138, 256.477), smart_home),
            Button("Fridge", "Kitchen", self.smart_home.kitchen_fridge, "Assets/Buttons/button_fridge.png",
                   "Assets/Buttons/button_fridge.png", (1549.301, 513.169), smart_home),
            Button("Thermostat", "Bathroom", self.smart_home.thermostat_bathroom, "Assets/Buttons/button_thermostat.png",
                   "Assets/Buttons/button_thermostat.png", (1692.465, 769.791), smart_home),
            Button("Doorbell", "Entrance", self.smart_home.entrance_doorbell, "Assets/Buttons/button_doorbell.png",
                   "Assets/Buttons/button_doorbell.png", (1549.302, 256.477), smart_home)
        ]
        self.buttons_Camera = [
            Button("Exit", None, None, "Assets/Buttons/button_exit.png", None, (1779.693, 246.525), smart_home),
            Button("Garage Door2", "Garage", self.smart_home.garage_door, "Assets/Buttons/button_garage2.png",
                   "Assets/Buttons/button_garage_pressed2.png", (1461.809, 772.288), smart_home)
        ]
        self.buttons_TV = [
            Button("Exit", None, None, "Assets/Buttons/button_exit.png", None, (1779.693, 246.525), smart_home),
            Button("TV2", "Living Room", self.smart_home.television, "Assets/Buttons/button_tv2.png",
                   "Assets/Buttons/button_tv2_pressed.png", (1548.959, 452.148), smart_home),
            Button("Volume Up", None, self.smart_home.television, "Assets/Buttons/button_vol_up.png", None,
                   (1457.203, 658.123), smart_home),
            Button("Volume Down", None, self.smart_home.television, "Assets/Buttons/button_vol_down.png", None,
                   (1457.201, 805.918), smart_home),
            Button("Channel Up", None, self.smart_home.television, "Assets/Buttons/button_ch_up.png", None,
                   (1656.235, 659.811), smart_home),
            Button("Channel Down", None, self.smart_home.television, "Assets/Buttons/button_ch_down.png", None,
                   (1656.234, 807.606), smart_home)
        ]
        self.buttons_Fridge = [
            Button("Exit", None, None, "Assets/Buttons/button_exit.png", None, (1779.693, 246.525), smart_home),
            Button("Minus Fridge", None, self.smart_home.kitchen_fridge, "Assets/Buttons/button_minus.png", None,
                   (1438.592, 943.541), smart_home),
            Button("Minus Freezer", None, self.smart_home.kitchen_fridge, "Assets/Buttons/button_minus.png", None,
                   (1665.936, 943.541), smart_home),
            Button("Plus Fridge", None, self.smart_home.kitchen_fridge, "Assets/Buttons/button_plus.png", None,
                   (1520.165, 943.541), smart_home),
            Button("Plus Freezer", None, self.smart_home.kitchen_fridge, "Assets/Buttons/button_plus.png", None,
                   (1747.509, 943.541), smart_home)
        ]
        self.buttons_Thermostat = [
            Button("Exit", None, None, "Assets/Buttons/button_exit.png", None, (1779.693, 246.525), smart_home),
            Button("Minus Bedroom", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_minus.png", None,
                   (1423.233, 626.518), smart_home),
            Button("Minus Bathroom", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_minus.png", None,
                   (1650.508, 626.518), smart_home),
            Button("Plus Bedroom", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_plus.png", None,
                   (1527.669, 626.518), smart_home),
            Button("Plus Bathroom", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_plus.png", None,
                   (1754.944, 626.518), smart_home),
            Button("Minus Livingroom", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_minus.png", None,
                   (1423.233, 928.463), smart_home),
            Button("Minus Kitchen", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_minus.png", None,
                   (1650.508, 928.463), smart_home),
            Button("Plus Livingroom", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_plus.png", None,
                   (1527.669, 928.463), smart_home),
            Button("Plus Kitchen", None, self.smart_home.thermostat_bathroom, "Assets/Buttons/button_plus.png", None,
                   (1754.944, 928.463), smart_home)
        ]
        self.buttons_Doorbell = [
            Button("Exit", None, None, "Assets/Buttons/button_exit.png", None, (1779.693, 246.525), smart_home),
            Button("Door2", "Entrance", self.smart_home.entrance_door, "Assets/Buttons/button_door2.png",
                   "Assets/Buttons/button_door_pressed2.png", (1461.809, 772.288), smart_home)
        ]

    def handle_event(self, event):
        if self.smart_home.visible_Automation:
            self.automation.handle_event(event)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.visibility_start()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button

                # Home Menu is visible - Camera Menu is not - TV Menu is not - Fridge Menu is not
                if self.smart_home.visible_Start and not self.visible_Camera and not self.visible_TV and \
                        not self.visible_Fridge and not self.visible_Thermostat and not self.visible_Doorbell:
                    for button in self.buttons_Start:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "Camera":
                                self.visibility_camera()
                            elif button.name == "TV":
                                self.visibility_tv()
                            elif button.name == "Fridge":
                                self.visibility_fridge()
                            elif button.name == "Thermostat":
                                self.visibility_thermostat()
                            elif button.name == "Doorbell":
                                self.visibility_doorbell()
                            elif button.name == "Automation":
                                self.visibility_automation()
                            else:
                                button.perform_action()
                                self.perform_automation(button)
                # Home Menu is visible - Camera Menu is visible - TV Menu is not - Fridge Menu is not
                elif self.smart_home.visible_Start and self.visible_Camera and not self.visible_TV and \
                        not self.visible_Fridge and not self.visible_Thermostat and not self.visible_Doorbell:
                    for button in self.buttons_Camera:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "Exit":
                                self.visibility_camera()
                            else:
                                button.perform_action()
                                self.perform_automation(button)
                # Home Menu is visible - Camera Menu is not - TV Menu is visible - Fridge Menu is not
                elif self.smart_home.visible_Start and not self.visible_Camera and self.visible_TV and \
                        not self.visible_Fridge and not self.visible_Thermostat and not self.visible_Doorbell:
                    for button in self.buttons_TV:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "Exit":
                                self.visibility_tv()
                            else:
                                button.perform_action()
                                self.perform_automation(button)
                elif self.smart_home.visible_Start and not self.visible_Camera and not self.visible_TV and \
                        self.visible_Fridge and not self.visible_Thermostat and not self.visible_Doorbell:
                    for button in self.buttons_Fridge:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "Exit":
                                self.visibility_fridge()
                            else:
                                button.perform_action()
                elif self.smart_home.visible_Start and not self.visible_Camera and not self.visible_TV and \
                        not self.visible_Fridge and self.visible_Thermostat and not self.visible_Doorbell:
                    for button in self.buttons_Thermostat:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "Exit":
                                self.visibility_thermostat()
                            else:
                                button.perform_action()
                elif self.smart_home.visible_Start and not self.visible_Camera and not self.visible_TV and \
                        not self.visible_Fridge and not self.visible_Thermostat and self.visible_Doorbell:
                    for button in self.buttons_Doorbell:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "Exit":
                                self.visibility_doorbell()
                            else:
                                button.perform_action()
                                self.perform_automation(button)

    def draw(self, screen):
        if self.smart_home.visible_Automation:
            self.automation.draw(screen)
        else:
            if self.smart_home.visible_Start:
                screen.blit(self.image, (1351, 42))  # Draw the image
                if self.visible_Camera:
                    screen.blit(self.image_Camera_Menu, (1377.386, 220.390))
                    for button in self.buttons_Camera:
                        button.entry_door_check()
                        screen.blit(button.image, button.position)
                    self.draw_garage_camera(screen)
                elif self.visible_TV:
                    screen.blit(self.image_TV_Menu, (1377.386, 220.390))
                    for button in self.buttons_TV:
                        screen.blit(button.image, button.position)
                elif self.visible_Fridge:
                    screen.blit(self.image_Fridge_Menu, (1377.386, 220.390))
                    for button in self.buttons_Fridge:
                        screen.blit(button.image, button.position)
                    font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 35)
                    screen.blit(font.render(self.smart_home.kitchen_fridge.fridge_temp_text, True, (0, 0, 0)), (1468.616, 887.673))
                    screen.blit(font.render(self.smart_home.kitchen_fridge.freezer_temp_text, True, (0, 0, 0)), (1681.863, 887.673))
                elif self.visible_Thermostat:
                    screen.blit(self.image_Thermostat_Menu, (1377.386, 220.390))
                    for button in self.buttons_Thermostat:
                        screen.blit(button.image, button.position)
                    font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 49)
                    screen.blit(font.render(self.smart_home.thermostat_bathroom.bedroom_temp_text, True, (0, 0, 0)), (1444.986+15, 508.686))
                    screen.blit(font.render(self.smart_home.thermostat_bathroom.bathroom_temp_text, True, (0, 0, 0)), (1672.261+15, 508.686))
                    screen.blit(font.render(self.smart_home.thermostat_bathroom.livingroom_temp_text, True, (0, 0, 0)), (1444.986+15, 810.631))
                    screen.blit(font.render(self.smart_home.thermostat_bathroom.kitchen_temp_text, True, (0, 0, 0)), (1672.261+15, 810.631))
                elif self.visible_Doorbell:
                    screen.blit(self.image_Doorbell_Menu, (1377.386, 220.390))
                    for button in self.buttons_Doorbell:
                        button.entry_door_check()
                        screen.blit(button.image, button.position)
                    self.draw_doorbell_camera(screen)
                else:
                    for button in self.buttons_Start:
                        button.entry_door_check()
                        screen.blit(button.image, button.position)

    def visibility_start(self):
        self.smart_home.visible_Start = not self.smart_home.visible_Start

    def visibility_camera(self):
        self.visible_Camera = not self.visible_Camera

    def visibility_tv(self):
        self.visible_TV = not self.visible_TV

    def visibility_fridge(self):
        self.visible_Fridge = not self.visible_Fridge

    def visibility_thermostat(self):
        self.visible_Thermostat = not self.visible_Thermostat

    def visibility_doorbell(self):
        self.visible_Doorbell = not self.visible_Doorbell

    def draw_doorbell_camera(self, screen):
        screen.blit(pygame.transform.scale(pygame.image.load(self.smart_home.doorbell_event), (410, 263)), (1411.859, 442.807))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Live.png"), (74, 30)), (1437.765, 456.057))

    def visibility_automation(self):
        self.smart_home.visible_Automation = not self.smart_home.visible_Automation

    def draw_garage_camera(self, screen):
        if self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Closed.png" or self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Open.png":
            if self.smart_home.garage_door.closed:
                self.smart_home.garage_event = "Assets/Backgrounds/Camera_Garage_Closed.png"
            elif not self.smart_home.garage_door.closed:
                self.smart_home.garage_event = "Assets/Backgrounds/Camera_Garage_Open.png"
        elif self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Closed_Cat.png" or self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Open_Cat.png":
            if self.smart_home.garage_door.closed:
                self.smart_home.garage_event = "Assets/Backgrounds/Camera_Garage_Closed_Cat.png"
            elif not self.smart_home.garage_door.closed:
                self.smart_home.garage_event = "Assets/Backgrounds/Camera_Garage_Open_Cat.png"
        else:
            if self.smart_home.garage_door.closed:
                self.smart_home.garage_event = "Assets/Backgrounds/Camera_Garage_Closed_Thief.png"
            elif not self.smart_home.garage_door.closed:
                self.smart_home.garage_event = "Assets/Backgrounds/Camera_Garage_Open_Thief.png"
        screen.blit(pygame.transform.scale(pygame.image.load(self.smart_home.garage_event), (304, 263)), (1465.269, 433.696))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Live.png"), (74, 30)), (1490.961, 446.945))

    def perform_automation(self, button):
        for automation in self.smart_home.automations_device:
            if automation.when == "Entrance - Door" and button.name == "Door1" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Entrance - Door" and button.name == "Door2" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Living Room - Television" and button.name == "TV2" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Living Room - Ceiling Lights" and button.name == "Ceiling Lights" and button.place == "Living Room" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Living Room - Floor Lamp" and button.name == "Floor Lamp" and button.place == "Living Room" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Kitchen - Ceiling Lights" and button.name == "Ceiling Lights" and button.place == "Kitchen" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Bedroom - Blinds" and button.name == "Blinds" and button.place == "Bedroom" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Bedroom - Ceiling Lights" and button.name == "Ceiling Lights" and button.place == "Bedroom" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Bedroom - Nightstand Lamp" and button.name == "Nightstand Lamp" and button.place == "Bedroom" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Bathroom - Blinds" and button.name == "Blinds" and button.place == "Bathroom" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Bathroom - Lights" and button.name == "Lights" and button.place == "Bathroom" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Garage - Door" and button.name == "Garage Door1" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)
            elif automation.when == "Garage - Door" and button.name == "Garage Door2" and automation.state1 == button.device.get_state():
                self.automation_helper(automation)

    def automation_helper(self, automation):
        if automation.do == "Living Room - Television" and self.buttons_TV[1].device.get_state() is not automation.state2:
            self.buttons_TV[1].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Living Room - Ceiling Lights" and self.buttons_Start[3].device.get_state() is not automation.state2:
            self.buttons_Start[3].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Living Room - Floor Lamp" and self.buttons_Start[8].device.get_state() is not automation.state2:
            self.buttons_Start[8].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Kitchen - Ceiling Lights" and self.buttons_Start[4].device.get_state() is not automation.state2:
            self.buttons_Start[4].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Bedroom - Blinds" and self.buttons_Start[0].device.get_state() is not automation.state2:
            self.buttons_Start[0].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Bedroom - Ceiling Lights" and self.buttons_Start[2].device.get_state() is not automation.state2:
            self.buttons_Start[2].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Bedroom - Nightstand Lamp" and self.buttons_Start[7].device.get_state() is not automation.state2:
            self.buttons_Start[7].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Bathroom - Blinds" and self.buttons_Start[1].device.get_state() is not automation.state2:
            self.buttons_Start[1].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Bathroom - Lights" and self.buttons_Start[5].device.get_state() is not automation.state2:
            self.buttons_Start[5].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Garage - Door" and self.buttons_Start[6].device.get_state() is not automation.state2:
            self.buttons_Start[6].perform_action()
            self.automation_notification(automation)
        elif automation.do == "Entrance - Door" and self.buttons_Start[12].device.get_state() is not automation.state2:
            self.buttons_Start[12].perform_action()
            self.automation_notification(automation)

    def automation_notification(self, automation):
        self.smart_home.notifications.append(Notification("⚙ Automation: " + automation.when + "(" + automation.state1 + ") ➡ " + automation.do + "(" + automation.state1 + ")", 7000))

    def automation_notification2(self, automation):
        self.smart_home.notifications.append(Notification("⚙ Automation: " + automation.when + " ➡ " + automation.do + "(" + automation.state + ")", 7000))

    def automation_helper2(self, automation):
        if automation.do == "Living Room - Television" and self.buttons_TV[1].device.get_state() is not automation.state:
            self.buttons_TV[1].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Living Room - Ceiling Lights" and self.buttons_Start[3].device.get_state() is not automation.state:
            self.buttons_Start[3].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Living Room - Floor Lamp" and self.buttons_Start[8].device.get_state() is not automation.state:
            self.buttons_Start[8].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Kitchen - Ceiling Lights" and self.buttons_Start[4].device.get_state() is not automation.state:
            self.buttons_Start[4].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Bedroom - Blinds" and self.buttons_Start[0].device.get_state() is not automation.state:
            self.buttons_Start[0].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Bedroom - Ceiling Lights" and self.buttons_Start[2].device.get_state() is not automation.state:
            self.buttons_Start[2].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Bedroom - Nightstand Lamp" and self.buttons_Start[7].device.get_state() is not automation.state:
            self.buttons_Start[7].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Bathroom - Blinds" and self.buttons_Start[1].device.get_state() is not automation.state:
            self.buttons_Start[1].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Bathroom - Lights" and self.buttons_Start[5].device.get_state() is not automation.state:
            self.buttons_Start[5].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Garage - Door" and self.buttons_Start[6].device.get_state() is not automation.state:
            self.buttons_Start[6].perform_action()
            self.automation_notification2(automation)
        elif automation.do == "Entrance - Door" and self.buttons_Start[12].device.get_state() is not automation.state:
            self.buttons_Start[12].perform_action()
            self.automation_notification2(automation)

    def perform_time_automation(self):
        if not self.smart_home.automation_done:
            for automation in self.smart_home.automations_time:
                if self.smart_home.current_time_state == "Morning" and automation.when == "Sunrise":
                    self.automation_helper2(automation)
                elif self.smart_home.current_time_state == "Day" and automation.when == "Daylight":
                    self.automation_helper2(automation)
                elif self.smart_home.current_time_state == "Noon" and automation.when == "Midday":
                    self.automation_helper2(automation)
                elif self.smart_home.current_time_state == "Night" and automation.when == "Nighttime":
                    self.automation_helper2(automation)
            for automation in self.smart_home.automations_sensor:
                if self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Closed_Cat.png" or self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Open_Cat.png" or self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Closed_Thief.png" or self.smart_home.garage_event == "Assets/Backgrounds/Camera_Garage_Open_Thief.png":
                    if automation.when == "Garage - Motion Sensor":
                        self.automation_helper2(automation)
                elif self.smart_home.doorbell_event == "Assets/Backgrounds/Camera_Morning_Cat.png" or self.smart_home.doorbell_event == "Assets/Backgrounds/Camera_Day_Cat.png" or self.smart_home.doorbell_event == "Assets/Backgrounds/Camera_Night_Thief.png":
                    if automation.when == "Entrance - Motion Sensor":
                        self.automation_helper2(automation)
        self.smart_home.automation_done = True


