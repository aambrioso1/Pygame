"""
Program to demonstrate event handling in with the Pygame module.
"""
import pygame, sys
import random
import math
from pygame.locals import *

pygame.init()

FPS = 200 # frames per second setting
fpsClock = pygame.time.Clock()

# Set up the animation window
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Mouse Event Test')

# A few color options for the background.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)


# Create The Backgound
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)
"""
# We load a play an mp3 file as background music.
pygame.mixer.music.load('C:\\Users\\aambrioso\\Pygame\\assets\\mp3\\DevilsPiano.mp3')
# pygame.mixer.music.play(-1,0.0) # play forever, -1, start at 0.0
musicPlaying = False # We will use this to turn the music on and off
"""



class Zombie(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       screen = pygame.display.get_surface()    
       
       image1 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\zombie_Alex.png')
       zombie_image = pygame.transform.rotozoom(image1, 0, 0.1)
       
       image2 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\\Mario_Alex2.png')
       human_image = pygame.transform.rotozoom(image2, 0, 0.4)
       #Mario_Alex2 = pygame.transform.rotozoom(Mario_Alex2, 0, 0.5)
       # Fetch the rectangle object that has the dimensions of the image
       self.image = human_image
       self.rect = human_image.get_rect()
       self.HUMAN = True
       self.area = screen.get_rect()
       start_x = 0
       start_y = 0
       self.rect.topleft = start_x, start_y
       self.X = 0
       self.Y = 0
       self.SPEED = 2
       
    
    def change(self):
       if self.HUMAN:
           self.original = self.image
           image1 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\zombie_Alex.png')
           self.image = pygame.transform.rotozoom(image1, 0, 0.1)
           self.HUMAN = not self.HUMAN
       else:
           self.image = self.original
           self.HUMAN = not self.HUMAN
       # self.image2 = Mario_Alex2 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\\Mario_Alex2.png')
        # Update the position of this object by setting the values of rect.x and rect.y
    
    
    def update(self):
        newpos = self.rect.move((self.X, self.Y))
        self.rect = newpos
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        dy = y - Z.rect.y
        dx = x - Z.rect.x
        r = math.sqrt(dx**2 + dy**2) + 0.0001
        cos = dx/r
        sin = dy/r
        Z.X = Z.SPEED*cos
        Z.Y = Z.SPEED*sin


Z = Zombie()


HUMAN = True
       
while True: # The main game loop.  Moves the zombie.  Switches direction randomly if zombie hits the wall.  Draws everything.  Checks if the user has pressed the m key to turn the music on or off.
    fpsClock.tick(FPS)
    
    allsprites = pygame.sprite.RenderPlain(Z)
       
   
    """
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    dy = y - Z.rect.y
    dx = x - Z.rect.x
    r = math.sqrt(dx**2 + dy**2)+.001
    cos = dx/r
    sin = dy/r
    Z.X = Z.SPEED*cos
    Z.Y = Z.SPEED*sin
    """
    for event in pygame.event.get(): 
        # Does the player want to quit?
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
        # Change character.
            Z.change()
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            dy = y - Z.rect.y
            dx = x - Z.rect.x
            r = math.sqrt(dx**2 + dy**2)
            cos = dx/r
            sin = dy/r
            
            Z.X = Z.SPEED*cos
            Z.Y = Z.SPEED*sin
            print('(Z.rect.x,Z.rect.y)',(Z.rect.x, Z.rect.y))
            print('(x,y)',(x, y))
            print('(Z.X,Z.Y)',(Z.X, Z.Y))
         """ 
              
    Z.update()
   
    # Draw stuff
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()             
    
