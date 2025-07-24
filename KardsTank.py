import sys
import pygame

class KardsTank:
    '''管理游戏资源及其行为'''
    def __init__(self):
        '''初始化游戏'''
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = 230,230,230
        pygame.display.set_caption("这个,,游戏。那。坦克,打4对面?对面。。是,你的机油?用wasd 上下左右。冻起来,然后j和,数字0打.")
        
    def run_game(self):
        '''开始游戏的函数'''
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
        pygame.display.flip()
        self.screen.fill(self.bg_color)
        
if __name__ == '__main__':
    kt = KardsTank()
    kt.run_game()