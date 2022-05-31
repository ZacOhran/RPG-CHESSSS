import pygame
from config import *
from csv import reader
from os import walk

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()

    def get_image(self, row, column, width, height):
        """Selecting individual image from image sheet."""
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), ((column * width), (row * height), width, height))
        
        return image

def import_csv_layout(path):
    """Import a csv file, separate the file to understand the parts of the map."""
    map = []

    with open(path) as level:
        layout = reader(level, delimiter=",")
        
        for row in layout:
            map.append(list(row))

        return map

def import_folder(path):
    """Import a folder with all of its assets in a list."""
    surfaces = []
    
    for main_dir, sub_dir, files in walk(path):
        for image in files:
            full_path = f"{path}/{image}"
            image_surf = pygame.image.load(full_path).convert_alpha()
            surfaces.append(image_surf)

    return surfaces
