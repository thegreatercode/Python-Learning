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

    #  screen.fill((255, 255, 255)) - #  Remove the first '#' for to chose the background color

    # pygame.draw.rect(SCREEN, (R, G, B), (X, Y, WIDTH, HEIGHT))
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 40, 40))
    pygame.draw.rect(screen, (0, 0, 255), (600, 0, 40, 40))
    pygame.draw.rect(screen, (255, 255, 255), (0, 440, 40, 40))
    pygame.draw.rect(screen, (0, 255, 0), (600, 440, 40, 40))
    # pygame.draw.line(SCREEN, (R, G, B), (START POINT), (DESTINY POINT),THICKNESS)
    pygame.draw.line(screen, (255, 0, 0), (40, 40), (600, 40), 1)
    pygame.draw.line(screen, (0, 0, 255), (40, 40), (40, 440), 1)
    pygame.draw.line(screen, (255, 255, 255), (40, 440), (600, 440), 1)
    pygame.draw.line(screen, (0, 255, 0), (600, 440), (600, 40), 1)
    pygame.draw.line(screen, (0, 255, 0), (40, 440), (600, 40), 1)
    pygame.draw.line(screen, (0, 255, 0), (40, 40), (600, 440), 1)
    # pygame.draw.circle(SCREEN, (R, G, B), (X, Y), RADIUS)
    pygame.draw.circle(screen, (0, 0, 255), (320, 240), 30)  # (SCREEN, (R, G, B), (X, Y), RADIUS)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
