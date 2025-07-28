import pygame
from math import *
from bullet import Bullet
class Tank(pygame.sprite.Sprite):
    '''管理坦克的类'''
    def __init__(self,kt_game,image):
        super().__init__()
        self.screen = kt_game.screen
        self.screen_rect = kt_game.screen.get_rect()
        self.settings = kt_game.settings
        self.game = kt_game
        
        self.id = image
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
        
        self.max_speed = self.settings.tank_max_speed
        self.acc = self.settings.tank_acc
        self.speed = 0
        self.f_acc = self.settings.friction_acc
        self.tank_collision = False
        self.is_moving = False
        self.is_rotating = False
        
        self.kredit = 0
        self.kredit_limit = 5
        self.k_timer = 0
        self.can_move_time = 0 #单位：毫秒
        self.move_timer = 0
        self.can_fire = False
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.dx = 0
        self.dy = 0
    def moving(self):
        global acc
        if self.kredit > 0 and self.can_move_time <= 0:
            self.can_move_time += 300
            self.kredit -= 1
        if self.moving_forward and self.moving_backward:
            self.is_moving = False
            if self.speed > 0.01:
                acc = -self.f_acc
            elif self.speed < 0.01:
                acc = self.f_acc
            else:
                acc = 0
        elif self.moving_backward and self.can_move_time > 0:
            acc = -self.acc
            self.is_moving = True
        elif self.moving_forward and self.can_move_time > 0:
            acc = self.acc
            self.is_moving = True
        else:
            self.is_moving = False
            if self.speed > 0.01:
                acc = -self.f_acc
            elif self.speed < -0.01:
                acc = self.f_acc
            else:
                acc = 0
        self.speed += acc
        if (self.speed < 0.01 or self.speed > -0.01) and acc == 0:
            self.speed = 0
        self.speed = max(min(self.speed,self.max_speed),-self.max_speed)
        
        if self.tank_collision:
            self.dx = (self.speed * cos(radians(self.angle)))/2
            self.dy = (-(self.speed * sin(radians(self.angle))))/2
        else:
            self.dx = self.speed * cos(radians(self.angle))
            self.dy = -(self.speed * sin(radians(self.angle)))
        
        self.x += self.dx
        self.y += self.dy
        
        self.x = max(0, min(self.x, self.screen_rect.width - self.rect.width))
        self.y = max(0, min(self.y, self.screen_rect.height - self.rect.height))
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    def rotate(self):
        if self.turn_left and self.turn_right:
            self.rotate_speed = 0
            self.is_rotating = False
        elif self.turn_left and self.can_move_time > 0:
            self.rotate_speed = 2
            self.is_rotating = True
        elif self.turn_right and self.can_move_time > 0:
            self.rotate_speed = -2
            self.is_rotating = True
        else:
            self.rotate_speed = 0
            self.is_rotating = False
        
        self.angle = (self.rotate_speed + self.angle) % 360
        self.image = pygame.transform.rotate(self.origin_image,self.angle)
        self.old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = self.old_center
    def _update_kredit(self):
        if pygame.time.get_ticks() - self.k_timer >= 1000:
            self.k_timer = pygame.time.get_ticks()
            print(self.speed,acc)
            if self.kredit < self.kredit_limit:
                self.kredit += 1
    def _check_kredit(self):
        if pygame.time.get_ticks() - self.move_timer >= 10:
            self.move_timer = pygame.time.get_ticks()
            if self.can_move_time > 0 and (self.is_moving or self.is_rotating):
                self.can_move_time -= 10
        if self.kredit > 0:
            self.can_fire = True
        else:
            self.can_fire = False
    def _fire_bullet(self):
        if self.can_fire:
            new_bullet = Bullet(self.game,self)
            self.game.bullets.add(new_bullet)
            self.kredit -= 1
    def update(self):
        self.screen.blit(self.image,self.rect)
        self.moving()
        self.rotate()
        self._update_kredit()
        self._check_kredit()