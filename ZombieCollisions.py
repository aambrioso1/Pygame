"""
Program to work out collision and the Sprite class in Pygame.
"""
import pygame, sys
import random
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
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

# We load a play an mp3 file as background music.
pygame.mixer.music.load('C:\\Users\\aambrioso\\Pygame\\assets\\mp3\\DevilsPiano.mp3')
# pygame.mixer.music.play(-1,0.0) # play forever, -1, start at 0.0
musicPlaying = False # We will use this to turn the music on and off

gravestoneImg = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\gravestone.png')
rot = -10
rot_del = 0
gravestoneImg = pygame.transform.rotozoom(gravestoneImg, rot, 0.1)
# gravestoneImg = pygame.transform.rotozoom(gravestoneImg, rot, 0.1)   

class Zombie(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       screen = pygame.display.get_surface()    
       #image1 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\zombie_Alex.png')
       #zombie_image = pygame.transform.rotozoom(image1, 0, 0.001)
                                                
                                                
       image2 = pygame.image.load('C:\\Users\\aambrioso\\Pygame\\assets\\images\\zhombies\\\Mario_Alex2.png')
       human_image = pygame.transform.rotozoom(image2, 0, 0.2)
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
           self.image = pygame.transform.rotozoom(image1, 0, 0.05)
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

N = 1
COUNT = 20
characters = [Zombie() for i in range(COUNT)] 

not_its = pygame.sprite.Group()
its = pygame.sprite.Group()
not_its.add(characters)
# not_its.remove(characters[0])
it = characters[0]
it.change()
its.add(it)

HUMAN = True
       
while True: # The main game loop.  Moves the zombie.  Switches direction randomly if zombie hits the wall.  Draws everything.  Checks if the user has pressed the m key to turn the music on or off.
    fpsClock.tick(FPS)
    
    
       
       
    for event in pygame.event.get():
        # Does the player want to quit?
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
        # Turn the music on and off with the m key.
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
            if event.key == K_z:
                characters[N].change()
                humans.remove(characters[N])
                zombies.add(characters[N])
                N += 1
                if N == COUNT: N = 0

                
                    
    
    collision_dict = pygame.sprite.groupcollide(its, not_its, False, True)
    if collision_dict != {}:
        for it in collision_dict.keys():
            for new_it in collision_dict[it]:
                new_it.change()
                its.add(new_it)
                print('not_its', len(not_its), not_its)
                print('its', its)
    not_its.remove(its.sprites()[0])
    if len(not_its) == 0:
        temp1 = not_its
        temp2 = its
        its = temp1
        not_its = temp2
        print('reversed not_its', not_its)
        it = not_its.sprites()[0]
        not_its.remove(it)
        it.change()
        its.add(it)
        print('reversed its', its)
        print('All not_its are now its.')
                    
                    
                    
    
    # Draw stuff
    allsprites = pygame.sprite.RenderPlain(characters)
    allsprites.update()
    
    screen.blit(background, (0, 0))
    
    
    # Draw a bunch of gravestones.
    BUNCH = 15
    # rot += rot_del
    for i in range(BUNCH//2):
        screen.blit(gravestoneImg, (i*50, 50))
        screen.blit(gravestoneImg, (i*50, 150))
 
    

    allsprites.draw(screen)
    pygame.display.flip()             
    