import pygame
from config import *
from support import *

class Player(pygame.sprite.Sprite):
    """Create the player object, everyway the player interacts with the environment here."""
    
    def __init__(self, pos, groups, obstacle_sprites):
        # Creating the player sprite
        super().__init__(groups)
        
        #Player graphics setup
        self.player_spritesheet = Spritesheet("./Graphics/Images/connor.png")
        self.player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = 0.15

        # Player object setup
        self.image = self.player_spritesheet.get_image(0, 0, TILESIZE, TILESIZE)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0)

        # Movement setup
        self.direction = pygame.math.Vector2()
        self.speed = 4

        # Action Values
        self.interact = False

        # Collision setup
        self.obstacle_sprites = obstacle_sprites
    
    def player_assets(self):
        self.animations = {
        "up_idle": [self.player_spritesheet.get_image(0, 1, TILESIZE, TILESIZE)],
        "down_idle": [self.player_spritesheet.get_image(0, 0, TILESIZE, TILESIZE)],
        "left_idle": [self.player_spritesheet.get_image(0, 2, TILESIZE, TILESIZE)],
        "right_idle": [self.player_spritesheet.get_image(0, 3, TILESIZE, TILESIZE)],
        "up": self.player_spritesheet.spritesheet_column(1, 4), 
        "down": self.player_spritesheet.spritesheet_column(0, 4), 
        "left": self.player_spritesheet.spritesheet_column(2, 4), 
        "right": self.player_spritesheet.spritesheet_column(3, 4)
        }

    def user_input(self):
        """Gathers any input from the user and changes certain data accordingly."""
        keys = pygame.key.get_pressed()

        # Movement Input
        if keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direction.x, self.direction.y = 0, -1
            self.status = "up"
        elif keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direction.x, self.direction.y = 0, 1
            self.status = "down"
        elif keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.direction.x, self.direction.y = 1, 0
            self.status = "right"
        elif keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.direction.x, self.direction.y = -1, 0
            self.status = "left"
        else: # Player must move to center of tile if no movement keys are being pressed
            self.direction.x = 0
            self.direction.y = 0
        
        # Action Input
        if keys[pygame.K_e]:
            self.interact = True

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not "idle" in self.status:
                self.status = f"{self.status}_idle"

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def movement(self, speed):
        """Moving the player based on user input."""
        # Changing the players position and finding any collisions
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        """Player collision with other objects."""
        # Horizontal collisions
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Moving left
                        self.hitbox.left = sprite.hitbox.right

        # Vertical collisions
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        """Updating the player drawing."""
        self.user_input()
        self.get_status()
        self.animate()
        self.movement(self.speed)
