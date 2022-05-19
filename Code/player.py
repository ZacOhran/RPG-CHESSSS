import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        # Creating the player sprite
        super().__init__(groups)
        self.image = pygame.image.load('./Graphics/Images/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-8, -8)

        # Movement setup
        self.direction = pygame.math.Vector2()
        self.speed = 4

        # Collision setup
        self.obstacle_sprites = obstacle_sprites
    
    def user_input(self):
        """Gathers any input from the user and changes certain data accordingly."""
        keys = pygame.key.get_pressed()

        # Vertical movement
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.direction.y = -1
        elif keys[pygame.K_s] and not keys[pygame.K_w]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # Horizontal movement
        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.direction.x = 1
        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def movement(self, speed):
        """Moving the player based on user input."""
        # Ensuring the player's speed is constant
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

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