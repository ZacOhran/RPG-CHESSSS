import pygame
from config import *

class Tile(pygame.sprite.Sprite):
    """Create every interactive background tile in the game."""
    
    def __init__(self, pos, groups):
        # Creating the obstacle sprite
        super().__init__(groups)
        self.image = pygame.image.load('./Graphics/Images/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0)