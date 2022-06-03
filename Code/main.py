import pygame
from sys import exit
from config import *
from debug import debug
from level import Level
from player import Player

class Game:
    """Create and run the entire game."""
    
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        main_icon = pygame.image.load('./Graphics/Images/player.png')
        pygame.display.set_caption('Schmoo')
        pygame.display.set_icon(main_icon)
        self.clock = pygame.time.Clock()

        # Creating player
        self.player = Player()

        # Creating the level
        self.running = True
        self.tavern_0 = Level("./Graphics/Levels/Tavern_0", self.player)
    
    def main(self):
        """Main game loop. Displays the gameplay."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Updating the screen
            self.screen.fill(BLACK)
            self.tavern_0.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    # Creating the game
    game = Game()
    game.main()

    # Closing the code
    pygame.quit()
    exit()