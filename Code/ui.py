import pygame
from config import *

class UI:
    def __init__(self):

        # General
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Bar setup
        self.xp_left = (UI_LEVEL_R)+5
        self.xp_top = SCREEN_HEIGHT-(UI_BAR_HEIGHT//2)-UI_LEVEL_R-5
        self.xp_bar_rect = pygame.Rect(self.xp_left, self.xp_top, UI_XP_BAR_WIDTH, UI_BAR_HEIGHT)
    
    def bar(self, current, max, bg_rect, color):
        # Draw background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # Converting stats
        ratio = current / max
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # Drawing bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
    
    def level(self, level, height):
        text_surface = self.font.render(str(level), False, TEXT_COLOR)
        center_cord = (self.xp_left, self.xp_top+(UI_BAR_HEIGHT//2))
        text_rect = text_surface.get_rect(center=(center_cord))
        points = [
            (center_cord[0] - height, center_cord[1]), 
            (center_cord[0], center_cord[1] + height), 
            (center_cord[0] + height, center_cord[1]), 
            (center_cord[0], center_cord[1] - height)
            ]
        pygame.draw.polygon(self.display_surface, UI_BG_COLOR, points)
        pygame.draw.polygon(self.display_surface, UI_BORDER_COLOR, points, 3)
        self.display_surface.blit(text_surface, text_rect)

    def run(self, player):
        self.bar(player.xp, player.xp_nl, self.xp_bar_rect, UI_XP_COLOR)
        self.level(player.level, UI_LEVEL_R)
