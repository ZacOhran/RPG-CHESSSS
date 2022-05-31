import pygame
from support import import_csv_layout
from config import *
from support import *
from debug import debug
from player import Player
from background import Tile


class Level:
    """Create the entire level layout of the game."""
    
    def __init__(self):
        # General setup
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = YCordSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()
    
    def create_map(self):
        """Generating the map of the level that is loaded."""
        # After Tiled map creation
        map_layouts = {
            "boundary": import_csv_layout("./Graphics/map/map_FloorBlocks.csv"),
            "grass": import_csv_layout("./Graphics/map/map_Grass.csv"),
            "object": import_csv_layout("./Graphics/map/map_Objects.csv")
        }
        
        graphics = {
            'grass': import_folder("./Graphics/Images")
        }
        
        for type, map in map_layouts.items():
            for row_index, row in enumerate(map):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
        
                        if type == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], "invisible")
        
        self.player = Player((31*TILESIZE, 22*TILESIZE), [self.visible_sprites], self.obstacle_sprites)

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

        # Creating the background visual
        self.background_surface = pygame.image.load("./Graphics/tilemap/ground.png").convert()
        self.background_rect = self.background_surface.get_rect(topleft=(0,0))
    
    def custom_draw(self, player):
        """Drawing all sprites in this class onto the display."""
        # Getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Background offset
        background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.background_surface, background_offset)

        # Drawing sprites onto screen using offset
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)