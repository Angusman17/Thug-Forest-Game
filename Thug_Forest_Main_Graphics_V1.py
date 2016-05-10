# Thug Forest Full Game
# Brandon Henry
# 3/7/16
'''Basic graphics stuff with pygame.'''
import pygame
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

#def draw_creature(screen,x,y):
#    pygame.draw.ellipse(screen, SKIN, [x,y,50,50])
#    pygame.draw.ellipse(screen, WHITE, [x+4,y+10,15,15])
#    pygame.draw.ellipse(screen, WHITE, [x+34,y+10,15,15])
#    pygame.draw.ellipse(screen, BLACK, [x+7,y+15,5,5])
#    pygame.draw.ellipse(screen, BLACK, [x+41,y+15,5,5])
#    pygame.draw.arc(screen, BLACK, [x+19,y+25,15,10], PI, 3*PI/2,2)
#    pygame.draw.arc(screen, BLACK, [x+19,y+25,15,10], 3*PI/2, 2*PI,2)
class Draw_Creature(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0
        self.image = pygame.Surface([width,height])
        self.image.fill(YELLOW)
        self.image.set_colorkey(YELLOW)
        pygame.draw.ellipse(self.image,YELLOW,[self.x,self.y,50,50])
        self.rect = self.image.get_rect()
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
    def draw(self,screen):
        pygame.draw.ellipse(screen, SKIN, [self.x,self.y,50,50])
        pygame.draw.ellipse(screen, WHITE, [self.x+4,self.y+10,15,15])
        pygame.draw.ellipse(screen, WHITE, [self.x+34,self.y+10,15,15])
        pygame.draw.ellipse(screen, BLACK, [self.x+7,self.y+15,5,5])
        pygame.draw.ellipse(screen, BLACK, [self.x+41,self.y+15,5,5])
        pygame.draw.arc(screen, BLACK, [self.x+19,self.y+25,15,10], PI, 3*PI/2,2)
        pygame.draw.arc(screen, BLACK, [self.x+19,self.y+25,15,10], 3*PI/2, 2*PI,2)
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randrange(0,701)
        self.y = random.randrange(-500,-10)
        self.y_change = 1
        self.image = pygame.Surface([35,35])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.ellipse(self.image,WHITE,[self.x,self.y,35,35])
    def move(self):
        self.y += self.y_change
    def draw(self,screen):
        pygame.draw.ellipse(screen, RED, [self.x,self.y,35,35])
        pygame.draw.rect(screen, STEMBROWN, [self.x+13,self.y-13, 7, 14])
        pygame.draw.ellipse(screen, GREEN, [self.x+16,self.y-10,11,15])

pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
y_offset = 0
pygame.display.set_caption('Thug Forest')


done = False
clock = pygame.time.Clock()

fruit_list = []
for i in range(10):
    fruit = Fruit()
    fruit_list.append(fruit)
    
thug_y = 390
thug_y_change = .25

#x_speed = 0
#y_speed = 0

#x_coord = size[0]/2
#y_coord = size[1]/2
score = 0
lives = 3

pygame.mixer.music.load('Thug_Forest_Music(ClearDay_Edit).mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(loops = -1)

thug = Draw_Creature(50,50)
thug.x = 500
thug.y = 350
thug.x_change = 0
thug.y_change = 0
explosion = Thug_Explosion.Explosion()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                thug.x_change = -2
            elif event.key == pygame.K_d:
                thug.x_change = 2
            elif event.key == pygame.K_w:
                thug.y_change = -2
            elif event.key == pygame.K_s:
                thug.y_change = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                thug.x_change = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                thug.y_change = 0
        if thug.x >= 650:
            thug.x_change = -1
        elif thug.x < 650:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    thug.x_change = -2
                elif event.key == pygame.K_d:
                    thug.x_change = 2
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    thug.x_change = 0
        if thug.x <= 0:
            thug.x_change = 1
        if thug.y >= 450:
            thug.y_change = -1
        elif thug.y < 450:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    thug.y_change = -2
                elif event.key == pygame.K_s:
                    thug.y_change = 2
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    thug.y_change = 0
        if thug.y <= 0:
            thug.y_change = 1
        
    thug.x += thug.x_change
    thug.y += thug.y_change
#    hit_list = pygame.sprite.spritecollide(thug,fruit_list, True)

#    pos = pygame.mouse.get_pos()
#    thug.x_change = pos[0]
#    thug.y_change = pos[1]
#    pygame.mouse.set_visible(False)

    for i in range(len(fruit_list)):
        if fruit_list[i].y == 500:
            lives -= 1


    screen.fill(WHITE)
    #Drawing the ground and the sky
    pygame.draw.rect(screen, BROWN, [0,250,700,250])
    pygame.draw.rect(screen, SKY, [0,0,700,250])

    #Drawing clouds for background
    for i in range(0,700,233):
        pygame.draw.ellipse(screen, WHITE, [-25+i,50,200,100])
    
    #Drawing trees for background and their shadows
    for i in range(0,700,100):
        pygame.draw.rect(screen, DBROWN, [50+i,0,50,250])
        pygame.draw.rect(screen, (210,180,110), [50+i,250,50,5])
        pygame.draw.ellipse(screen, DGREEN, [-50+i,-50,250,150])

    #Drawing a bush
    pygame.draw.rect(screen, DBROWN, [202,375,10,25])
    pygame.draw.ellipse(screen, DGREEN, [175,338,50,50])
    pygame.draw.ellipse(screen, DGREEN, [198,345,50,50])
    pygame.draw.ellipse(screen, DGREEN, [162,347,50,50])

    #Drawing a pond
    pygame.draw.ellipse(screen, WATER, [75,400,250,60])
    
    #Drawing another little creature bobbing in the pond
    pygame.draw.ellipse(screen, SKIN, [125,thug_y,50,50])
    pygame.draw.ellipse(screen, WHITE, [129,thug_y+10,15,15])
    pygame.draw.ellipse(screen, WHITE, [159,thug_y+10,15,15])
    pygame.draw.ellipse(screen, BLACK, [132,thug_y+15,5,5])
    pygame.draw.ellipse(screen, BLACK, [166,thug_y+15,5,5])
    pygame.draw.arc(screen, BLACK, [144,thug_y+25,15,10], PI, 3*PI/2,2)
    pygame.draw.arc(screen, BLACK, [144,thug_y+25,15,10], 3*PI/2, 2*PI,2)
    thug_y -= thug_y_change
    if thug_y > 400 or thug_y < 370:
        thug_y_change = thug_y_change * -1
        
    #Makes a spot for the bobbing creature to be behind
    pygame.draw.rect(screen, WATER, [100,415,200,35])

    #Drawing little creatures
#    thug = draw_creature(screen,x_coord,y_coord)
#    thug2 = draw_creature(screen,thug2_x,thug2_y)
    thug.move()
    thug.draw(screen)
    
    #Makes apples that fall from the trees above

    
#    for i in range(len(fruit_list)):
#        pygame.draw.circle(screen, RED, fruit_list[i], 15)
#        pygame.draw.rect(screen, STEMBROWN, [fruit_list[i][0]-2,fruit_list[i][1]-25, 7, 12])
#        pygame.draw.circle(screen, GREEN, [fruit_list[i][0]+7,fruit_list[i][1]-17], 5)
#        fruit_list[i][1] += 1
    for i in range(len(fruit_list)):
        fruit_list[i].draw(screen)
        fruit_list[i].move()
        if fruit_list[i].y > 500:
            y = random.randrange(-500,-10)
            fruit_list[i].y = y
            x = random.randrange(0,700)
            fruit_list[i].x = x

    font1 = pygame.font.SysFont('Calibri',15,True,False)
    text1 = font1.render('Score: ' + str(score),True,WHITE)
    screen.blit(text1, [550,3])
    
    font2 = pygame.font.SysFont('Calibri',15,True,False)
    text2 = font2.render('Lives: ' + str(lives),True,WHITE)
    screen.blit(text2, [550,15])
    
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
