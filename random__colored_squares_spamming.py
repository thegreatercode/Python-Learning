import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen_width = 640
screen_height = 480

x = 0
y = 0

r = 0
g = 0
b = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Small Ball Game')

fps = pygame.time.Clock()  # Controls the FPS of the game with the fps.tick()

while True:
    fps.tick(3)
    screen.fill((0, 0, 0))  # This is used to make the screen turns black while the movements
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

    pygame.draw.rect(screen, (r, g, b), (x, y, 40, 40))
    x = random.randint(3, 610)
    y = random.randint(3, 440)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
