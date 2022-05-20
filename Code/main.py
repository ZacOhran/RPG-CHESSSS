import pygame
import sys
from config import *
from debug import debug
from level import Level

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        main_icon = pygame.image.load('./Graphics/Images/player.png')
        pygame.display.set_caption('Schmoo')
        pygame.display.set_icon(main_icon)
        self.clock = pygame.time.Clock()

        # Creating the level, and running variable
        self.running = True
        self.level = Level()
    
    def main(self):
        """Main game loop. Displays the gameplay."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Updating the screen
            self.screen.fill(BLACK)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    # Creating the game
    game = Game()
    game.main()

    # Closing the code
    pygame.quit()
    sys.exit()