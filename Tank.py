import pygame 
class Tank:
    '''管理坦克的类'''
    def __init__(self,kt_game,image):
        self.screen = kt_game.screen
        self.screen_rect = kt_game.screen.get_rect()
        
        self.image = pygame.image.load(f'images/{image}.png')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.moving_forward = False
        self.moving_backward = False
    def blit(self):
        self.screen.blit(self.image,self.rect)
        self.moving()
    
    def moving(self):
        if self.moving_forward:
            self.rect.y -= 1
        if self.moving_backward:
            self.rect.y += 1