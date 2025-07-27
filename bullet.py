import pygame
from math import *

class Bullet(pygame.sprite.Sprite):
    '''管理子弹的类'''
    def __init__(self,kt_game,belong_to):
        super().__init__()
        self.screen = kt_game.screen
        self.settings = kt_game.settings
        self.color = self.settings.bullet_color
        self.angle = belong_to.angle
        self.speed_x = self.settings.bullet_speed * cos(radians(self.angle))
        self.speed_y = -(self.settings.bullet_speed * sin(radians(self.angle)))
        self.belong_to = belong_to
        self.create_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.center = belong_to.rect.center
        self.rect.x += 10 * cos(radians(belong_to.angle))
        self.rect.y -= 10 * sin(radians(belong_to.angle))
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        if self.rect.x <= 0 or self.rect.x >= self.settings.screen_width:
            self.speed_x = -self.speed_x
        if self.rect.y <= 0 or self.rect.y >= self.settings.screen_height:
            self.speed_y = -self.speed_y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)