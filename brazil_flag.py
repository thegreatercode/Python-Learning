import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen_width = 640
screen_height = 480

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Small Ball Game')

# Run until the user asks to quit
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

    # Fill the background with white
    screen.fill((0, 156, 59))

    # pygame.draw.polygon((surface, color, points, width)   width is optional
    pygame.draw.polygon(screen, (255, 223, 0), [(320, 60), (580, 240), (320, 420), (60, 240)])

    # pygame.draw.circle(SCREEN, (R, G, B), (X, Y), RADIUS)
    pygame.draw.circle(screen, (0, 39, 118), (320, 240), 120)  # (SCREEN, (R, G, B), (X, Y), RADIUS)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
