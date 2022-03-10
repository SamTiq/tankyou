import pygame
from random import randint
from sense_hat import SenseHat

sense= SenseHat()

sense.set_imu_config(False, True, False)

pygame.font.init()


class Tank:
    def __init__(self):

        self.pos = (100, resolution_x - 100)
        self.health = 3
        self.speed = 15
        self.rect = pygame.Rect((self.pos[0], self.pos[1]), (default_tank.get_width(), default_tank.get_height()))
        self.invisibility = 0
        self.score = 0
    
    def move(self, pos):
        if pos[0]>=0 and pos[0]<=resolution_x-50:
            self.pos = pos
 
 
    
    def collision(self, tab):
        if self.invisibility==0:
            for element in tab:
                if self.rect.colliderect(element.rect):
                    self.health-=1
                    
                    Obstacle.instances.remove(element)
                    self.invisibility=50


class Obstacle:
    instances=[]
    def __init__(self):
        self.pos = (randint(0,resolution_x), 0)
        self.health = 3
        self.rect = pygame.Rect((self.pos[0], self.pos[1]), (crate_obstacle.get_width(), crate_obstacle.get_height()))
        '''
        self.size = size
        self.sprite = sprite
        self.speed = speed
        '''
        Obstacle.instances.append(self)

    def move(self):
        if self.pos[1]<resolution_y:
            self.pos = (self.pos[0], self.pos[1]+10)
        else:
            tank.score +=1
            Obstacle.instances.remove(self)

    def display(self):
        window_surface.blit(crate_obstacle, [self.pos[0], self.pos[1]])

    
      
def display_tank(i):
    if tank.invisibility==0:
        if i%50<=25:
            window_surface.blit(default_tank, [tank.pos[0], tank.pos[1]])
        else:
            window_surface.blit(default_tank2, [tank.pos[0], tank.pos[1]])  
    else:
        print("a")
        if i%100<=25:
            window_surface.blit(default_tank, [tank.pos[0], tank.pos[1]])
        elif i%100<=50:
            window_surface.blit(invicibility_tank, [tank.pos[0], tank.pos[1]])
        elif i%100<=75:
            window_surface.blit(default_tank2, [tank.pos[0], tank.pos[1]])
        else:
            window_surface.blit(invicibility_tank2, [tank.pos[0], tank.pos[1]])
            

def allMoveObstacle():
    for element in Obstacle.instances:
        element.move()

def allDisplayObstacle():
    for element in Obstacle.instances:
        element.display()

def updateRect():
    tank.rect = pygame.Rect((tank.pos[0], tank.pos[1]), (default_tank.get_width(), default_tank.get_height()))
    for element in Obstacle.instances:
        element.rect= pygame.Rect((element.pos[0], element.pos[1]), (crate_obstacle.get_width(), crate_obstacle.get_height()))

def displayHearth(tank):

    if tank.health<=0:
        window_surface.blit(greyHeart, [resolution_x-60 , 20])
        window_surface.blit(greyHeart, [resolution_x-110  , 20])
        window_surface.blit(greyHeart, [resolution_x-160 , 20])

    if tank.health==1:
        window_surface.blit(greyHeart, [resolution_x-60 , 20])
        window_surface.blit(greyHeart, [resolution_x-110  , 20])
        window_surface.blit(redHeart, [resolution_x-160 , 20])

    if tank.health==2:
        window_surface.blit(greyHeart, [resolution_x-60 , 20])
        window_surface.blit(redHeart, [resolution_x-110  , 20])
        window_surface.blit(redHeart, [resolution_x-160 , 20])

    if tank.health==3:
        window_surface.blit(redHeart, [resolution_x-60 , 20])
        window_surface.blit(redHeart, [resolution_x-110  , 20])
        window_surface.blit(redHeart, [resolution_x-160 , 20])

y_bg = 0
resolution_x = 800
resolution_y = 800

window_surface=pygame.display.set_mode((resolution_x, resolution_y))


default_tank = pygame.image.load('assets/default_tank.png')
default_tank.convert_alpha()
default_tank = pygame.transform.scale(default_tank, [50, 70])

default_tank2 = pygame.image.load('assets/default_tank_sprite_2.png')
default_tank2.convert_alpha()
default_tank2 = pygame.transform.scale(default_tank2, [50, 70])

invicibility_tank= pygame.image.load('assets/invincible_tank_sprite_2.png')
invicibility_tank.convert_alpha()
invicibility_tank = pygame.transform.scale(invicibility_tank, [50, 70])

invicibility_tank2 = pygame.image.load('assets/invincible_tank_sprite_1.png')
invicibility_tank2.convert_alpha()
invicibility_tank2 = pygame.transform.scale(invicibility_tank2, [50, 70])



