import pygame
from math import *

class Tank(pygame.sprite.Sprite):
    '''管理坦克的类'''
    def __init__(self,kt_game,image):
        self.screen = kt_game.screen
        self.screen_rect = kt_game.screen.get_rect()
        
        self.origin_image = pygame.image.load(f'images/{image}.png').convert_alpha()
        self.image = self.origin_image
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.moving_forward = False
        self.moving_backward = False
        
        self.angle = 0
        self.rotate_speed = 0
        self.turn_left = False
        self.turn_right = False
        
        self.velocity = 5
                
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def moving(self):
        if self.moving_forward and self.moving_backward:
            speed = 0
        elif self.moving_backward:
            speed = -self.velocity
        elif self.moving_forward:
            speed = self.velocity
        else:
            speed = 0
        
        dx = speed * cos(radians(self.angle))
        dy = -(speed * sin(radians(self.angle)))
        
        self.x += dx
        self.y += dy
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
    def rotate(self):
        print(self.angle)
        if self.turn_left and self.turn_right:
            self.rotate_speed = 0
        elif self.turn_left:
            self.rotate_speed = 2
        elif self.turn_right:
            self.rotate_speed = -2
        else:
            self.rotate_speed = 0
        
        self.angle = (self.rotate_speed + self.angle) % 360
        self.image = pygame.transform.rotate(self.origin_image,self.angle)
        self.old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = self.old_center
    def update(self):
        self.screen.blit(self.image,self.rect)
        self.moving()
        self.rotate()