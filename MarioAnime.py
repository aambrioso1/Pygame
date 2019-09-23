import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 500), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
MarioImg = pygame.image.load('SmallerMario.png')
Mariox = 10
Marioy = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        Mariox += 5
        if Mariox == 560:
            direction = 'down'
    elif direction == 'down':
        Marioy += 5
        if Marioy == 460:
            direction = 'left'
    elif direction == 'left':
        Mariox -= 5
        if Mariox == 10:
            direction = 'up'
    elif direction == 'up':
        Marioy -= 5
        if Marioy == 10:
            direction = 'right'

    DISPLAYSURF.blit(MarioImg, (Mariox, Marioy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)