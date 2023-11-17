import pygame
import sys

from Code.smart_app import SmartApp

pygame.init()

# Set up display
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Smart Home Simulation")

# Load background images
morning = pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Backgrounds/PinkMorning.png")
day = pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Backgrounds/BlueDay.png")
noon = pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Backgrounds/OrangeSunset.png")
night = pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Backgrounds/MarineblueNight.png")

# Load Assets
house = pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/HomeTest1.png")
garage = pygame.image.load("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Smart_Devices/GarageDoor.png")

smart_app = SmartApp("C:/Uni Basel/Mdl. Applications and Related Topics/Cybernetics/Cybernetic/Assets/Phone.png")

# Define time intervals (in seconds) for each background
morning_duration = 1
day_duration = 1
noon_duration = 1
night_duration = 1

total_cycle_duration = morning_duration + day_duration + noon_duration + night_duration

# Clock
clock = pygame.time.Clock()
current_time = 0

# Visibility of the smart home app
visible = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        smart_app.handle_event(event)

    current_time = (current_time + clock.tick(60) / 1000) % total_cycle_duration  # Convert milliseconds to seconds

    # Determine the current background based on the in-game time
    if 0 <= current_time < morning_duration:
        current_background = morning
    elif morning_duration <= current_time < morning_duration + day_duration:
        current_background = day
    elif morning_duration + day_duration <= current_time < morning_duration + day_duration + noon_duration:
        current_background = noon
    else:
        current_background = night

    screen.fill((0, 0, 0))

    # Draw images on the screen
    screen.blit(current_background, (0, 0))
    screen.blit(house, (0, 0))
    screen.blit(garage, (0, 0))

    # menu_content.set_alpha(200)  # Set transparency (adjust as needed)
    smart_app.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Adjust as needed
