import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screen_width = 640
screen_height = 480

x = screen_width / 2
y = screen_height / 2

x2 = randint(3, 610)
y2 = randint(3, 440)

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

    if pygame.key.get_pressed()[K_UP]:  # This code solves the problem above keeping thw key pressed do:
        y -= 10
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 10
    if pygame.key.get_pressed()[K_DOWN]:
        y += 10
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 10

    ret_red = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))
    ret_blue = pygame.draw.rect(screen, (0, 0, 255), (x2, y2, 40, 50))

    if ret_red.colliderect(ret_blue):
        x2 = randint(3, 610)
        y2 = randint(3, 440)

    pygame.display.flip()
