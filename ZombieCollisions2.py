"""
Program to work out collision and the Sprite class in Pygame.
"""
import pygame, sys
import random
from pygame.locals import *

pygame.init()

FPS = 100 # frames per second setting
fpsClock = pygame.time.Clock()

# Set up the animation window
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Zombie Animation')

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
       start_x = random.randint(0, 800)
       start_y = random.randint(0, 600)
       self.rect.topleft = start_x, start_y
       self.X = 4
       self.Y = 4
       
       
    
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
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left:
                self.X = random.randint(3,6)
                newpos = self.rect.move((self.X, self.Y))
                
            if self.rect.right > self.area.right:
                self.X = random.randint(-6,-3)
                newpos = self.rect.move((self.X, self.Y))
            
            if self.rect.bottom > self.area.bottom:
                self.Y = random.randint(-5, -3)
                newpos = self.rect.move((self.X, self.Y))
                
            if self.rect.top < self.area.top:
                self.Y = random.randint(3, 6)
                newpos = self.rect.move((self.X, self.Y))
                
        self.rect = newpos

COUNT = 10
characters = [Zombie() for i in range(COUNT)] 

characterGroup = pygame.sprite.Group()
characterGroup.add(characters)

print(characters[0].rect)

HUMAN = True
       
while True: # The main game loop.  Moves the zombie.  Switches direction randomly if zombie hits the wall.  Draws everything.  Checks if the user has pressed the m key to turn the music on or off.
    fpsClock.tick(FPS)
    
    allsprites = pygame.sprite.RenderPlain(characters)
       
   
    
    for event in pygame.event.get():
        # Does the player want to quit?
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
        # Turn the music on and off with the m key.
           if event.key == K_t:
                characters[0].change()
        
                
                    
    allsprites.update()
    #print(pygame.sprite.groupcollide(characterGroup,characterGroup, False, False))
    # Draw stuff
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()             
    