import pygame
import random
from pygame import mixer
 
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
pygame.init()
checker = False
speed_powerup = False
speed_powerdown = False
health_powerup = False
health_powerdown = False
count = 1000000
font = pygame.font.SysFont('ComicSans', 30, True, False)


mixer.music.load('game_audios/bgm.mp3')
mixer.music.play()
        
size = (700, 600) # x,y
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Runner")

map_one = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('game_pics/reaper.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.swap = 0 # facing left
        self.player_wall = []
        self.health = 20
        self.damage = 2
        self.coin = 0
        
        
    def update(self):
        if self.health <= 0:
            self.kill()
        player.rect.x += self.x_speed
        player.rect.y += self.y_speed
        if player.rect.x < 28:
            player.rect.x = 28
        if player.rect.x > 610:
            player.rect.x = 610
        if player.rect.y < 25:
            player.rect.y = 25
        if player.rect.y > 520:
            player.rect.y = 520
        if keys[pygame.K_RIGHT]:
            self.swap = 1
        if keys[pygame.K_LEFT]:
            self.swap = 0
            
        self.player_wall = pygame.sprite.spritecollide(player, walls_list, False)
        if self.player_wall:
            player.rect.bottom = self.player_wall[0].rect.top # this is when the player is standing on top of the platform
            if self.y_speed < 0:
                player.rect.top = self.player_wall[0].rect.bottom + 1 # this means if the player touches the bottom of a platform above it, it won't stick to it beacause the + 1 causes a pixel gap in between so they are not actually touching
        
        player_hit_enemy = pygame.sprite.spritecollide(player, enemy_list, False)
        if player_hit_enemy:
            self.health -= enemy.damage
            if self.swap == 1:
                self.rect.x -= 80
                enemy.rect.x += 30
                if enemy.rect.x > 610:
                    enemy.rect.x = 610
            else:
                self.rect.x += 80
                enemy.rect.x -= 30
                if enemy.rect.x < 30:
                    enemy.rect.x = 30
            mixer.music.load('game_audios/enemy_attack.mp3')
            mixer.music.play()

        player_hit_portal = pygame.sprite.spritecollide(player, portal_list, False)
        if player_hit_portal:
            all_sprites_list.empty()

                    
        player_collects_coin = pygame.sprite.spritecollide(player, coin_list, True)
        if player_collects_coin:
            self.coin += 1
            mixer.music.load('game_audios/coin_pickup.mp3')
            mixer.music.play()
        


class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_walk = [pygame.image.load('boss_walk/boss1.png'),pygame.image.load('boss_walk/boss2.png'),pygame.image.load('boss_walk/boss3.png'),pygame.image.load('boss_walk/boss4.png'),pygame.image.load('boss_walk/boss5.png'),pygame.image.load('boss_walk/boss6.png'),pygame.image.load('boss_walk/boss7.png'),pygame.image.load('boss_walk/boss8.png'),pygame.image.load('boss_walk/boss9.png'),pygame.image.load('boss_walk/boss10.png'),pygame.image.load('boss_walk/boss11.png')]
        self.boss_walkopposite = [pygame.image.load('boss_walkopposite/boss1.png'),pygame.image.load('boss_walkopposite/boss2.png'),pygame.image.load('boss_walkopposite/boss3.png'),pygame.image.load('boss_walkopposite/boss4.png'),pygame.image.load('boss_walkopposite/boss5.png'),pygame.image.load('boss_walkopposite/boss6.png'),pygame.image.load('boss_walkopposite/boss7.png'),pygame.image.load('boss_walkopposite/boss8.png'),pygame.image.load('boss_walkopposite/boss9.png'),pygame.image.load('boss_walkopposite/boss10.png'),pygame.image.load('boss_walkopposite/boss11.png')]
        self.current_image = 0
        self.image = self.boss_walk[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.boss_x_speed = -2
        self.boss_y_speed = 0
        self.delay = pygame.time.get_ticks()
        self.swap = 0 # facing left
        self.health = 10
        self.damage = 3
        
    def update(self):
        if self.health <= 0:
            self.kill()
            coin = Coin(self.rect.x,self.rect.y)
            coin_list.add(coin)
            all_sprites_list.add(coin)
            all_sprites_list.add(coin_list)           
            portal = Portal(40,40)
            portal_list.add(portal)
            all_sprites_list.add(portal)
            all_sprites_list.add(portal_list)

            
        time_now = pygame.time.get_ticks()
        if time_now - self.delay >= 125: # controls boss running animation speed
            self.current_image += 1
            if self.current_image > 4:
                self.current_image = 0
            if self.swap == 0: # swap changes the list of images to the one facing the other direction
                self.image = self.boss_walk[self.current_image]
            else:
                self.image = self.boss_walkopposite[self.current_image]
            self.delay = pygame.time.get_ticks()
        self.rect.x += self.boss_x_speed
        self.rect.y += self.boss_y_speed
        if self.rect.x < 30:
            self.boss_x_speed *= -1
            self.swap = 1
        if self.rect.x > 600:
            self.boss_x_speed *= -1
            self.swap = 0

        boss_hit_by_sword = pygame.sprite.spritecollide(self, sword_list, False)
        if boss_hit_by_sword:
            self.health -= player.damage
            if self.swap == 1:
                self.rect.x -= 80
            else:
                self.rect.x += 80
            
        
class Sword(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('game_pics/sword.png')
        self.rect = self.image.get_rect()
        if player.swap == 1:
            self.rect.x = player.rect.x + 50
        else:
            self.rect.x = player.rect.x - 50
            self.image = pygame.transform.flip(self.image, True, False) # This flips the image vertically. True means in the x direction. False because no flip is needed in the y direction.
        self.rect.y = player.rect.y
        self.sword_on_screen = True
        self.spawn_time = pygame.time.get_ticks()
    
    def update(self):
        if self.sword_on_screen:
            now = pygame.time.get_ticks()
            mixer.music.load('game_audios/sword.mp3')
            mixer.music.play()
            if now - self.spawn_time >= 100:
                self.kill()
                self.sword_on_screen = False
     
   
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #self.total_enemies = 0
        self.walk = [pygame.image.load('walk/enemy1.png'),pygame.image.load('walk/enemy2.png'),pygame.image.load('walk/enemy3.png'),pygame.image.load('walk/enemy4.png'),pygame.image.load('walk/enemy5.png')]
        self.walk_opposite = [pygame.image.load('walk_opposite/enemy1_opposite.png'),pygame.image.load('walk_opposite/enemy2_opposite.png'),pygame.image.load('walk_opposite/enemy3_opposite.png'),pygame.image.load('walk_opposite/enemy4_opposite.png'),pygame.image.load('walk_opposite/enemy5_opposite.png')]
        self.current_image = 0
        self.image = self.walk[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enemy_x_speed = -2
        self.enemy_y_speed = 0
        self.delay = pygame.time.get_ticks()
        self.swap = 0 # facing left
        self.health = 5
        self.damage = 1
        
    def update(self):
        if self.health <= 0:
            self.kill()
            #self.total_enemies -= 1
            coin = Coin(self.rect.x,self.rect.y)
            coin_list.add(coin)
            all_sprites_list.add(coin)
            all_sprites_list.add(coin_list)

        if len(enemy_list.sprites()) == 0:
            boss = Boss(100,100)
            boss_list = pygame.sprite.Group()
            boss_list.add(boss)
            all_sprites_list.add(boss)
            all_sprites_list.add(boss_list)

            
        time_now = pygame.time.get_ticks()
        if time_now - self.delay >= 125: # controls enemy running animation speed
            self.current_image += 1
            if self.current_image > 4:
                self.current_image = 0
            if self.swap == 0: # swap changes the list of images to the one facing the other direction
                self.image = self.walk[self.current_image]
            else:
                self.image = self.walk_opposite[self.current_image]
            self.delay = pygame.time.get_ticks()
        self.rect.x += self.enemy_x_speed
        self.rect.y += self.enemy_y_speed
        if self.rect.x < 28:
            self.enemy_x_speed *= -1
            self.swap = 1
        if self.rect.x > 610:
            self.enemy_x_speed *= -1
            self.swap = 0

        enemy_hit_by_sword = pygame.sprite.spritecollide(self, sword_list, False)
        if enemy_hit_by_sword:
            self.health -= player.damage
            if self.swap == 1:
                self.rect.x -= 80
            else:
                self.rect.x += 80


class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((28,25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Portal(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('game_pics/portal.png')
        self.rect = self.image.get_rect()       
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.spin = [pygame.image.load('coins/coin1.png'),pygame.image.load('coins/coin2.png'),pygame.image.load('coins/coin3.png'),pygame.image.load('coins/coin4.png')]
        self.current_image = 0
        self.image = self.spin[self.current_image]
        self.rect = self.image.get_rect()
        self.delay = pygame.time.get_ticks()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.delay >= 200: # controls coin spinning animation speed
            self.current_image += 1
            if self.current_image > 3:
                self.current_image = 0
            self.image = self.spin[self.current_image]
            self.delay = pygame.time.get_ticks()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        not_valid = True
        same = False
        while not_valid:
            x_coordinate = random.randint(50,650)
            y_coordinate = random.randint(50,550)
            if x_coordinate != wall.rect.x and y_coordinate != wall.rect.y:
                if len(coin_list) != 0:
                    all_coins_list = coin_list.sprites()
                    for i in all_coins_list:
                        if x_coordinate == i.rect.x or y_coordinate == i.rect.y:
                            same = True
                not_valid = same

        self.image = pygame.image.load('game_pics/powerup.png')
        self.rect = self.image.get_rect()       
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate

        self.r = random.randint(0,3)

    def update(self):
        global all_powerups
        global count
        global speed_powerup
        global speed_powerdown
        global health_powerup
        global health_powerdown

        player_powerup = pygame.sprite.spritecollide(self, player_list, False)
        for a in player_powerup:
            if self.r == 0:
                speed_powerup = True
            elif self.r == 1:
                speed_powerdown = True
            elif self.r == 2:
                health_powerup = True
            else:
                health_powerdown = True
                
            self.kill()
            count = 0

all_sprites_list = pygame.sprite.Group()

powerup_list = pygame.sprite.Group()
all_sprites_list.add(powerup_list)

coin_list = pygame.sprite.Group()

player = Player(40,570)
player_list = pygame.sprite.Group()
player_list.add(player)
walls_list = pygame.sprite.Group()
all_sprites_list.add(player)

enemy = Enemy(600,535)
enemy2 = Enemy(500,535)
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)
enemy_list.add(enemy2)

sword_list = pygame.sprite.Group()
all_sprites_list.add(enemy)
all_sprites_list.add(enemy2)
all_sprites_list.add(enemy_list)

portal_list = pygame.sprite.Group()
    
coin2 = Coin(340,340)
coin_list.add(coin2)
all_sprites_list.add(coin2)
coin3 = Coin(500,500)
coin_list.add(coin3)
all_sprites_list.add(coin3)

for x in range(25):
    for y in range(25):
        if map_one[x][y] == 1:
            wall = Wall(x*28,y*24)
            all_sprites_list.add(wall)
            walls_list.add(wall)

health_text = font.render('Health:', True, WHITE)
coins_text = font.render('Coins:', True, WHITE)

done = False
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    keys = pygame.key.get_pressed()

    if not player.player_wall:
        player.y_speed += 2 # gravity that constantly pulls player down

    if player.player_wall:
        if player.player_wall[0].rect.bottom < player.rect.top:
            player.y_speed += 2
            
    player.x_speed = 0
    player.rect.y += 10
    player_wall_hit = pygame.sprite.spritecollide(player, walls_list, False)
    player.rect.y -= 10
    
    if player_wall_hit:
        if keys[pygame.K_UP]:
            player.y_speed -= 30
            player.image = pygame.image.load('game_pics/reaper.png')
            
    if keys[pygame.K_RIGHT]:
        player.image = pygame.image.load('game_pics/reaper.png')
        if speed_powerup == True:
            player.x_speed += 6
            
        if speed_powerdown == True:
            player.x_speed += 1

        player.x_speed += 3
            
    if keys[pygame.K_LEFT]:
        player.image = pygame.image.load('game_pics/reaper_backwards.png')
        if speed_powerup == True:
            player.x_speed -= 6

        if speed_powerdown == True:
            player.x_speed -= 1

        player.x_speed -= 3
            
    if keys[pygame.K_SPACE] and len(sword_list.sprites()) == 0:
        sword = Sword()
        sword_list.add(sword)
        all_sprites_list.add(sword)

    if player.health < 10 and not checker:
        checker = True
        powerup = PowerUp()
        powerup_list.add(powerup)
        all_sprites_list.add(powerup)

    if health_powerup == True:
        player.health += 10
        health_powerup = False

    if health_powerdown == True:
        player.health -= 10
        player_powerdown = False
        
    if count == 600:
        speed_powerup = False

    if player.health > 30:
        player.health = 30

    if player.health < 0:
        player.health = 0

    if abs(enemy.rect.x - player.rect.x) < 20 and (enemy.rect.y - player.rect.y) < 20:
        mixer.music.load('game_audios/roar.wav')
        mixer.music.play()
        
    count += 1

    screen.fill((255,255,255))
    background = pygame.image.load('game_pics/background.jpg')
    screen.blit(background,(0,0))
    
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    health_value = font.render(str(player.health), True, WHITE)
    screen.blit(health_text, [30, 10])
    screen.blit(health_value, [120, 10])

    coins_value = font.render(str(player.coin), True, WHITE)
    screen.blit(coins_text, [500, 10])
    screen.blit(coins_value, [580, 10])

    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
