import pygame
import sys

pygame.init()

# Set up display
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Pygame Example")

# Load image
morning = pygame.image.load("PinkMorning.png")
day = pygame.image.load("BlueDay.png")
noon = pygame.image.load("OrangeSunset.png")
night = pygame.image.load("MarineblueNight.png")

house = pygame.image.load("HomeTest1.png")
garage = pygame.image.load("GarageDoor.png")
phone = pygame.image.load("Phone.png")

resized_phone = pygame.transform.scale(phone, (532, 1001))

# Define time intervals (in seconds) for each background
morning_duration = 1
day_duration = 1
noon_duration = 1
night_duration = 1

total_cycle_duration = morning_duration + day_duration + noon_duration + night_duration

clock = pygame.time.Clock()
current_time = 0
# Normalize menu position
visible = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            visible = not visible

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

    # Draw image on the screen
    screen.blit(current_background, (0, 0))
    screen.blit(house, (0, 0))
    screen.blit(garage, (0, 0))

    #menu_content.set_alpha(200)  # Set transparency (adjust as needed)
    if visible:
        #screen.blit(menu_content, (0, 0))
        screen.blit(resized_phone, (1351, 42))


    # Update display
    pygame.display.flip()
    clock.tick(60)  # Adjust as needed
