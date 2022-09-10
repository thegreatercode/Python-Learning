import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen_width = 640
screen_height = 480

x = screen_width / 2
y = screen_height / 2



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
    '''
        if event.type == KEYDOWN:      it is commented because that code just works for move the rec once
            if event.key == K_UP:
                y -= 20
            if event.key == K_RIGHT:  
                x += 20
            if event.key == K_DOWN:
                y += 20
            if event.key == K_LEFT:
                x -= 20'''

    if pygame.key.get_pressed()[K_UP]:  # This code solves the problem above keeping thw key pressed do:
        y -= 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 20
    if pygame.key.get_pressed()[K_DOWN]:
        y += 20
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 20

    pygame.draw.rect(screen, (0, 0, 255), (x, y, 40, 40))
    pygame.display.flip()
