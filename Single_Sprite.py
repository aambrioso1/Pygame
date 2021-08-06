<<<<<<< HEAD
"""
Program that demonstrates the sprite class in Pygame.
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


# Create The Backgound
background = pygame.Surface(screen.get_size())
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert
background = background.convert()
background.fill(BLACK)


class Character(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       screen = pygame.display.get_surface()    
                    
       image = pygame.image.load('C:\\Users\\Alex\\Pygame\\assets\\images\\girl_character.png')
       char_image = pygame.transform.rotozoom(image, 0, 0.2)
       #Mario_Alex2 = pygame.transform.rotozoom(Mario_Alex2, 0, 0.5)
       # Fetch the rectangle object that has the dimensions of the image
       self.image = char_image
       self.rect = char_image.get_rect()
       self.HUMAN = True
       self.area = screen.get_rect()
       start_x = 0
       start_y = 0
       self.rect.topleft = start_x, start_y
       self.X = 0
       self.Y = 0
       self.SPEED = 2

    def update(self):
        newpos = self.rect.move((self.X, self.Y))
        self.rect = newpos
        print(f'new position = {newpos}')
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        print(f'x = {x} and y = {y}')
        dy = y - self.rect.y
        dx = x - self.rect.x
        r = math.sqrt(dx**2 + dy**2) + 0.00001
        cos = dx/r
        sin = dy/r
        self.X = self.SPEED*cos
        self.Y = self.SPEED*sin

"""  
Code to define a new method for the character
    def change(self):
       if self.HUMAN:
           self.original = self.image
           image1 = pygame.image.load('C:\\Users\\Alex\\Pygame\\assets\\images\\zhombies\\zombie_Alex.png')
           self.image = pygame.transform.rotozoom(image1, 0, 0.1)
           self.HUMAN = not self.HUMAN
       else:
           self.image = self.original
           self.HUMAN = not self.HUMAN
       # self.image2 = Mario_Alex2 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\\Mario_Alex2.png')
        # Update the position of this object by setting the values of rect.x and rect.y
"""    
    
# Create a instance of the class character
C = Character()

# Game lop=op       
while True: # The main game loop.  Moves the zombie.  Switches direction randomly if zombie hits the wall.  Draws everything.  Checks if the user has pressed the m key to turn the music on or off.
    fpsClock.tick(FPS)
    
    allsprites = pygame.sprite.RenderPlain(C)
         
   
    for event in pygame.event.get(): 
        # Does the player want to quit?
        if event.type == QUIT: # Check if windows x has been clicked
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN: #checks if mouse button has been pressed
        # Do something. 
            pass
                      
    C.update()
   
    # Draw stuff
    
    # The blit method draws one image onto another.
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(background, (0, 0))
    
    allsprites.draw(screen)
    
    # Updates the contents of the display
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()             
    
=======
"""
Program that demonstrates the sprite class in Pygame.
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


# Create The Backgound
background = pygame.Surface(screen.get_size())
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert
background = background.convert()
background.fill(BLACK)


class Character(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       screen = pygame.display.get_surface()    
                    
       image = pygame.image.load('C:\\Users\\Alex\\Pygame\\assets\\images\\girl_character.png')
       char_image = pygame.transform.rotozoom(image, 0, 0.2)
       #Mario_Alex2 = pygame.transform.rotozoom(Mario_Alex2, 0, 0.5)
       # Fetch the rectangle object that has the dimensions of the image
       self.image = char_image
       self.rect = char_image.get_rect()
       self.HUMAN = True
       self.area = screen.get_rect()
       start_x = 0
       start_y = 0
       self.rect.topleft = start_x, start_y
       self.X = 0
       self.Y = 0
       self.SPEED = 2

    def update(self):
        newpos = self.rect.move((self.X, self.Y))
        self.rect = newpos
        print(f'new position = {newpos}')
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        print(f'x = {x} and y = {y}')
        dy = y - self.rect.y
        dx = x - self.rect.x
        r = math.sqrt(dx**2 + dy**2) + 0.00001
        cos = dx/r
        sin = dy/r
        self.X = self.SPEED*cos
        self.Y = self.SPEED*sin

"""  
Code to define a new method for the character
    def change(self):
       if self.HUMAN:
           self.original = self.image
           image1 = pygame.image.load('C:\\Users\\Alex\\Pygame\\assets\\images\\zhombies\\zombie_Alex.png')
           self.image = pygame.transform.rotozoom(image1, 0, 0.1)
           self.HUMAN = not self.HUMAN
       else:
           self.image = self.original
           self.HUMAN = not self.HUMAN
       # self.image2 = Mario_Alex2 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\\Mario_Alex2.png')
        # Update the position of this object by setting the values of rect.x and rect.y
"""    
    
# Create a instance of the class character
C = Character()

# Game lop=op       
while True: # The main game loop.  Moves the zombie.  Switches direction randomly if zombie hits the wall.  Draws everything.  Checks if the user has pressed the m key to turn the music on or off.
    fpsClock.tick(FPS)
    
    allsprites = pygame.sprite.RenderPlain(C)
         
   
    for event in pygame.event.get(): 
        # Does the player want to quit?
        if event.type == QUIT: # Check if windows x has been clicked
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN: #checks if mouse button has been pressed
        # Do something. 
            pass
                      
    C.update()
   
    # Draw stuff
    
    # The blit method draws one image onto another.
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(background, (0, 0))
    
    allsprites.draw(screen)
    
    # Updates the contents of the display
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()             
    
>>>>>>> update mouse_chase.py
