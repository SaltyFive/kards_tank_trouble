import sys
import pygame
from settings import Settings
from tank import Tank
from bullet import Bullet
class KardsTank:
    '''管理游戏资源及其行为'''
    def __init__(self):
        '''初始化游戏'''
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.player1 = Tank(self,'Ger')
        self.player2 = Tank(self,'Eng')
        self.players = pygame.sprite.Group()
        self.players.add(self.player1)
        self.players.add(self.player2)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("这个,,游戏。那。坦克,打4对面?对面。。是,你的机油?用wasd 上下左右。冻起来,然后j和,数字0打.")
        self.clock = pygame.time.Clock()
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)
    def _check_keydown(self,event):
        if event.key == pygame.K_w:
            self.player1.moving_forward = True
        elif event.key == pygame.K_s:
            self.player1.moving_backward = True
        
        if event.key == pygame.K_UP:
            self.player2.moving_forward = True
        elif event.key == pygame.K_DOWN:
            self.player2.moving_backward = True
        
        if event.key == pygame.K_a:
            self.player1.turn_left = True
        elif event.key == pygame.K_d:
            self.player1.turn_right = True
        
        if event.key == pygame.K_LEFT:
            self.player2.turn_left = True
        elif event.key == pygame.K_RIGHT:
            self.player2.turn_right = True
                        
        if event.key == pygame.K_j:
            self._fire_bullet(self.player1)
        if event.key == pygame.K_KP0:
            self._fire_bullet(self.player2)
    def _check_keyup(self,event):
        if event.key == pygame.K_w:
            self.player1.moving_forward = False
        elif event.key == pygame.K_s:
            self.player1.moving_backward = False
        if event.key == pygame.K_UP:
            self.player2.moving_forward = False
        elif event.key == pygame.K_DOWN:
            self.player2.moving_backward = False
                        
        if event.key == pygame.K_a:
            self.player1.turn_left = False
        elif event.key == pygame.K_d:
            self.player1.turn_right = False
        if event.key == pygame.K_LEFT:
            self.player2.turn_left = False
        elif event.key == pygame.K_RIGHT:
            self.player2.turn_right = False
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.players.update()
        self.bullets.update()
        self._update_bullet()
        pygame.display.flip()
        
        self.clock.tick(self.settings.FPS)
    def _fire_bullet(self,belong_to):
        new_bullet = Bullet(self,belong_to)
        self.bullets.add(new_bullet)
    def _update_bullet(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets.copy():
            if pygame.time.get_ticks() - bullet.create_time >= 3000:
                self.bullets.remove(bullet)
    def run_game(self):
        '''开始游戏的函数'''
        while 1:
            self._check_events()
            self._update_screen()
if __name__ == '__main__':
    kt = KardsTank()
    kt.run_game()