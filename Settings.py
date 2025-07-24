import pygame
class Settings:
    '''存放所有游戏设置'''
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = (self.screen_width,self.screen_height)
        self.bg_color = 230,230,230
        
        self.text_color = 30,30,30
        self.font = pygame.font.SysFont(None,48)