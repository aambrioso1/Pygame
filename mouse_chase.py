# mouse_chase.py

import pygame, sys, random
from pygame.locals import *

import math

# set up pygame

pygame.init()
mainClock = pygame.time.Clock()
# Set up the window.
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
                                       0, 32)
pygame.display.set_caption('Mouse Chase')

# set up the colors for the background and the ball
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SPEED = 4 # controls how quickly ball moves
c_x = 250 # current x value for the ball initially 250
c_y = 250 # current y value for the ball initially 250

# run the game loop forever
while True:
    # check for a quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # colors the background of the surface
    windowSurface.fill(WHITE)

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    # updates the position of the ball by moving it slightly toward the mouse
    dy = y - c_y
    dx = x - c_x
    r = math.sqrt(dx**2 + dy**2)+0.0001
    cos = dx/r
    sin = dy/r
    x_speed = int(SPEED*cos)
    y_speed = int(SPEED*sin)
    c_x += x_speed
    c_y += y_speed

    # redraws the ball and updates the window
    pygame.draw.circle(windowSurface, RED, (c_x, c_y), 20)
    pygame.display.update()


    mainClock.tick(100)