import pygame
 
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

x_speed = 0
y_speed = 0

pygame.init()
 
size = (700, 600) # x,y
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Runner")

map_one = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('reaper.png')
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 570

    def update(self):
        player.rect.x += x_speed
        player.rect.y += y_speed
        if player.rect.x < 28:
            player.rect.x = 28
        if player.rect.x > 610:
            player.rect.x = 610
        if player.rect.y < 25:
            player.rect.y = 25
        if player.rect.y > 520:
            player.rect.y = 520

        player_wall = pygame.sprite.spritecollide(player, walls_list, False)
        if player_wall:
            player.rect.bottom = player_wall[0].rect.top
            if y_speed < 0:
                player.rect.top = player_wall[0].rect.bottom


        player_hit_enemy = pygame.sprite.spritecollide(player, enemy_list, False)
        if player_hit_enemy:
            self.rect.x -= 20
        
            
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('boss_wolf.png')
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 50
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
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
        self.swap = 0


    def update(self):
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

        enemy_hit_player = pygame.sprite.spritecollide(enemy, player_list, False)
        if enemy_hit_player:
            self.rect.x += 20
        

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((28,25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

all_sprites_list = pygame.sprite.Group()
#boss = Boss()
player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
walls_list = pygame.sprite.Group()
all_sprites_list.add(player)
#all_sprites_list.add(boss)
enemy = Enemy(600,535)
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)
all_sprites_list.add(enemy)
all_sprites_list.add(enemy_list)


for x in range(25):
    for y in range(25):
        if map_one[x][y] == 1:
            wall = Wall(x*28,y*24)
            all_sprites_list.add(wall)
            walls_list.add(wall)


done = False

clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    y_speed += 2 # gravity that constantly pulls player down
    x_speed = 0

    player.rect.y += 10
    player_wall_hit = pygame.sprite.spritecollide(player, walls_list, False)
    player.rect.y -= 10
    if player_wall_hit:
        if keys[pygame.K_UP]:
            y_speed -= 30
            player.image = pygame.image.load('reaper.png')
    if keys[pygame.K_RIGHT]:
        player.image = pygame.image.load('reaper.png')
        x_speed += 3
    if keys[pygame.K_LEFT]:
        player.image = pygame.image.load('reaper_backwards.png')
        x_speed -= 3    


    screen.fill(BLACK)
 
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
