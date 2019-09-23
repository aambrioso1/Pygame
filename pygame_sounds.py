# A demonstration of how to generate a sound using Pygame library.  I found the following website helpful: http://inventwithpython.com/invent4thed/chapter20.html

import pygame, sys
from pygame.locals import *

pygame.init()

# Open a window.
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
       0, 32)
pygame.display.set_caption('Halloween Background Music')


# Loading and playing a sound effect:
soundObj = pygame.mixer.Sound('C:\\Users\\aambrioso\\Pygame\\assets\\wav\\BatmanPunch.wav')
"""
soundObj.play()
import time
time.sleep(1) # wait and let the sound play for 1 seconds
soundObj.stop()
"""

# We load a play an mp3 file as background music.
pygame.mixer.music.load('C:\\Users\\aambrioso\\Pygame\\assets\\mp3\\DevilsPiano.mp3')
pygame.mixer.music.play(-1,0.0) # play forever, -1, start at 0.0
musicPlaying = True # We will use this to turn the music on and off

# The program waits for two events.  Quit by clicking on the exit x in the upper right of the window and type an m to stop and start the music.
while True:
    # Check for events.
    for event in pygame.event.get():
            # Does the player want to quit?
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            # Turn the music on and off
            if event.type == KEYUP:
                if event.key == K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = not musicPlaying
                if event.key == K_p:
                    pygame.mixer.music.stop()
                    soundObj.play()
                    import time
                    time.sleep(1) # wait a for 1 second while sound plays
                    soundObj.stop()
                    pygame.mixer.music.play(-1, 0.0)
                    


