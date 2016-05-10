# Thug Forest Full Game
# Brandon Henry
# 3/7/16
'''Full game of Thug Forest(Name for now).  Game in which your main goal is to
catch falling objects before they reach the bottom of the screen.'''
import pygame
import time
import random
import Thug_Explosion

PI = 3.141592653
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (214,184,114)
SKY = (80,250,250)
DBROWN = (145,90,26)
DGREEN = (1,102,3)
SKIN = (250,241,212)
PINK = (250,177,177)
WATER = (79,178,240)
STEMBROWN = (209,172,92)
APPLEBITS = (250,248,222)

class Draw_Player(pygame.sprite.Sprite):
    '''Class for creating and displaying the player's character.'''
    def __init__(self,width,height):
        super().__init__()
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0
        self.image = pygame.image.load('Game_Character.png')
        self.image = pygame.transform.scale(self.image,(300,300))
        self.rect = self.image.get_rect()
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
    def draw(self,screen):
        screen.blit(self.image, [self.x-135,self.y-100])

class Draw_Bird(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.x = random.randrange(0,950)
        self.y = random.randrange(100,600)
        self.x_change = -2
        self.images1 = []
        self.images2 = []
        self.images1.append(pygame.transform.scale(pygame.image.load('Bird.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Bird2.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Bird3.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Bird4.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Bird5.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Bird6.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Bird7.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Bird_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Bird2_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Bird3_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Bird4_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Bird5_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Bird6_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Bird7_1.png'), (150,150)))
        self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
        self.rect = self.image1.get_rect()
    def update(self):
        self.index += 1
        if self.index >= len(self.images1):
            self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
    def move(self):
        self.x += self.x_change
        if self.x >= 1050:
            self.x_change *= -1
            self.y -= 150
        elif self.x <= -150:
            self.x_change *= -1
            self.y -= 150
        if self.y <= 100:
            self.y = random.randrange(100,600)
    def draw(self,screen):
        if self.x_change == -2:
            screen.blit(self.image1, [self.x,self.y])
        elif self.x_change == 2:
            screen.blit(self.image2, [self.x,self.y])

class Draw_Dragon(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.x = random.randrange(0,950)
        self.y = random.randrange(100,600)
        self.x_change = -2
        self.images1 = []
        self.images2 = []
        self.images1.append(pygame.transform.scale(pygame.image.load('Dragon.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Dragon2.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Dragon3.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Dragon4.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Dragon5.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Dragon6.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Dragon7.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Dragon_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Dragon2_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Dragon3_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Dragon4_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Dragon5_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Dragon6_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Dragon7_1.png'), (150,150)))
        self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
        self.rect = self.image1.get_rect()
    def update(self):
        self.index += 1
        if self.index >= len(self.images1):
            self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
    def move(self):
        self.x += self.x_change
        if self.x >= 1050:
            self.x_change *= -1
            self.y -= 150
        elif self.x <= -150:
            self.x_change *= -1
            self.y -= 150
        if self.y <= 100:
            self.y = random.randrange(100,600)
    def draw(self,screen):
        if self.x_change == -2:
            screen.blit(self.image1, [self.x,self.y])
        elif self.x_change == 2:
            screen.blit(self.image2, [self.x,self.y])

class Draw_Whale(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.x = random.randrange(0,950)
        self.y = random.randrange(100,600)
        self.x_change = -2
        self.images1 = []
        self.images2 = []
        self.images1.append(pygame.transform.scale(pygame.image.load('FlyingWhale.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('FlyingWhale2.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('FlyingWhale3.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('FlyingWhale4.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('FlyingWhale5.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('FlyingWhale6.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('FlyingWhale7.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('FlyingWhale_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('FlyingWhale2_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('FlyingWhale3_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('FlyingWhale4_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('FlyingWhale5_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('FlyingWhale6_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('FlyingWhale7_1.png'), (150,150)))
        self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
        self.rect = self.image1.get_rect()
    def update(self):
        self.index += 1
        if self.index >= len(self.images1):
            self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
    def move(self):
        self.x += self.x_change
        if self.x >= 1050:
            self.x_change *= -1
            self.y -= 150
        elif self.x <= -150:
            self.x_change *= -1
            self.y -= 150
        if self.y <= 100:
            self.y = random.randrange(100,600)
    def draw(self,screen):
        if self.x_change == -2:
            screen.blit(self.image1, [self.x,self.y])
        elif self.x_change == 2:
            screen.blit(self.image2, [self.x,self.y])

class Draw_IceMonster(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.x = random.randrange(0,950)
        self.y = random.randrange(100,600)
        self.x_change = -2
        self.images1 = []
        self.images2 = []
        self.images1.append(pygame.transform.scale(pygame.image.load('IceMonster.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('IceMonster2.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('IceMonster3.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('IceMonster4.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('IceMonster5.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('IceMonster6.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('IceMonster7.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('IceMonster_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('IceMonster2_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('IceMonster3_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('IceMonster4_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('IceMonster5_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('IceMonster6_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('IceMonster7_1.png'), (150,150)))
        self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
        self.rect = self.image1.get_rect()
    def update(self):
        self.index += 1
        if self.index >= len(self.images1):
            self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
    def move(self):
        self.x += self.x_change
        if self.x >= 1050:
            self.x_change *= -1
            self.y -= 150
        elif self.x <= -150:
            self.x_change *= -1
            self.y -= 150
        if self.y <= 100:
            self.y = random.randrange(100,600)
    def draw(self,screen):
        if self.x_change == -2:
            screen.blit(self.image1, [self.x,self.y])
        elif self.x_change == 2:
            screen.blit(self.image2, [self.x,self.y])

class Draw_Turtle(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.x = random.randrange(0,950)
        self.y = random.randrange(100,600)
        self.x_change = -2
        self.images1 = []
        self.images2 = []
        self.images1.append(pygame.transform.scale(pygame.image.load('Turtle.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Turtle2.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Turtle3.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Turtle4.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Turtle5.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Turtle6.png'), (150,150)))
        self.images1.append(pygame.transform.scale(pygame.image.load('Turtle7.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Turtle_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Turtle2_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Turtle3_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Turtle4_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Turtle5_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Turtle6_1.png'), (150,150)))
        self.images2.append(pygame.transform.scale(pygame.image.load('Turtle7_1.png'), (150,150)))
        self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
        self.rect = self.image1.get_rect()
    def update(self):
        self.index += 1
        if self.index >= len(self.images1):
            self.index = 0
        self.image1 = self.images1[self.index]
        self.image2 = self.images2[self.index]
    def move(self):
        self.x += self.x_change
        if self.x >= 1050:
            self.x_change *= -1
            self.y -= 150
        elif self.x <= -150:
            self.x_change *= -1
            self.y -= 150
        if self.y <= 100:
            self.y = random.randrange(100,600)
    def draw(self,screen):
        if self.x_change == -2:
            screen.blit(self.image1, [self.x,self.y])
        elif self.x_change == 2:
            screen.blit(self.image2, [self.x,self.y])


class Fruit(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.x = random.randrange(0,950)
        self.y = random.randrange(-1000,-10)
        self.y_change = 1.0
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
    def move(self):
        self.y += self.y_change
    def draw(self,screen):
        screen.blit(self.image, [self.x,self.y])
        
class Power(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.x = random.randrange(100,901)
        self.y = random.randrange(100,901)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(200,150))
        self.rect = self.image.get_rect()
    def draw(self,screen):
        screen.blit(self.image, [self.x,self.y])

class Buttons(pygame.sprite.Sprite):
    def __init__(self,image,image1,image2,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(250,250))
        self.image1 = pygame.image.load(image1)
        self.image1 = pygame.transform.scale(self.image1,(250,250))
        self.image2 = pygame.image.load(image2)
        self.image2 = pygame.transform.scale(self.image2,(250,250))
        self.rect = self.image.get_rect()
    def update(self):
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1] 
        if self.x <= mouse_x <= self.x + 250 and self.y + 90 <= mouse_y <= self.y + 140:
            self.image = self.image2
        else:
            self.image = self.image1
    def draw(self,screen):
        screen.blit(self.image, [self.x,self.y])


def Gamemodes():
    if play.x <= mouse_x <= play.x + 250 and play.y + 50 <= mouse_y <= play.y + 25:
            return 1
    elif howto.x <= mouse_x <= howto.x + 250 and howto.y <= mouse_y <= howto.y + 25:
            return 1
    else:
        return 0
def fruit_add(image):
    for i in range(10):
        fruit = Fruit(image)
        fruit_list.add(fruit)
def fruit_add2(image):
    for i in range(3):
        fruit = Fruit(image)
        fruit_list2.add(fruit)
        

pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode([screen_width,screen_height])
y_offset = 0
pygame.display.set_caption('Thug Forest')

done = False
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

fruit_list = pygame.sprite.Group()
fruit_list2 = pygame.sprite.Group()

score = 0
lives = 3

seconds = 60
milliseconds = 0

pygame.mixer.music.load('Thug_Forest_Music(ClearDay_Edit).mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(loops = -1)

thug = Draw_Player(50,50)
bird = Draw_Bird(25,25)
dragon = Draw_Dragon(25,25)
whale = Draw_Whale(25,25)
ice = Draw_IceMonster(25,25)
turtle = Draw_Turtle(25,25)
thug.x = 500
thug.y = 350
thug.x_change = 0
thug.y_change = 0
#explosion = Thug_Explosion.Explosion()
Background1 = pygame.image.load('Background1.png')
Background2 = pygame.image.load('Background2.png')
Background3 = pygame.image.load('Background3.jpeg')
Background4 = pygame.image.load('Background4.png')
Background5 = pygame.image.load('Background5.jpeg')
bomb = Power('Bomb.png')
bomb_count = 0
speed = Power('Speed.png')
speed_count = 0
clock_power = Power('Clock.png')
life = Power('Life.png')
timer = 0
level = 1
pause = False
gamemode = 0
play = Buttons('PlayButton1.png','PlayButton1.png',
               'PlayButton2.png',350,250)
howto = Buttons('HowToButton1.png','HowToButton1.png',
                'HowToButton2.png',350,350)

while not done:
    print(gamemode)
    if gamemode == 0:
        fruit_add2('Apple.png')
        fruit_add2('DragonFruit.png')
        fruit_add2('Coconut.png')
        fruit_add2('SnowBerries.png')
        fruit_add2('Meteorite.png')
        while gamemode == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamemode = 1
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    gamemode = Gamemodes()

            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1] 
            screen.fill(APPLEBITS)
            for fruit in fruit_list2:
                fruit.draw(screen)
                fruit.move()
                if fruit.y > 1000:
                    y = random.randrange(-500,-10)
                    fruit.y = y
                    x = random.randrange(0,950)
                    fruit.x = x
            play.update()
            play.draw(screen)
            howto.update()
            howto.draw(screen)

            pygame.display.flip()
        
            
    elif gamemode == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.USEREVENT:
                    time -= 1
                    text = str(time).rjust(3)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        thug.x_change = -3
                    elif event.key == pygame.K_d:
                        thug.x_change = 3
                    elif event.key == pygame.K_w:
                        thug.y_change = -3
                    elif event.key == pygame.K_s:
                        thug.y_change = 3
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        thug.x_change = 0
                    elif event.key == pygame.K_w or event.key == pygame.K_s:
                        thug.y_change = 0
                if thug.x >= 950:
                    thug.x = 935
                elif thug.x < 950:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            thug.x_change = -3
                        elif event.key == pygame.K_d:
                            thug.x_change = 3
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_a or event.key == pygame.K_d:
                            thug.x_change = 0
                #Work on potential pause function
                '''elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        pause = False
            while pause == False:
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_p:
                            Pause = True'''
                    
                        
                if thug.x <= 0:
                    thug.x = 15
                if thug.y >= 950:
                    thug.y = 935
                elif thug.y < 950:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            thug.y_change = -3
                        elif event.key == pygame.K_s:
                            thug.y_change = 3
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            thug.y_change = 0
                if thug.y <= 0:
                    thug.y = 15
                
            thug.x += thug.x_change
            thug.y += thug.y_change
            if 25 <= score <= 49:
                for fruit in fruit_list:
                    fruit.y_change = 1.5
            if 50 <= score <= 99:
                for fruit in fruit_list:
                    fruit.y_change = 2.0
            if 100 <= score <= 199:
                for fruit in fruit_list:
                    fruit.y_change = 2.5
            if 200 <= score:
                for fruit in fruit_list:
                    fruit.y_change = 2.5

            #Depending on the speed of the fruits, the y coordinate that they get reset
            #to the top at will change slightly.
            for fruit in fruit_list:
                if fruit.y_change == 1.0:
                    if fruit.y >= 1000:
                        lives -= 1
                elif fruit.y_change == 1.5:
                    if fruit.y >= 999:
                        lives -= 1
                elif fruit.y_change == 2.0:
                    if fruit.y >= 999:
                        lives -= 1
                elif fruit.y_change == 2.5:
                    if fruit.y >= 998:
                        lives -= 1
                #I'm using this code to handle collisions
                if thug.y - 35 <= fruit.y <= thug.y + 40 and thug.x - 35 <= fruit.x <= thug.x + 40:
                    score += 1
                    y = random.randrange(-500,-10)
                    fruit.y = y
                    x = random.randrange(0,950)
                    fruit.x = x
                if 0 <= score <= 24:
                    if bird.y <= fruit.y <= bird.y + 70 and bird.x <= fruit.x <= bird.x + 100:
                        score -= 1
                        y = random.randrange(-500,-10)
                        fruit.y = y
                        x = random.randrange(0,950)
                        fruit.x = x
                if 25 <= score <= 49:
                    if dragon.y <= fruit.y <= dragon.y + 70 and dragon.x <= fruit.x <= dragon.x + 100:
                        score -= 1
                        y = random.randrange(-500,-10)
                        fruit.y = y
                        x = random.randrange(0,950)
                        fruit.x = x
                if 50 <= score <= 99:
                    if whale.y <= fruit.y <= whale.y + 70 and whale.x <= fruit.x <= whale.x + 100:
                        score -= 1
                        y = random.randrange(-500,-10)
                        fruit.y = y
                        x = random.randrange(0,950)
                        fruit.x = x
                if 100 <= score <= 199:
                    if ice.y <= fruit.y <= ice.y + 70 and ice.x <= fruit.x <= ice.x + 100:
                        score -= 1
                        y = random.randrange(-500,-10)
                        fruit.y = y
                        x = random.randrange(0,950)
                        fruit.x = x
                if 200 <= score:
                    if turtle.y <= fruit.y <= turtle.y + 70 and turtle.x <= fruit.x <= turtle.x + 100:
                        score -= 1
                        y = random.randrange(-500,-10)
                        fruit.y = y
                        x = random.randrange(0,950)
                        fruit.x = x
            if thug.y - 35 <= bomb.y <= thug.y + 40 and thug.x - 35 <= bomb.y <= thug.x + 40:
                bomb_count += 1
            #Handles the timer for the game
            if milliseconds > 1000:
                seconds -= 1
                milliseconds -= 1000
            milliseconds += clock.tick_busy_loop(60)

            if lives == 0:
                gamemode = 2

                                                       
            screen.fill(WHITE)
                                            
            #Changes the levels and enemies based on the score
            if 0 <= score <= 24:
                screen.blit(Background1, [0,0])
                bird.update()
                bird.move()
                bird.draw(screen)
            elif 25 <= score <= 49:
                screen.blit(Background2, [0,0])
                dragon.update()                      
                dragon.move()
                dragon.draw(screen)
            elif 50 <= score <= 99:
                screen.blit(Background3, [0,0])
                whale.update()
                whale.move()
                whale.draw(screen)
            elif 100 <= score <= 199:
                screen.blit(Background4, [0,0])
                ice.update()                                      
                ice.move()
                ice.draw(screen)
            elif score >= 200:
                turtle.update()
                turtle.move()
                turtle.draw(screen)
                screen.blit(Background5, [0,0])
            #Resets the timer with each new level
            if score == 25:
                seconds = 60
                level = 2
            elif score == 50:
                seconds = 60
                level = 3
            elif score == 100:
                seconds = 60
                level = 4
            elif score == 200:
                seconds = 60
                level = 5

            if level == 1:
                fruit_add('Apple.png')
                level = 0
            elif level == 2:
                score += 1
                fruit_list = pygame.sprite.Group()
                fruit_add('DragonFruit.png')
                level = 0
            elif level == 3:
                score += 1
                fruit_list = pygame.sprite.Group()
                fruit_add('Coconut.png')
                level = 0
            elif level == 4:
                score += 1
                fruit_list = pygame.sprite.Group()
                fruit_add('SnowBerries.png')
                level = 0
            elif level == 5:
                score += 1
                fruit_list = pygame.sprite.Group()
                fruit_add('Meteorite.png')
                level = 0

            #Drawing player
            thug.move()
            thug.draw(screen)
            
            #Makes apples that fall from the trees above
            timer += 1
            for fruit in fruit_list:
                fruit.draw(screen)
                fruit.move()
                if fruit.y > 1000:
                    y = random.randrange(-500,-10)
                    fruit.y = y
                    x = random.randrange(0,950)
                    fruit.x = x

            #Displays powerups on the screen randomly
            '''bomb.draw(screen)
            speed.draw(screen)
            clock_power.draw(screen)
            life.draw(screen)'''
            
            #Displays various things on screen, like lives, time, score, etc.
            font1 = pygame.font.SysFont('Comic Sans MS',15,True,False)
            text1 = font1.render('Score: ' + str(score),True,WHITE)
            screen.blit(text1, [25,3])
            
            font2 = pygame.font.SysFont('Comic Sans MS',15,True,False)
            text2 = font2.render('Lives: ' + str(lives),True,WHITE)
            screen.blit(text2, [25,18])

            font3 = pygame.font.SysFont('Comic Sans MS',15,True,False)
            text3 = font3.render('Time: ' + str(seconds),True,WHITE)
            screen.blit(text3, [25,33])

            font4 = pygame.font.SysFont('Comic Sans MS',15,True,False)
            text4 = font4.render('Bombs: ' + str(bomb_count),True,WHITE)
            screen.blit(text4, [25, 48])
            
            pygame.display.flip()

    elif gamemode == 2:
        while gamemode == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamemode = 1
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    gamemode = Gamemodes()
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1] 
            screen.fill(APPLEBITS)
            for fruit in fruit_list:
                fruit.draw(screen)
                fruit.move()
                if fruit.y > 1000:
                    y = random.randrange(-500,-10)
                    fruit.y = y
                    x = random.randrange(0,950)
                    fruit.x = x
            play.update()
            play.draw(screen)
            howto.update()
            howto.draw(screen)
pygame.quit()
