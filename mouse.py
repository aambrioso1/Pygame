import pygame, sys
from pygame.locals import *

"""
Prints out mouse event numbers when cursor is in the display window:
    
1 = left click
2 = right and left click simultaneously or scroll push
3 = right click
4 = scroll up
5 = scroll down
"""

pygame.init()
pygame.display.set_mode((600,300))
pygame.display.set_caption('Mouse Input Demonstration')

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT: # Checks for QUIT event (click on x in window).
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE: # Check if user presses ESC.
            running = False
        if event.type == MOUSEBUTTONDOWN:  # Check if user pushes mouse down.
            print('Button down event:', event.button)
        if event.type == MOUSEBUTTONUP:  # Check if user releases the mouse.
            print('Button up event:', event.button)
        if event.type == MOUSEMOTION:
            print('Mouse motion event:', pygame.mouse.get_pos())

pygame.display.quit()