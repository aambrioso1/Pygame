"""
Creates a group of tiles for a image file for a map for a game backdrop (png).
Once the group of tiles is create they can be rearrange to create different maps.
"""

import pygame
import pygame.locals
import random as rd

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width//width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height//height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

"""
new_table = [[[] for j in range(4)] for i in range(4)]
print(new_table)
"""    

tile_file = "C:\\Users\\Alex\\OneDrive - Hillsborough Community College\\Programming\\Pygame\\assets\\planets.png"

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    screen.fill((255, 255, 255))
    table = load_tile_table(tile_file, 250, 112)
    
    tile_list = [tile for row in table for tile in row]
    map_array = ['abab'*4 for i in range(4)]
    print(map_array)
    tile_dict = dict(zip('abcdefghijklmnop',tile_list))
    print(tile_list)
    
    for i in range(4):
        for j in range(4):
            table[i][j] = tile_dict[map_array[i][j]]
    
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            x_factor, y_factor = (255, 130) 
            screen.blit(tile, (x*x_factor, y*y_factor)) # Good values (110, 55)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass