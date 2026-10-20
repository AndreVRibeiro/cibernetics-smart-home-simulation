import random
import platform

import pygame.image

from notifications import Notification
from smart_doorbell import Doorbell
from smart_thermostat import Thermostat
from smart_fridge import Fridge
from smart_door import Door
from smart_tv import TV
from smart_blinds import Blinds
from smart_garage import Garage
from smart_ligths import Light
from smart_camera import Camera

# Load background images
morning_image = pygame.image.load("Assets/Backgrounds/PinkMorning.png")
day_image = pygame.image.load("Assets/Backgrounds/BlueDay.png")
noon_image = pygame.image.load("Assets/Backgrounds/OrangeSunset.png")
night_image = pygame.image.load("Assets/Backgrounds/MarineblueNight.png")

morning_event = ["Assets/Backgrounds/Camera_Morning_Normal.png",
                 "Assets/Backgrounds/Camera_Morning_Cat.png"]
day_event = ["Assets/Backgrounds/Camera_Day_Normal.png",
             "Assets/Backgrounds/Camera_Day_Cat.png",
             "Assets/Backgrounds/Camera_Day_Delivery.png"]
noon_event = ["Assets/Backgrounds/Camera_Sunset_Normal.png",
              "Assets/Backgrounds/Camera_Sunset_Delivery.png"]
night_event = ["Assets/Backgrounds/Camera_Night_Normal.png",
               "Assets/Backgrounds/Camera_Night_Thief.png"]
garage_event_images = ["Assets/Backgrounds/Camera_Garage_Closed_Thief.png",
                       "Assets/Backgrounds/Camera_Garage_Closed.png",
                       "Assets/Backgrounds/Camera_Garage_Open_Cat.png"]

# Define time intervals (in seconds) for each background
morning_duration = 2
day_duration = 2
noon_duration = 2
night_duration = 2

total_cycle_duration = morning_duration + day_duration + noon_duration + night_duration


