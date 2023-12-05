import pygame
import sys

from smart_app import SmartApp
from smart_home import SmartHome

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

# Set up display
#screen = pygame.display.set_mode((1920, 1080))
#pygame.display.set_caption("Smart Home Simulation")

# Create the smart home and the smart home application
smart_home = SmartHome()
smart_app = SmartApp(smart_home)

# Screen Display
screen_width, screen_height = 1920, 1080
fullscreen = False
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)  # Make the window resizable
pygame.display.set_caption("Smart Home Simulation")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)  # Update the screen size
            screen_width, screen_height = event.w, event.h
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            # Toggle fullscreen on 'f' key press
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

        smart_app.handle_event(event)

    screen.fill((0, 0, 0))

    # Draw images on the screen
    smart_home.day_and_night_cycle(screen)
    smart_home.draw(screen)

    # menu_content.set_alpha(200)  # Set transparency (adjust as needed)
    smart_app.draw(screen)
    smart_home.update_notification_array()
    smart_home.draw_notifications(screen)

    # Update display
    pygame.display.flip()
    smart_home.clock.tick(60)  # Adjust as needed