redHeart = pygame.image.load('assets/redHeart.png')
greyHeart = pygame.image.load('assets/greyHeart.png')
redHeart = pygame.transform.scale(redHeart, [50, 50])
greyHeart = pygame.transform.scale(greyHeart, [50, 50])

background = pygame.image.load('assets/background.png')
background.convert_alpha()
background = pygame.transform.scale(background, [resolution_x, resolution_y])

leaderboard_background = pygame.image.load('assets/leaderboard.jpg')
leaderboard_background = pygame.transform.scale(leaderboard_background, [resolution_x, resolution_y])

menu_background = pygame.image.load('assets/menu.jpg')
menu_background = pygame.transform.scale(menu_background, [resolution_x, resolution_y])

crate_obstacle = pygame.image.load('assets/crate_obstacle.png')
crate_obstacle.convert_alpha()
crate_obstacle = pygame.transform.scale(crate_obstacle, [50, 50])

font = pygame.font.SysFont("arial", 30)

tank = Tank()
i=0
menu = True #change this and make it work <3
game = False
leaderboard = False
while menu or game or leaderboard:
    #MENUUUUUUUUUUUUU
    while game:
        
        if i%5==0:
            Obstacle()

        i+=1
        gyro_only = sense.get_gyroscope()
        print(gyro_only["pitch"])
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                game=False
            
        if gyro_only["pitch"]>180 and gyro_only["pitch"]<350:

            tank.move((tank.pos[0]+tank.speed, tank.pos[1]))

        if gyro_only["pitch"]<180 and gyro_only["pitch"]>10:
            tank.move((tank.pos[0]-tank.speed, tank.pos[1]))
                
        if event.type==pygame.KEYDOWN:  
            if event.key==pygame.K_RIGHT:
                tank.move((tank.pos[0]+tank.speed, tank.pos[1]))

            if event.key==pygame.K_LEFT:
                tank.move((tank.pos[0]-tank.speed, tank.pos[1]))
                
        if tank.invisibility != 0:
            tank.invisibility-=1

        window_surface.fill(pygame.Color(0,0,0))
        print("test")
        window_surface.blit(background, [0, 0])
        bg_height = background.get_rect().height
        rel_y = y_bg %  bg_height

        window_surface.fill(pygame.Color(0,0,0))
        window_surface.blit(background, [0, rel_y - bg_height])
        if rel_y >= 0:
                window_surface.blit(background,[0,rel_y])

        y_bg += 1

        score = str(tank.score)
        textimage = font.render(score, True, (255,255,255))
        window_surface.blit(textimage, (4,4))

        tank.collision(Obstacle.instances)
        allMoveObstacle()
        allDisplayObstacle()
        updateRect()

        display_tank(i)

        if tank.health == 0:
            tank.health = 3
            menu = True
            game = False
            Obstacle.instances= []
            f = open("leaderboard.txt", "r")
            text = f.read()
            f.close()
            tab = text.split("/")

            for i in range(len(tab)):
                tab[i]=int(tab[i])

            tab.append(tank.score)
            tab=sorted(tab)

            insert = ""

            for i in range(1, len(tab)-1):

                insert = insert + str(tab[i]) + "/"

            insert = insert + str(tab[len(tab)-1])
            f = open("leaderboard.txt", "w")
            f.write(insert)
            f.close()
            tank.score = 0
        displayHearth(tank)
        pygame.time.delay(4)

        pygame.display.flip()

    while(menu):
        pygame.time.delay(10)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[1]>565 and pos[1]<637:
                    menu = False
                    game = True
                    leaderboard = False
                    

                elif pos[1]>660 and pos[1]<740:
                    menu = False
                    game = False
                    leaderboard = True

                elif pos[1]>755 and pos[1]<789:
                    menu = False
                    game = False

        window_surface.blit(menu_background, [0, 0])
        pygame.display.flip()

# -----------------------------
# Leaderboard loop
# -----------------------------
    update_score = False
    while(leaderboard):
        pygame.time.delay(10)
        window_surface.blit(leaderboard_background, [0, 0])
        if update_score == False:
            f = open("leaderboard.txt", "r")
            text = f.read()
            f.close()
            tab_score = text.split("/")

            for i in range(len(tab_score)):
                tab_score[i]=int(tab_score[i])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leader = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[1]>0:
                    menu = True
                    game = False
                    leaderboard = False
        
        for i in range(len(tab_score)):
            textimage = font.render(str(tab_score[len(tab_score)-1-i]), True, (255,255,255))
            window_surface.blit(textimage, (resolution_x//2+100-(5/100 * resolution_x),resolution_y//18*(i+4)))


        pygame.display.flip()

# closes the pygame window 
pygame.quit()