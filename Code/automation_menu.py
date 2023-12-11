import pygame

from automation import AutomationTime, AutomationSensor, AutomationDevice
from notifications import Notification
from button import Button


class AutomationMenu:
    def __init__(self, smart_home):
        self.image_New_Automation = pygame.transform.scale(pygame.image.load("Assets/Menus/New_Automation.png"),
                                                           (532, 1001))
        self.image_My_Automation = pygame.transform.scale(pygame.image.load("Assets/Menus/My_Automations.png"),
                                                          (532, 1001))
        self.smart_home = smart_home
        self.visible_My_Automations = False

        # Time Automation ############################################################################################
        self.image_Time_Automation = pygame.transform.scale(pygame.image.load("Assets/Menus/Time_Automation.png"),
                                                            (532, 1001))
        self.image_Time_Automation2 = pygame.transform.scale(pygame.image.load("Assets/Menus/Time_Automation_2.png"),
                                                             (532, 1001))
        self.image_Time_Automation3 = pygame.transform.scale(pygame.image.load("Assets/Menus/Time_Automation_3.png"),
                                                             (532, 1001))
        self.visible_Time_Automation = False
        self.time_names = ["Sunrise", "Daylight", "Midday", "Nighttime"]
        self.time_checked = [False, False, False, False]
        self.time_next = False

        self.visible_Time_Automation2 = False
        self.time_checked2 = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.time_next2 = False

        self.visible_Time_Automation3 = False
        self.time_active_inactive_names = []
        self.time_active_inactive = [False, False]
        self.time_next3 = False

        # Sensor Automation ##########################################################################################
        self.image_Sensor_Automation = pygame.transform.scale(pygame.image.load("Assets/Menus/Sensor_Automation.png"),
                                                              (532, 1001))
        self.visible_Sensor_Automation = False
        self.sensor_names = ["Entrance - Motion Sensor", "Garage - Motion Sensor"]
        self.sensor_checked = [False, False]
        self.sensor_next = False

        self.image_Sensor_Automation2 = pygame.transform.scale(
            pygame.image.load("Assets/Menus/Sensor_Automation_2.png"),
            (532, 1001))
        self.visible_Sensor_Automation2 = False
        self.sensor_checked2 = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.sensor_next2 = False

        self.image_Sensor_Automation3 = pygame.transform.scale(
            pygame.image.load("Assets/Menus/Sensor_Automation_3.png"),
            (532, 1001))
        self.visible_Sensor_Automation3 = False
        self.sensor_active_inactive_names = []
        self.sensor_active_inactive = [False, False]
        self.sensor_next3 = False

        # Device Automation ##########################################################################################
        self.image_Device_Automation = pygame.transform.scale(pygame.image.load("Assets/Menus/Device_Automation.png"),
                                                              (532, 1001))
        self.image_Device_Automation2 = pygame.transform.scale(
            pygame.image.load("Assets/Menus/Device_Automation_2.png"),
            (532, 1001))
        self.image_Device_Automation3 = pygame.transform.scale(
            pygame.image.load("Assets/Menus/Device_Automation_3.png"),
            (532, 1001))
        self.image_Device_Automation4 = pygame.transform.scale(
            pygame.image.load("Assets/Menus/Device_Automation_4.png"),
            (532, 1001))

        self.visible_Device_Automation = False

        self.devices_names = ["Entrance - Door", "Living Room - Television", "Living Room - Ceiling Lights",
                              "Living Room - Floor Lamp", "Kitchen - Ceiling Lights", "Bedroom - Blinds",
                              "Bedroom - Ceiling Lights", "Bedroom - Nightstand Lamp", "Bathroom - Blinds",
                              "Bathroom - Lights", "Garage - Door"]

        # Device Automation Window 1
        self.devices_checked = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.devices_next = False

        # Device Automation Window 2
        self.visible_Device_Automation2 = False
        self.active_inactive_names = []
        self.devices_active_inactive = [False, False]
        self.devices_next2 = False

        # Device Automation Window 3
        self.visible_Device_Automation3 = False
        self.devices_names3 = []
        self.devices_checked3 = []
        self.devices_next3 = False

        # Device Automation Window 4
        self.visible_Device_Automation4 = False
        self.devices_active_inactive_names4 = []
        self.devices_active_inactive4 = [False, False]
        self.devices_next4 = False

        # Buttons
        self.buttons_New_Automation = [
            Button("Time", None, None, "Assets/Buttons/button_automation_time.png", None, (1402.341, 287.116),
                   smart_home),
            Button("Device", None, None, "Assets/Buttons/button_automation_device.png", None, (1402.341, 393.128),
                   smart_home),
            Button("Sensor", None, None, "Assets/Buttons/button_automation_sensor.png", None, (1402.341, 499.141),
                   smart_home),
            Button("List", None, None, "Assets/Buttons/button_automation_list.png", None, (1402.341, 691.154),
                   smart_home),
            Button("Cancel", None, None, "Assets/Buttons/button_cancel.png", None, (1418.908, 941.936), smart_home)
        ]
        self.buttons_back_next = [
            Button("Back", None, None, "Assets/Buttons/button_back.png", None, (1418.908, 941.936), smart_home),
            Button("Next", None, None, "Assets/Buttons/button_next.png", None, (1739.065, 941.936), smart_home)
        ]
        self.buttons_back_done = [
            Button("Back", None, None, "Assets/Buttons/button_back.png", None, (1418.908, 941.936), smart_home),
            Button("Done", None, None, "Assets/Buttons/button_done.png", None, (1739.065, 941.936), smart_home)
        ]
        self.buttons_back = [
            Button("Back", None, None, "Assets/Buttons/button_back.png", None, (1418.908, 941.936), smart_home),
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.visibility_start()
            self.visibility_automation()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button

            # Automation Menu
            if self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Time_Automation3 and not self.visible_Device_Automation \
                    and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_New_Automation:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Cancel":
                            self.visibility_automation()
                        elif button.name == "Device":
                            self.visibility_automation_device()
                        elif button.name == "Time":
                            self.visibility_automation_time()
                        elif button.name == "Sensor":
                            self.visibility_automation_sensor()
                        elif button.name == "List":
                            self.visibility_my_automations()
            # Device Automation Window 1
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Time_Automation3 and self.visible_Device_Automation \
                    and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_next:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_device()
                        elif button.name == "Next" and self.devices_next:
                            self.visibility_automation_device2()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.devices_names):
                    if pygame.Rect((x + 380, 320 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.devices_checked):
                            self.devices_checked[x] = False
                        self.devices_checked[i] = not self.devices_checked[i]
                    y = y + 55
                    if not any(self.devices_checked):
                        self.devices_next = False
                    else:
                        self.devices_next = True
            # Device Automation Window 2
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Time_Automation3 and self.visible_Device_Automation \
                    and self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_next:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_device2()
                        elif button.name == "Next" and self.devices_next2:
                            self.visibility_automation_device3()
                            self.new_devices_names()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.devices_active_inactive):
                    if pygame.Rect((x + 380, 390 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.devices_active_inactive):
                            self.devices_active_inactive[x] = False
                        self.devices_active_inactive[i] = not self.devices_active_inactive[i]
                    y = y + 55
                    if not any(self.devices_active_inactive):
                        self.devices_next2 = False
                    else:
                        self.devices_next2 = True
            # Device Automation Window 3
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Time_Automation3 and self.visible_Device_Automation \
                    and self.visible_Device_Automation2 and self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_next:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_device3()
                            self.devices_checked3.clear()
                            self.devices_names3.clear()
                        elif button.name == "Next" and self.devices_next3:
                            # self.selected_devices_names()
                            self.visibility_automation_device4()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.devices_names3):
                    if pygame.Rect((x + 380, 320 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.devices_checked3):
                            self.devices_checked3[x] = False
                        self.devices_checked3[i] = not self.devices_checked3[i]
                    y = y + 55
                    if not any(self.devices_checked3):
                        self.devices_next3 = False
                    else:
                        self.devices_next3 = True
            # Device Automation Window 4
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Time_Automation3 and self.visible_Device_Automation \
                    and self.visible_Device_Automation2 and self.visible_Device_Automation3 and self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_done:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_device4()
                            self.devices_active_inactive_names4.clear()
                            # self.devices_active_inactive4.clear()
                        elif button.name == "Done" and self.devices_next4:
                            self.create_device_automation()
                            self.reset_values_devices()
                            self.visibility_automation_device()
                            self.visibility_automation_device2()
                            self.visibility_automation_device3()
                            self.visibility_automation_device4()
                            self.smart_home.notifications.append(Notification("New Notification was created!", 5000))
                            self.visibility_my_automations()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.devices_active_inactive_names4):
                    if pygame.Rect((x + 380, 395 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.devices_active_inactive4):
                            self.devices_active_inactive4[x] = False
                        self.devices_active_inactive4[i] = not self.devices_active_inactive4[i]
                    y = y + 55
                    if not any(self.devices_active_inactive4):
                        self.devices_next4 = False
                    else:
                        self.devices_next4 = True
            # Time Automation #########################################################################################
            elif self.smart_home.visible_Automation and self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Device_Automation \
                    and not self.visible_Time_Automation3 and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_next:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_time()
                        if button.name == "Next" and self.time_next:
                            self.visibility_automation_time2()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.time_names):
                    if pygame.Rect((x + 380, 325 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.time_checked):
                            self.time_checked[x] = False
                        self.time_checked[i] = not self.time_checked[i]
                    y = y + 55
                    if not any(self.time_checked):
                        self.time_next = False
                    else:
                        self.time_next = True
            # Time Automation 2
            elif self.smart_home.visible_Automation and self.visible_Time_Automation and self.visible_Time_Automation2 \
                    and not self.visible_Time_Automation3 and not self.visible_Device_Automation and not self.visible_Device_Automation2 and not \
                    self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_next:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_time2()
                        if button.name == "Next" and self.time_next2:
                            self.visibility_automation_time3()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.devices_names):
                    if pygame.Rect((x + 380, 325 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.time_checked2):
                            self.time_checked2[x] = False
                        self.time_checked2[i] = not self.time_checked2[i]
                    y = y + 55
                    if not any(self.time_checked2):
                        self.time_next2 = False
                    else:
                        self.time_next2 = True
            # Time Automation 3
            elif self.smart_home.visible_Automation and self.visible_Time_Automation and self.visible_Time_Automation2 \
                    and self.visible_Time_Automation3 and not self.visible_Device_Automation \
                    and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 \
                    and not self.visible_Device_Automation4 and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_done:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_time3()
                            self.time_active_inactive_names.clear()
                        if button.name == "Done" and self.time_next3:
                            self.create_time_automation()
                            self.reset_values_time()
                            self.visibility_automation_time()
                            self.visibility_automation_time2()
                            self.visibility_automation_time3()
                            self.smart_home.notifications.append(Notification("New Notification was created!", 5000))
                            self.visibility_my_automations()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.time_active_inactive_names):
                    if pygame.Rect((x + 380, 395 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.time_active_inactive):
                            self.time_active_inactive[x] = False
                        self.time_active_inactive[i] = not self.time_active_inactive[i]
                    y = y + 55
                    if not any(self.time_active_inactive):
                        self.time_next3 = False
                    else:
                        self.time_next3 = True
            # Sensor Automation #####################################################################################
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Device_Automation \
                    and not self.visible_Time_Automation3 and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_next:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_sensor()
                        if button.name == "Next" and self.sensor_next:
                            self.visibility_automation_sensor2()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.sensor_names):
                    if pygame.Rect((x + 380, 325 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.sensor_checked):
                            self.sensor_checked[x] = False
                        self.sensor_checked[i] = not self.sensor_checked[i]
                    y = y + 55
                    if not any(self.sensor_checked):
                        self.sensor_next = False
                    else:
                        self.sensor_next = True
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Device_Automation \
                    and not self.visible_Time_Automation3 and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and self.visible_Sensor_Automation and self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_next:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_sensor2()
                        if button.name == "Next" and self.sensor_next2:
                            self.visibility_automation_sensor3()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.devices_names):
                    if pygame.Rect((x + 380, 325 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.sensor_checked2):
                            self.sensor_checked2[x] = False
                        self.sensor_checked2[i] = not self.sensor_checked2[i]
                    y = y + 55
                    if not any(self.sensor_checked2):
                        self.sensor_next2 = False
                    else:
                        self.sensor_next2 = True
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Device_Automation \
                    and not self.visible_Time_Automation3 and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and self.visible_Sensor_Automation and self.visible_Sensor_Automation2 and self.visible_Sensor_Automation3 and not self.visible_My_Automations:
                for button in self.buttons_back_done:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_automation_sensor3()
                        if button.name == "Done" and self.sensor_next3:
                            self.create_sensor_automation()
                            self.reset_values_sensors()
                            self.visibility_automation_sensor()
                            self.visibility_automation_sensor2()
                            self.visibility_automation_sensor3()
                            self.smart_home.notifications.append(Notification("New Notification was created!", 5000))
                            self.visibility_my_automations()
                        else:
                            self.select_option_notification()
                x, y = 1412.907, 0
                for i, device in enumerate(self.sensor_active_inactive_names):
                    if pygame.Rect((x + 380, 395 + y), (20, 20)).collidepoint(event.pos):
                        for x, _ in enumerate(self.sensor_active_inactive):
                            self.sensor_active_inactive[x] = False
                        self.sensor_active_inactive[i] = not self.sensor_active_inactive[i]
                    y = y + 55
                    if not any(self.sensor_active_inactive):
                        self.sensor_next3 = False
                    else:
                        self.sensor_next3 = True
            elif self.smart_home.visible_Automation and not self.visible_Time_Automation and not self.visible_Time_Automation2 and not self.visible_Device_Automation \
                    and not self.visible_Time_Automation3 and not self.visible_Device_Automation2 and not self.visible_Device_Automation3 and not self.visible_Device_Automation4 \
                    and not self.visible_Sensor_Automation and not self.visible_Sensor_Automation2 and not self.visible_Sensor_Automation3 and self.visible_My_Automations:
                for button in self.buttons_back_done:
                    if button.rect.collidepoint(event.pos):
                        if button.name == "Back":
                            self.visibility_my_automations()

    def draw(self, screen):
        if self.smart_home.visible_Automation:
            screen.blit(self.image_New_Automation, (1351, 42))
            for button in self.buttons_New_Automation:
                screen.blit(button.image, button.position)
        # Device Automation 1
        if self.visible_Device_Automation:
            screen.blit(self.image_Device_Automation, (1351, 42))
            self.draw_devices(screen)
            for button in self.buttons_back_next:
                screen.blit(button.image, button.position)
        # Device Automation 2
        if self.visible_Device_Automation2:
            screen.blit(self.image_Device_Automation2, (1351, 42))
            self.draw_active_inactive(screen, self.devices_checked, self.devices_names)
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 30)
            text = font.render(self.get_device_name(self.devices_checked, self.devices_names), True, (0, 0, 0))
            screen.blit(text, (1412.035, 300))
            for button in self.buttons_back_next:
                screen.blit(button.image, button.position)
        # Device Automation 3
        if self.visible_Device_Automation3:
            screen.blit(self.image_Device_Automation3, (1351, 42))
            self.draw_devices3(screen)
            for button in self.buttons_back_next:
                screen.blit(button.image, button.position)
        # Device Automation 4
        if self.visible_Device_Automation4:
            screen.blit(self.image_Device_Automation4, (1351, 42))
            self.draw_active_inactive4(screen, self.devices_checked3, self.devices_names3)
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 21)
            text = font.render(self.get_device_name(self.devices_checked, self.devices_names), True, (0, 0, 0))
            screen.blit(text, (1495, 222))
            text = font.render(self.get_device_name(self.devices_checked3, self.devices_names3), True, (0, 0, 0))
            screen.blit(text, (1460, 275))
            for button in self.buttons_back_done:
                screen.blit(button.image, button.position)
        # Time Automation 1
        if self.visible_Time_Automation:
            screen.blit(self.image_Time_Automation, (1351, 42))
            self.draw_time_sensor(screen, self.time_checked, self.time_names)
            for button in self.buttons_back_next:
                screen.blit(button.image, button.position)
        # Time Automation 2
        if self.visible_Time_Automation2:
            screen.blit(self.image_Time_Automation2, (1351, 42))
            self.draw_time_sensor(screen, self.time_checked2, self.devices_names)
            for button in self.buttons_back_next:
                screen.blit(button.image, button.position)
        # Time Automation 3
        if self.visible_Time_Automation3:
            screen.blit(self.image_Time_Automation3, (1351, 42))
            self.time_draw_active_inactive(screen, self.time_checked2, self.devices_names)
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 21)
            text = font.render(self.get_device_name(self.time_checked, self.time_names), True, (0, 0, 0))
            screen.blit(text, (1495, 222))
            text = font.render(self.get_device_name(self.time_checked2, self.devices_names), True, (0, 0, 0))
            screen.blit(text, (1460, 275))
            for button in self.buttons_back_done:
                screen.blit(button.image, button.position)
        # Sensor Automation 1
        if self.visible_Sensor_Automation:
            screen.blit(self.image_Sensor_Automation, (1351, 42))
            self.draw_time_sensor(screen, self.sensor_checked, self.sensor_names)
            for button in self.buttons_back_next:
                screen.blit(button.image, button.position)
        # Sensor Automation 2
        if self.visible_Sensor_Automation2:
            screen.blit(self.image_Sensor_Automation2, (1351, 42))
            self.draw_time_sensor(screen, self.sensor_checked2, self.devices_names)
            for button in self.buttons_back_next:
                screen.blit(button.image, button.position)
        # Sensor Automation 3
        if self.visible_Sensor_Automation3:
            screen.blit(self.image_Sensor_Automation3, (1351, 42))
            self.sensor_draw_active_inactive(screen, self.sensor_checked2, self.devices_names)
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 21)
            text = font.render(self.get_device_name(self.sensor_checked, self.sensor_names), True, (0, 0, 0))
            screen.blit(text, (1495, 222))
            text = font.render(self.get_device_name(self.sensor_checked2, self.devices_names), True, (0, 0, 0))
            screen.blit(text, (1460, 275))
            for button in self.buttons_back_done:
                screen.blit(button.image, button.position)
        if self.visible_My_Automations:
            screen.blit(self.image_My_Automation, (1351, 42))
            self.draw_my_automations(screen)
            for button in self.buttons_back:
                screen.blit(button.image, button.position)

    def reset_values_time(self):
        self.time_checked = [False, False, False, False]
        self.time_next = False
        self.time_checked2 = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.time_next2 = False
        self.time_active_inactive_names = []
        self.time_active_inactive = [False, False]
        self.time_next3 = False

    def reset_values_devices(self):
        self.devices_checked = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.devices_next = False
        self.active_inactive_names = []
        self.devices_active_inactive = [False, False]
        self.devices_next2 = False
        self.devices_names3 = []
        self.devices_checked3 = []
        self.devices_next3 = False
        self.devices_active_inactive_names4 = []
        self.devices_active_inactive4 = [False, False]
        self.devices_next4 = False

    def reset_values_sensors(self):
        self.sensor_checked = [False, False]
        self.sensor_next = False
        self.sensor_checked2 = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.sensor_next2 = False
        self.sensor_active_inactive_names = []
        self.sensor_active_inactive = [False, False]
        self.sensor_next3 = False

    def create_time_automation(self):
        when = self.get_device_name(self.time_checked, self.time_names)
        do = self.get_device_name(self.time_checked2, self.devices_names)
        if self.time_active_inactive[0]:
            state = "Active"
        else:
            state = "Inactive"
        self.smart_home.automations_time.append(AutomationTime(when, do, state))

    def create_sensor_automation(self):
        when = self.get_device_name(self.sensor_checked, self.sensor_names)
        do = self.get_device_name(self.sensor_checked2, self.devices_names)
        if self.sensor_active_inactive[0]:
            state = "Active"
        else:
            state = "Inactive"
        self.smart_home.automations_sensor.append(AutomationSensor(when, do, state))

    def create_device_automation(self):
        when = self.get_device_name(self.devices_checked, self.devices_names)
        if self.devices_active_inactive[0]:
            state1 = "Active"
        else:
            state1 = "Inactive"
        do = self.get_device_name(self.devices_checked3, self.devices_names3)
        if self.devices_active_inactive4[0]:
            state2 = "Active"
        else:
            state2 = "Inactive"
        self.smart_home.automations_device.append(AutomationDevice(when, state1, do, state2))

    def new_devices_names(self):
        for i, name in enumerate(self.devices_names):
            if not self.devices_checked[i]:
                self.devices_names3.append(name)
                self.devices_checked3.append(False)

    def select_option_notification(self):
        self.smart_home.notifications.append(Notification("⚠ Please select an option", 3000))
        pygame.mixer.music.load("Assets/Sounds/stop.mp3")
        pygame.mixer.music.play()

    def draw_my_automations(self, screen):
        x, y = 1412.907, 0
        font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 20)
        for a in self.smart_home.automations_device:
            text = font.render("When: " + a.when + " (" + a.state1 + ")", True, (0, 0, 0))
            screen.blit(text, (x, 280 + y))
            y = y + 35
            text = font.render("Do: " + a.do + " (" + a.state1 + ")", True, (0, 0, 0))
            screen.blit(text, (x, 280 + y))
            y = y + 55
        for a in self.smart_home.automations_time:
            text = font.render("When: " + a.when, True, (0, 0, 0))
            screen.blit(text, (x, 280 + y))
            y = y + 35
            text = font.render("Do: " + a.do + " (" + a.state + ")", True, (0, 0, 0))
            screen.blit(text, (x, 280 + y))
            y = y + 55
        for a in self.smart_home.automations_sensor:
            text = font.render("When: " + a.when, True, (0, 0, 0))
            screen.blit(text, (x, 280 + y))
            y = y + 35
            text = font.render("Do: " + a.do + " (" + a.state + ")", True, (0, 0, 0))
            screen.blit(text, (x, 280 + y))
            y = y + 55

    # Time Automation Functions ######################################################################################
    def draw_time_sensor(self, screen, check, names):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        for i, device in enumerate(names):
            # Draw checkbox
            checkbox_color = black if check[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 325 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 325 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(device, True, black)
            screen.blit(text, (x, 320 + y))
            y = y + 55

    def time_draw_active_inactive(self, screen, checked, names):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        self.get_time_active_inactive_terms(checked, names)
        for i, word in enumerate(self.time_active_inactive_names):
            # Draw checkbox
            checkbox_color = black if self.time_active_inactive[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 395 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 395 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(word, True, black)
            screen.blit(text, (x, 390 + y))
            y = y + 55

    def get_time_active_inactive_terms(self, checked, names):
        if self.get_device_name(checked, names).__contains__("Television") or self.get_device_name(checked,
                                                                                                   names).__contains__(
            "Lights") or self.get_device_name(checked, names).__contains__("Lamp"):
            self.time_active_inactive_names = ["On", "Off"]
        else:
            self.time_active_inactive_names = ["Open", "Close"]

    # Sensor Automation Functions ###################################################################################
    def sensor_draw_active_inactive(self, screen, checked, names):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        self.get_sensor_active_inactive_terms(checked, names)
        for i, word in enumerate(self.sensor_active_inactive_names):
            # Draw checkbox
            checkbox_color = black if self.sensor_active_inactive[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 395 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 395 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(word, True, black)
            screen.blit(text, (x, 390 + y))
            y = y + 55

    def get_sensor_active_inactive_terms(self, checked, names):
        if self.get_device_name(checked, names).__contains__("Television") or self.get_device_name(checked,
                                                                                                   names).__contains__(
            "Lights") or self.get_device_name(checked, names).__contains__("Lamp"):
            self.sensor_active_inactive_names = ["On", "Off"]
        else:
            self.sensor_active_inactive_names = ["Open", "Close"]

    # Device Automation Functions ####################################################################################
    def get_device_name(self, checked, names):
        for i, value in enumerate(checked):
            if value:
                return names[i]

    def get_active_inactive_terms(self, checked, names):
        if self.get_device_name(checked, names).__contains__("Television") or self.get_device_name(checked,
                                                                                                   names).__contains__(
            "Lights") or self.get_device_name(checked, names).__contains__("Lamp"):
            self.active_inactive_names = ["On", "Off"]
        else:
            self.active_inactive_names = ["Open", "Close"]

    def get_active_inactive_terms4(self, checked, names):
        if self.get_device_name(checked, names).__contains__("Television") or self.get_device_name(checked,
                                                                                                   names).__contains__(
            "Lights") or self.get_device_name(checked, names).__contains__("Lamp"):
            self.devices_active_inactive_names4 = ["On", "Off"]
        else:
            self.devices_active_inactive_names4 = ["Open", "Close"]

    def draw_devices(self, screen):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        for i, device in enumerate(self.devices_names):
            # Draw checkbox
            checkbox_color = black if self.devices_checked[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 325 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 325 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(device, True, black)
            screen.blit(text, (x, 320 + y))
            y = y + 55

    def draw_devices3(self, screen):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        for i, device in enumerate(self.devices_names3):
            # Draw checkbox
            checkbox_color = black if self.devices_checked3[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 325 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 325 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(device, True, black)
            screen.blit(text, (x, 320 + y))
            y = y + 55

    def draw_devices4(self, screen):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        for i, device in enumerate(self.devices_active_inactive_names4):
            # Draw checkbox
            checkbox_color = black if self.devices_active_inactive4[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 320 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 320 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(device, True, black)
            screen.blit(text, (x, 320 + y))
            y = y + 55

    def draw_active_inactive(self, screen, checked, names):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        self.get_active_inactive_terms(checked, names)
        for i, word in enumerate(self.active_inactive_names):
            # Draw checkbox
            checkbox_color = black if self.devices_active_inactive[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 395 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 395 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(word, True, black)
            screen.blit(text, (x, 390 + y))
            y = y + 55

    def draw_active_inactive4(self, screen, checked, names):
        white = (255, 255, 255)
        black = (0, 0, 0)
        x, y = 1412.907, 0
        self.get_active_inactive_terms4(checked, names)
        for i, word in enumerate(self.devices_active_inactive_names4):
            # Draw checkbox
            checkbox_color = black if self.devices_active_inactive4[i] else white
            pygame.draw.rect(screen, checkbox_color, (x + 380, 395 + y, 20, 20))
            pygame.draw.rect(screen, black, (x + 380, 395 + y, 20, 20), 2)

            # Draw device name
            font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 25)
            text = font.render(word, True, black)
            screen.blit(text, (x, 390 + y))
            y = y + 55

    def visibility_start(self):
        self.smart_home.visible_Start = not self.smart_home.visible_Start

    def visibility_automation(self):
        self.smart_home.visible_Automation = not self.smart_home.visible_Automation

    def visibility_my_automations(self):
        self.visible_My_Automations = not self.visible_My_Automations

    # Visibility of Time Automation Windows
    def visibility_automation_time(self):
        self.visible_Time_Automation = not self.visible_Time_Automation

    def visibility_automation_time2(self):
        self.visible_Time_Automation2 = not self.visible_Time_Automation2

    def visibility_automation_time3(self):
        self.visible_Time_Automation3 = not self.visible_Time_Automation3

    # Visibility of Device Automation Windows
    def visibility_automation_device(self):
        self.visible_Device_Automation = not self.visible_Device_Automation

    def visibility_automation_device2(self):
        self.visible_Device_Automation2 = not self.visible_Device_Automation2

    def visibility_automation_device3(self):
        self.visible_Device_Automation3 = not self.visible_Device_Automation3

    def visibility_automation_device4(self):
        self.visible_Device_Automation4 = not self.visible_Device_Automation4

    # Visibility of Sensor Automation Windows
    def visibility_automation_sensor(self):
        self.visible_Sensor_Automation = not self.visible_Sensor_Automation

    def visibility_automation_sensor2(self):
        self.visible_Sensor_Automation2 = not self.visible_Sensor_Automation2

    def visibility_automation_sensor3(self):
        self.visible_Sensor_Automation3 = not self.visible_Sensor_Automation3
