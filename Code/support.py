import pygame
from csv import reader
from os import walk

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
            image_surf = pygame.image.Load(full_path).convert_alpha()
            surfaces.append(image_surf)

    return surfaces
