import pygame
from support import import_csv_layout
from config import *
from support import *
from debug import debug
from background import Tile
from ui import UI


class Level:
    """Create the entire level layout of the game."""
    
    def __init__(self, folder, player):
        # General setup
        self.display_surface = pygame.display.get_surface()

        self.csv_layouts, self.bg_image_path = import_folder(folder)

        # Sprite group setup
        self.visible_sprites = YCordSortCameraGroup(self.bg_image_path)
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.player = player
        self.create_map()

        # UI - User Interface
        self.ui = UI()
    
    def create_map(self):
        """Generating the map of the level that is loaded."""
        # Spritesheets
        self.inside_b = Spritesheet("./Graphics/Tilesets/Redo_Inside_B.png")
        self.inside_c = Spritesheet("./Graphics/Tilesets/Redo_Inside_C.png")

        # For each CSV File there is a map
        for type, map in self.csv_layouts.items():
            for row_index, row in enumerate(map):
                for col_index, col in enumerate(row):
                    # -1 in CSV means no tile
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        # Collision / Invisible tile to set map boundaries
                        if type == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], "invisible", infl_x=-16)
                        if type == 'inside_b':
                            surf = self.inside_b.spritesheet_number(int(col), 16)
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], "tile", surf, -48, -48)
                        if type == 'inside_c':
                            surf = self.inside_c.spritesheet_number(int(col), 16)
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], "tile", surf, -32, -62)
        
        self.player.spawn_player((23*TILESIZE, 18*TILESIZE), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        """Updating and drawing the game onto the screen."""
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.run(self.player)


class YCordSortCameraGroup(pygame.sprite.Group):
    def __init__(self, bg_path):
        # General setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # Creating the background visual
        self.background_surface = pygame.image.load(bg_path).convert()
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