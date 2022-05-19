import pygame
from config import *

pygame.init()

font = pygame.font.Font(None, 30)

def debug(info, x = 10, y = 10):
    """Debug function, display certain info onto the screen to see what is does."""
    # Getting the screen, creating the text of the information
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, WHITE)
    debug_rect = debug_surf.get_rect(topleft = (x, y))

    # Displaying onto the screen
    pygame.draw.rect(display_surface, BLACK, debug_rect)
    display_surface.blit(debug_surf, debug_rect)