class SmartHome:

    def __init__(self):
        self.devices = [pygame.image.load("Assets/HomeTest1.png")]

        self.morning = False
        self.day = False
        self.noon = False
        self.night = False
        self.current_time_state = None
        self.new_time_state = None
        self.automation_done = False

        # Clock
        self.clock = pygame.time.Clock()
        self.current_time = 0
        self.last_image_change_time = pygame.time.Clock()

        self.doorbell_event = None
        self.garage_event = None

        # Add the Blinds to the Smart House
        self.blinds_bedroom = Blinds(pygame.image.load("Assets/Smart_Devices/Bedroom_Blinds.png"))
        self.blinds_bathroom = Blinds(pygame.image.load("Assets/Smart_Devices/Bathroom_Blinds.png"))
        self.devices.append(self.blinds_bedroom.image)
        self.devices.append(self.blinds_bathroom.image)

        # Add the Ceiling Lights to the Smart House
        self.ceiling_lights_bedroom = Light(pygame.image.load("Assets/Smart_Devices/Bedroom_Ceiling_Lights.png"))
        self.nightstand_lamp_bedroom = Light(pygame.image.load("Assets/Smart_Devices/Bedroom_Light.png"))
        self.ceiling_lights_livingroom = Light(pygame.image.load("Assets/Smart_Devices/Livingroom_Ceiling_Lights.png"))
        self.floor_lamp_livingroom = Light(pygame.image.load("Assets/Smart_Devices/Livingroom_Lamp.png"))
        self.ceiling_lights_kitchen = Light(pygame.image.load("Assets/Smart_Devices/Kitchen_Ceiling_Lights.png"))
        self.lights_bathroom = Light(pygame.image.load("Assets/Smart_Devices/Bathroom_Lights.png"))

        # Add the Garage Door
        self.garage_door = Garage(pygame.image.load("Assets/Smart_Devices/Garage_Door.png"))
        self.devices.append(self.garage_door.image)

        # Add the entrance Door
        self.entrance_door = Door(pygame.image.load("Assets/Smart_Devices/Entry_Door.png"))

        # Add the TV
        self.television = TV(pygame.image.load("Assets/Smart_Devices/Garage_Door.png"))

        # Add the camera
        self.garage_camera = Camera(None)

        # Add the doorbell camera
        self.entrance_doorbell = Doorbell(None)

        # Add the fridge
        self.kitchen_fridge = Fridge(None)

        # Add the thermostat
        self.thermostat_bathroom = Thermostat(None)

        # Add array for notifications
        self.notifications = []

        self.automations_device = []
        self.automations_time = []
        self.automations_sensor = []

        self.devices_list = [self.entrance_door, self.television, self.ceiling_lights_livingroom,
                             self.floor_lamp_livingroom, self.ceiling_lights_kitchen, self.blinds_bedroom,
                             self.ceiling_lights_bedroom, self.nightstand_lamp_bedroom, self.blinds_bathroom,
                             self.lights_bathroom, self.garage_door]

        self.visible_Start = False
        self.visible_Automation = False

    def draw(self, screen):
        font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 35)
        text = font.render("Smart App [SPACE]", True, (0, 0, 0))
        screen.blit(text, (1550, 76))
        text = font.render("Quit [ESC]", True, (0, 0, 0))
        screen.blit(text, (1550, 130))
        for image in self.devices:
            screen.blit(image, (0, 0))

    def update_notification_array(self):
        self.notifications = [notif for notif in self.notifications if not notif.is_expired()]

    def draw_notifications(self, screen):
        # font = pygame.font.Font(pygame.font.match_font('Bahnschrift'), 50)
        
        font = pygame.font.Font(pygame.font.match_font('Segoe UI Emoji'), 40)
        y_position = 50
        background_color = (255, 255, 255)
        for notif in self.notifications:
            text_surface = font.render(notif.text, True, (0, 0, 0))

            text_rect = text_surface.get_rect()
            text_rect.topleft = (200, y_position)

            # Create a background rectangle
            background_rect = pygame.Rect(text_rect.left, text_rect.top, text_rect.width, text_rect.height)
            pygame.draw.rect(screen, background_color, background_rect)

            # Blit the background and text onto the screen
            screen.blit(text_surface, text_rect.topleft)

            # screen.blit(text_surface, (200, y_position))
            y_position += text_surface.get_height() + 5

    def day_and_night_cycle(self, screen):
        self.current_time = (self.current_time + self.clock.tick(
            60) / 1000) % total_cycle_duration  # Convert milliseconds to seconds

        # Determine the current background based on the in-game time
        if 0 <= self.current_time < morning_duration:
            self.night = False
            self.morning = True
            self.new_time_state = "Morning"
            current_background = morning_image
        elif morning_duration <= self.current_time < morning_duration + day_duration:
            self.morning = False
            self.day = True
            self.new_time_state = "Day"
            current_background = day_image
        elif morning_duration + day_duration <= self.current_time < morning_duration + day_duration + noon_duration:
            self.day = False
            self.noon = True
            self.new_time_state = "Noon"
            current_background = noon_image
        else:
            self.noon = False
            self.night = True
            self.new_time_state = "Night"
            current_background = night_image

        if self.new_time_state != self.current_time_state:
            self.automation_done = False
            self.current_time_state = self.new_time_state
            if self.current_time_state == "Morning":
                self.doorbell_event = random.choices(morning_event, weights=[8, 1])[0]
            elif self.current_time_state == "Day":
                self.doorbell_event = random.choices(day_event, weights=[8, 1, 3])[0]
            elif self.current_time_state == "Noon":
                self.doorbell_event = random.choices(noon_event, weights=[8, 2])[0]
            elif self.current_time_state == "Night":
                self.doorbell_event = random.choices(night_event, weights=[7, 1])[0]

            if self.doorbell_event == "Assets/Backgrounds/Camera_Day_Delivery.png" or self.doorbell_event == "Assets/Backgrounds/Camera_Sunset_Delivery.png":
                self.draw_garage_camera()
                pygame.mixer.music.load("Assets/Sounds/doorbell.mp3")
                pygame.mixer.music.play()
                self.notifications.append(Notification("[Ding-Dong!] Doorbell alert! Check who's at the door", 6000))
            elif self.doorbell_event == "Assets/Backgrounds/Camera_Morning_Cat.png" or self.doorbell_event == "Assets/Backgrounds/Camera_Day_Cat.png" or self.doorbell_event == "Assets/Backgrounds/Camera_Night_Thief.png":
                self.draw_garage_camera()
                pygame.mixer.music.load("Assets/Sounds/alert.mp3")
                pygame.mixer.music.play()
                self.notifications.append(
                    Notification("[!] Security Notification: Motion detected outside your door", 6000))
            else:
                self.garage_event = random.choices(garage_event_images, weights=[1, 8, 2])[0]
                if self.garage_event == "Assets/Backgrounds/Camera_Garage_Closed_Cat.png" or self.garage_event == "Assets/Backgrounds/Camera_Garage_Open_Cat.png" or self.garage_event == "Assets/Backgrounds/Camera_Garage_Closed_Thief.png" or self.garage_event == "Assets/Backgrounds/Camera_Garage_Open_Thief.png":
                    pygame.mixer.music.load("Assets/Sounds/alert.mp3")
                    pygame.mixer.music.play()
                    self.notifications.append(
                        Notification("[!] Security Notification: Motion detected outside your Garage", 6000))
        screen.blit(current_background, (0, 0))

    def draw_garage_camera(self):
        if self.garage_door.closed:
            self.garage_event = "Assets/Backgrounds/Camera_Garage_Closed.png"
        elif not self.garage_door.closed:
            self.garage_event = "Assets/Backgrounds/Camera_Garage_Open.png"
