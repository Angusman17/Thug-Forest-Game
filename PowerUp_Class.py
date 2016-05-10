# PowerUp Class
# Brandon Henry
# 3/34/16
'''Class used to handle power ups in Thug Game.'''
import pygame
import random

class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randrange(50,951)
        self.y = random.randrange(50,951)
        self.image = pygame.image.load('Speed.png')
        self.image = pygame.transform.scale(self.image, (50,50))
    def draw(self,screen):
        screen.blit(self.image, [self.x,self.y])
