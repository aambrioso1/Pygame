"""
A simple zhombie animation.   A character bounces off of walls randomly.   Some gravestones are drawn in the background.   Spookie music will play and stop playing if the user presses the m key.   if the player presses the t key the character turns into a zombie.

We use four assets: (1) a regular character image (2) a zhombie image, (3) A spooky music file, and (4) A gravestone image.  The code will need to be adjusted to retrieve the files from the appropriate directory for user’s installation.
"""

import pygame, sys
import random
from pygame.locals import *

pygame.init()

FPS = 100 # frames per second setting
fpsClock = pygame.time.Clock()

# Set up the animation window
DISPLAYSURF = pygame.display.set_mode((600, 500), 0, 32)
pygame.display.set_caption('Zhombie Animation')

# A few color options for the background.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Load the images we are using.
zhombie1Img = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\zhombie1.png')
zombie_Alex = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\zombie_Alex.png')
Mario_Alex2 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\\Mario_Alex2.png')
gravestoneImg = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\gravestone.png')

# Resize the images so they fit the window better.   The first integer in degrees will rotate the image the second resizes the image by that factor.
zhombie1Img = pygame.transform.rotozoom(zhombie1Img, 0, 0.1)
zombie_Alex = pygame.transform.rotozoom(zombie_Alex, 0, 0.1)
Mario_Alex2 = pygame.transform.rotozoom(Mario_Alex2, 0, 0.5)
gravestoneImg = pygame.transform.rotozoom(gravestoneImg, 0, 0.1)

ZOMBIE = False # Decide whether to draw zombie or not.

# Starting zhombie postion.
z1_x = 10
z1_y = 10

# Initial speed of zombie.
X_SPEED = 4
Y_SPEED = 4


# We load a play an mp3 file as background music.
pygame.mixer.music.load('C:\\Users\\aambrioso\\Pygame\\assets\\mp3\\DevilsPiano.mp3')
# pygame.mixer.music.play(-1,0.0) # play forever, -1, start at 0.0
musicPlaying = False # We will use this to turn the music on and off


while True: # The main game loop.  Moves the zombie.  Switches direction randomly if zombie hits the wall.  Draws everything.  Check if we have press the m key to turn the music on or off.
    DISPLAYSURF.fill(BLACK)
    z1_x += X_SPEED
    z1_y += Y_SPEED
    if z1_x >= 560:
       X_SPEED = random.randint(-4,-2)
       z1_x += X_SPEED
       z1_y += Y_SPEED
    elif z1_y >= 460:
        Y_SPEED = random.randint(-4,-2)
        z1_x += X_SPEED
        z1_y += Y_SPEED
    elif z1_x <= 5:
        X_SPEED = random.randint(2,4)
        z1_x += X_SPEED
        z1_y += Y_SPEED
    elif z1_y <= 5:
        Y_SPEED = random.randint(2,4)
        z1_x += X_SPEED
        z1_y += Y_SPEED
    
    # Draw a bunch of gravestones.
    BUNCH = 15
    for i in range(BUNCH//2):
        DISPLAYSURF.blit(gravestoneImg, (i*50, 50))
        DISPLAYSURF.blit(gravestoneImg, (i*50, 150))
    
    # Draw zombie in a new position.
    # DISPLAYSURF.blit(zhombie1Img, (z1_x, z1_y))
    if ZOMBIE:
        DISPLAYSURF.blit(zombie_Alex, (z1_x, z1_y))
    else: DISPLAYSURF.blit(Mario_Alex2, (z1_x, z1_y))
 
    for event in pygame.event.get():
        # Does the player want to quit?
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                   
        # Check if player pushed a key on the keyboard.
        if event.type == KEYUP:
            # Turn the music on and off with the m key.
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
            if event.key == K_t:
                ZOMBIE = not ZOMBIE
    
    pygame.display.update()
    fpsClock.tick(FPS)
