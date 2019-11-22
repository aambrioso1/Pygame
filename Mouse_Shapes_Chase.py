"""
pygame -  A module of methods for writing games in Python
sys - part of the Python standard library.  A library which allows the programmer access variables and functions used by the interpreter
pygame.locals - a module containing variables used by Pygame.
random - a module containing methods for generating random numbers.   Note the structure from <module> import *.  The allows the programmer to use the function without having to prefix the module name.
"""
import pygame, sys, random
# from pygame.locals import *
import random
import math

# Set up pygame

pygame.init()
mainClock = pygame.time.Clock()
# Set up the window.
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
                                        0, 32)
pygame.display.set_caption('Shape Chase')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
FUSHIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)


# Creates a array of all the pixels on the surface
pixAr = pygame.PixelArray(windowSurface)

#Colors the background of the surface
windowSurface.fill(WHITE)

pygame.draw.line(windowSurface, BLUE, (100,300), (300,450),3)
pygame.draw.rect(windowSurface, OLIVE, (300, 100, 50, 50))
pygame.draw.circle(windowSurface, RED, (250,250), 50)
pixAr[400][400] = FUSHIA
pygame.draw.polygon(windowSurface, PURPLE, ((50,100),(100,50),(150,100),(150,200),(50,200)))


SPEED = 4
c_x = 250
c_y = 250

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        # Does the player want to quit.
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
                    
    """
    # Colors the background of the surface
    windowSurface.fill(WHITE)
    
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    
    dy = y - c_y
    dx = x - c_x
    r = math.sqrt(dx**2 + dy**2)+0.0001
    cos = dx/r
    sin = dy/r
    x_speed = int(SPEED*cos)
    y_speed = int(SPEED*sin)
    c_x += x_speed
    c_y += y_speed
            
    pygame.draw.circle(windowSurface, RED, (c_x, c_y), 20)
    # pygame.draw.rect(windowSurface, OLIVE, (c_x, c_y, 50, 50))
    """
    pygame.display.update()
    mainClock.tick(10)
