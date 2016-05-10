import pygame
import random
my_list = []
APPLEBITS = (250,248,222)

class Rectangle():
    def __init__(self):
        self.x = random.randrange(345,356)
        self.y = random.randrange(245,256)
        self.width = random.randrange(5,10)
        self.height = random.randrange(5,10)
        self.x_change = random.randrange(-1,1)
        self.y_change = -5
#        self.r = random.randrange(0,255)
#        self.g = random.randrange(0,255)
#        self.b = random.randrange(0,255)
    def draw(self,screen,color):
        pygame.draw.rect(screen,color,[self.x,self.y,self.width,self.height])
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.y_change += .1

#Creates a class that provides ellipses of random size and color.
class Ellipse(Rectangle):
    def draw(self,screen,color):
        pygame.draw.ellipse(screen,color,[self.x,self.y,self.width,self.height])
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.y_change += .1

class Explosion():
    def __init__(self):
        self.my_list = []
        self.counter = 0
    def explode(self):
        for i in range(5):
            my_object = Rectangle()
            my_list.append(my_object)
        for i in range(5):
            my_object2 = Ellipse()
            my_list.append(my_object2)
    def update(self,screen):
        if self.counter < 500000:
            if len(my_list) >= 5:
                for i in range(10):
                    my_list[i].draw(screen,APPLEBITS)
                    my_list[i].move()
                    self.counter += 1
