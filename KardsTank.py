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
        self.font = self.settings.font
        
        
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.player1 = Tank(self,'Ger')
        self.player2 = Tank(self,'Eng')
        self.players = pygame.sprite.Group(self.player1,self.player2)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("这个,,游戏。那。坦克,打4对面?对面。。是,你的机油?用wasd 上下左右。冻起来,然后j和,数字0打.")
        self.clock = pygame.time.Clock()
    def _check_events(self):
        self._check_tanks_collision()
        self._check_tank_bullets_collision()
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
                        
        if event.key == pygame.K_j and self.player1.can_fire:
            self.player1._fire_bullet()
        if event.key == pygame.K_KP0 and self.player2.can_fire:
            self.player2._fire_bullet()
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
        self.bullets.update()
        self.players.update()
        self._update_bullet()
        txt = self.font.render(f'剩余指挥点{self.player1.kredit},可移动毫秒数{self.player1.can_move_time}',True,(255,255,255))
        self.screen.blit(txt,(100,100))
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
                bullet.alive = False
            if bullet.alive == False:
                self.bullets.remove(bullet)
    def _check_tanks_collision(self):
        for tank1 in self.players:
            for tank2 in self.players:
                if tank1 != tank2 and pygame.sprite.collide_rect(tank1,tank2):
                    tank1.tank_collision,tank2.tank_collision = True,True
                    dx = tank1.rect.centerx - tank2.rect.centerx
                    dy = tank1.rect.centery - tank2.rect.centery
                    if dx == 0 and dy == 0:
                        dx, dy = 1, 0
                    distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)
                    dx, dy = dx / distance, dy / distance
                    tank1.rect.x += dx * self.settings.push_strength
                    tank1.rect.y += dy * self.settings.push_strength
                    tank2.rect.x -= dx * self.settings.push_strength
                    tank2.rect.y -= dy * self.settings.push_strength
                else:
                    tank1.tank_collision,tank2.tank_collision = False,False
    def _check_tank_bullets_collision(self):
        for tank in self.players:
            hits = pygame.sprite.spritecollide(tank,self.bullets,False)
            for bullet in hits:
                if bullet.belong_to != tank:
                    print(f'玩家{tank.id}被{bullet.belong_to.id}击中')
                    bullet.alive = False
                elif pygame.time.get_ticks() - bullet.create_time > 100:
                    print(f'玩家{tank.id}被自己击中')
                    bullet.alive = False
    
    def run_game(self):
        '''开始游戏的函数'''
        while 1:
            self._check_events()
            self._update_screen()
if __name__ == '__main__':
    kt = KardsTank()
    kt.run_game()