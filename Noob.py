import pygame
from entities import * 
import random as r 
import colors as cc
import colorgentool as genn
from classes import *
pygame.init()


class Environment:
    def __init__(self,screen):
        self.valor = Bot([500,500],20,1,"Retardium",cc.colorlist[11])
        self.dushman = spawner(screen,self.valor) 
        for a in range(0,5):
            self.dushman.spawn(cc.colorlist[5])
        self.score = 0
        self.reward = 0
        self.scoredisplay = Text(((screen.get_width()//2)-70,10),50,cc.colorlist[12],"Score : 0 ",2)
    
    def reset(self,screen):
        self.reward = 0
        self.valor = Bot([500,500],20,1,"Retardium",cc.colorlist[11])
        self.dushman.reset_spawner()
        for a in range(0,5):
            self.dushman.spawn(cc.colorlist[5])
        self.score = 0
        self.scoredisplay.update_text("Score :".format(self.score))
    
    def is_collision(self,):
        for a in self.dushman.enemies:
            distance = ((self.valor.x - a.x) ** 2 + (self.valor.y - a.y) ** 2) ** 0.5
            if distance <= self.valor.radius + a.radius:
                return True
            return False
  
    def step(self,screen,action):#updating environment - implements actions -returns reward or gameover
        self.valor.move(action,screen)   
        for e in self.dushman.enemies:
            m = pygame.mouse.get_pos()
            e.move1(screen,self.valor.x,self.valor.y)
        if self.is_collision():
            self.reward += 1 #change ur reward here
            
        else:
            self.reward = -100 #insta kill 
        return self.reward
        
    def render(self,screen):
        for a in self.dushman.enemies:
            a.draw(screen)
        self.valor.draw(screen)
        self.scoredisplay.update_text("Score: {}".format(self.score))
        self.scoredisplay.draw(screen)
        pass