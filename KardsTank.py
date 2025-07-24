import sys
import pygame
from settings import Settings
from tank import Tank
class KardsTank:
    '''管理游戏资源及其行为'''
    def __init__(self):
        '''初始化游戏'''
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.tank = Tank(self,'Ger')
        pygame.display.set_caption("这个,,游戏。那。坦克,打4对面?对面。。是,你的机油?用wasd 上下左右。冻起来,然后j和,数字0打.")
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.tank.moving_forward = True
                    elif event.key == pygame.K_s:
                        self.tank.moving_backward = True
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.tank.moving_forward = False
                    elif event.key == pygame.K_s:
                        self.tank.moving_backward = False
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.tank.blit()
        pygame.display.flip()
    
    def run_game(self):
        '''开始游戏的函数'''
        while 1:
            self._check_events()
            self._update_screen()
if __name__ == '__main__':
    kt = KardsTank()
    kt.run_game()