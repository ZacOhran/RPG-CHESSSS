from pygame import *
from KnightClass import *
from stats import *
from main import *


    


class Battle:

    def __init__():
        # create buttons, background, sprites, etc
        # pygame.draw.rect(game.screen, image = 'button1')
        bg = Background('battlebackground.png', (0,0))
        pass


    def drawing(self):
        # draw background, buttons, sprites, etc
        game.screen.blit(Background.image, Background.rect)
        


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



while self.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
    
    # Updating the screen
    screen.fill(BLACK)
    Battle.drawing()
    pygame.display.update()
    clock.tick(FPS)