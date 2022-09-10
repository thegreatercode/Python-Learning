import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen_width = 640
screen_height = 480

x = 0
y = 0



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Small Ball Game')

fps = pygame.time.Clock()  # Controls the FPS of the game with the fps.tick()

while True:
    fps.tick(50)
    screen.fill((0, 0, 0))  # This is used to make the screen turns black while the movements
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

    pygame.draw.rect(screen, (0, 0, 255), (x, y, 40, 40))
    y += 1

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
