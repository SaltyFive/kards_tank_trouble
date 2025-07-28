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
        self.FPS = 60
        
        self.tank_speed = 2
        self.push_strength = 5
        
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = 60,60,60