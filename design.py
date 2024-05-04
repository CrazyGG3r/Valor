
import pygame
pygame.init()
import random as r 
import colors as c
class Background:
    def __init__(self,window,pop= 100,style = 1):
        self.squares = []
        self.squares = []
        self.population = pop
        self.maxsize = 150
        self.choice = [-1,1]
        self.style = style
        self.reset_bg(window)
            
    def reset_bg(self,window):
        if self.style ==1:
            self.reset_bg1(window)
        if self.style ==2:
            self.reset_bg2(window)
        if self.style ==3:
            self.reset_bg3(window)
    
    def reset_bg2(self,window):
        if self.squares:
            for a in range(self.population):
                self.squares.pop()
        for a in range(self.population):
            neon = r.randint(10,20)
            coo = (r.randint(0,window.get_width()),r.randint(0,window.get_height()))
            coloro = (0,neon,neon)
            raa = r.randint(0,10)/1000
            raa = r.choice(self.choice) * raa
            self.squares.append(Square(coo,r.randint(30,self.maxsize),coloro,raa,1))
            
    def reset_bg3(self,window):
        if self.squares:
            for a in range(self.population):
                self.squares.pop()
        for a in range(self.population):
            neon = r.randint(30,60)
            coo = (r.randint(0,window.get_width()),r.randint(0,window.get_height()))
            coloro = (0,neon,neon)
            raa = r.randint(0,100)/200
            self.squares.append(Square(coo,r.randint(5,self.maxsize-100),coloro,raa))
            
    def reset_bg1(self,window):
        if self.squares:
            for a in range(self.population):
                self.squares.pop()
        newlist = c.colorlist[2:8]
        for a in range(self.population):
            # neon = r.randint(30,90)
            coo = (r.randint(0,window.get_width()),r.randint(0,window.get_height()))
            coloro = r.choice(newlist)
            raa = r.randint(0,100)/1000
            raa = r.choice(self.choice) * raa
            self.squares.append(Square(coo,r.randint(10,self.maxsize-50),coloro,raa))
            
    def draw(self,window):
        window.fill(c.colorlist[0])
        for a in self.squares:
            a.move(window)
            a.draw(window)

class Square:
    def __init__(self,coords,l,color,ra):
        self.l = l
        self.color = color
        self.coords = coords
        self.x = self.coords[0]
        self.y = self.coords[1]
        # self.angle = r.randint(0,360)
        self.angle = 100
        self.surface = pygame.Surface((self.l,self.l),pygame.SRCALPHA)
        self.surface.set_alpha(10)
        self.RotationalSpeed = ra
        speed = 10
        
        self.directionVector = (r.randint(-speed,speed)/r.randint(10,100),r.randint(speed,speed)/r.randint(10,100))
        print(self.directionVector)
        
    def move(self,screen):
        self.x +=  self.directionVector[0]
        self.y +=  self.directionVector[1]
        self.coords = (self.x,self.y)
        if self.x >= screen.get_width():
            self.directionVector = (self.directionVector[0]*-1,self.directionVector[1])
            
        if self.x <= 0:
            self.directionVector = (self.directionVector[0]*-1,self.directionVector[1])
        
        if self.y <= 0 :
            self.directionVector = (self.directionVector[0],self.directionVector[1]*-1)
        
        if self.y >= screen.get_height():
            self.directionVector = (self.directionVector[0],self.directionVector[1]*-1)
        
        
        pass
    def draw(self, screen):  
        square_surface = pygame.Surface((self.l, self.l), pygame.SRCALPHA)
        square_surface.fill(self.color)
        rotated_surface = pygame.transform.rotate(square_surface, self.angle)
        rect = rotated_surface.get_rect(center=self.coords)
        screen.blit(rotated_surface, rect.topleft)
        self.angle += self.RotationalSpeed  
    def updateCoord(self,coords):
        self.coords = coords
    def rotate(self,):
        pass
        


class Trailsquare:
    def __init__(self,size,):
        self.size = size
        self.trail = {}
        self.maxsize = 20
        self.createTrail()
    
    def update(self,mouse):
        keeys = list(self.trail.keys())
        previous = mouse
        for a in keeys:
            curr = self.trail[a]
            self.trail[a] = previous
            previous = curr
            
    def resetTrail(self):
        d = {}
        self.trail = d
        self.createTrail()
                
    def createTrail(self):
        choice = [-1.1]
        newlist = c.colorlist[3:11]
        for a in range(self.size):
            coo = (0,0)
            
            coloro = r.choice(newlist)
            raa = r.randint(0,100)/1000
            raa = r.choice(choice) * raa
            
            self.trail[Square(coo,r.randint(0,self.maxsize),coloro,raa)] = (0,0)

    def draw(self, screen):
        for a in self.trail:
            a.updateCoord(self.trail[a])
            a.draw(screen)