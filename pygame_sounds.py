"""
A demonstration of how to generate a sound using Pygame library.  It does the following:
    
(1) It opens an empty window.
(2) It plays spooky background music.   
(3) The player can turn the music on and off by pushing the m key.   
(4) The player can play a punch sound by pushing the p key.

My goal is to create a simple zhombie tag game with a game mode and an autonomous mode.

You can find directions for install the Pygame library here:
    https://www.pygame.org/wiki/GettingStarted

You will need two sound files for this program.   I put two files you can use in my Pygame repository:
Look for BatmanPunch.wav and DevilsPiano.mp3.

I found the following website helpful: http://inventwithpython.com/invent4thed/chapter20.html
My thanks to Al Sweigart for making his books available online.   
"""

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
            # Check if player push a key on the keyboard.
            if event.type == KEYUP:
                # Turn the music on and off with the m key
                if event.key == K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = not musicPlaying
                # Stop the music and play a punch sound with the p key.
                if event.key == K_p:
                    pygame.mixer.music.stop()
                    soundObj.play()
                    import time
                    time.sleep(1) # wait a for 1 second while sound plays.
                    soundObj.stop()
                    # Start the background music again.
                    pygame.mixer.music.play(-1, 0.0)
                    


