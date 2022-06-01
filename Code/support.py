import pygame
from config import *
from csv import reader

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()

    def get_image(self, row, column, width, height):
        """Selecting individual image from image sheet."""
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), ((column * width), (row * height), width, height))
        
        return image

    def spritesheet_column(self, column, amount_of_assets):
        column_assets = []
        for i in range(amount_of_assets):
            column_assets.append(self.get_image(i, column, TILESIZE, TILESIZE))
            
        return column_assets
    
    def spritesheet_number(self, number, tile_set_width):
        row = 0
        while number > (tile_set_width-1):
            row += 1
            number -= tile_set_width
        
        return self.get_image(row, number, TILESIZE, TILESIZE)

def import_csv_layout(path):
    """Import a csv file, separate the file to understand the parts of the map."""
    map = []

    with open(path) as level:
        layout = reader(level, delimiter=",")
        
        for row in layout:
            map.append(list(row))

        return map
