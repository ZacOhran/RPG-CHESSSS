import pygame
from config import *
from debug import debug
from player import Player
from background import Tile


class Level:
    def __init__(self):
        # General setup
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = YCordSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()
    
    def create_map(self):
        """Generating the map of the level that is loaded."""
        # Row Index is the number of the row, row is whats inside the row
        for row_index, row in enumerate(WORLD_MAP):
            # Column index is the number of the column, column is whats inside
            for col_index, col in enumerate(row):
                # Creating the tiles for the map
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                # Every x in world map is an obstacle
                if col == 'x':
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
                # Every p is the player
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        """Updating and drawing the game onto the screen."""
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YCordSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # General setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
    
    def custom_draw(self, player):
        """Drawing all sprites in this class onto the display."""
        # Getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Drawing sprites onto screen using offset
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)