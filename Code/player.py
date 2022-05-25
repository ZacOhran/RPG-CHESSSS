import pygame
from config import *

class Player(pygame.sprite.Sprite):
    """Create the player object, everyway the player interacts with the environment here."""
    
    def __init__(self, pos, groups, obstacle_sprites):
        # Creating the player sprite
        super().__init__(groups)
        self.image = pygame.image.load('./Graphics/Images/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0)

        # Movement setup
        self.direction = pygame.math.Vector2()
        self.speed = 4

        # Collision setup
        self.obstacle_sprites = obstacle_sprites
    
    def user_input(self):
        """Gathers any input from the user and changes certain data accordingly."""
        keys = pygame.key.get_pressed()

        # Vertical movement
        if self.hitbox.x % TILESIZE == 0 and self.hitbox.y % TILESIZE == 0: # Ensure player is centered in tile
            if keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
                self.direction.x, self.direction.y = 0, -1
            elif keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:
                self.direction.x, self.direction.y = 0, 1
            elif keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_w] and not keys[pygame.K_s]:
                self.direction.x, self.direction.y = 1, 0
            elif keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
                self.direction.x, self.direction.y = -1, 0
            else: # Player must move to center of tile if no movement keys are being pressed
                self.direction.x = 0
                self.direction.y = 0
    
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
        self.movement(self.speed)