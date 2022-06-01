import pygame
from config import *

class Tile(pygame.sprite.Sprite):
    """Create every interactive background tile in the game."""
    
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE)), infl_x=0, infl_y=0):
        # Creating the obstacle sprite
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        
        # Object is for graphics larger than one tile
        if self.sprite_type == "object":
            self.rect = self.image.get_rect(topleft = [pos[0], pos[1] - TILESIZE])
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(infl_x, infl_y)