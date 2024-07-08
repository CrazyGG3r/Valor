

import random as r
from math import atan2, degrees, dist, sqrt
import pygame
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
pygame.init()

#ENTITIES DEFINED:
#BALL

class   Ball:
    def __init__(self,coords, radius, speed, name, color,):
        self.fnt = pygame.font.Font(None, 20)
        self.x = int(coords[0])
        self.y = int(coords[1])
        self.radius = int(radius)
        self.tname = str(name)
        self.name = self.fnt.render(self.tname, True, (255, 255, 255))
        self.speed = int(speed)
        self.color = tuple(color)
        
    def bname(self):
       self.name = self.fnt.render(self.tname, True, (255, 255, 255))
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        screen.blit(self.name,((self.x-self.radius),(self.y + self.radius +10)))
                
   
            
    def updatewholeball(self,data):
       self.tname = str(data['name'])
       self.bname()
       self.x = data['x']
       self.y = data['y']
       self.color = data['color']
    def to_dict(self):
        return {'x': self.x, 'y': self.y, 'radius': self.radius}
    
    def check_pos(self,screen):
        if self.x>screen.get_width()+self.radius:
            self.x = 0 - self.radius
        if self.x<0-self.radius:
            self.x = screen.get_width() + self.radius
        if self.y>screen.get_height()+ self.radius:
            self.y = 0-self.radius
        if self.y<0-self.radius:
            self.y = screen.get_height() + self.radius                              
class bullet:
    def __init__(self,color = (255,255,255),x = 0,y = 0, Duration = 1, size = 5):
        pass
        
    def draw(self,screen):
        pass
        
    
    def shot(self,charx,chary,mousex,mousey):
        pass
      
    def move(self):
        pass
    
class gun:
    def __init__(self,ammo = 1000,cooldown = 30):
        pass   
    
class pistol(gun):
    def __init__(self,ammo = 15, cd = 50):
        super().__init__(ammo,cd)
        pass
        
    def shoot(self,px,py,mx,my):
        pass

        
class Bot(Ball):
    def __init__(self,coords, radius, speed, name, color ,screen=None):
        super().__init__(coords, radius, speed, name, color,)
        self.lives = 1
        self.prev = 0
        self.MovVector = [0,0]
        self.movelimit = 60 * 1
        self.decayRate = self.speed/self.movelimit
    def resetMov(self):
        self.MovVector = [0,0]
        
    def decayVector(self):
        if self.MovVector[0] > 0:
            self.MovVector[0] -= self.decayRate
        if self.MovVector[1] > 0:
            self.MovVector[1] -= self.decayRate
        if self.MovVector[0] < 0:
            self.MovVector[0] += self.decayRate
        if self.MovVector[1] < 0:
            self.MovVector[1] += self.decayRate
            
    def move(self,event,screen,client = None):
         self.x += self.MovVector[0]
         self.y += self.MovVector[1]
         self.decayVector()
         if event == 0:
             self.MovVector[0] = -self.speed #left
         if event == 1:
             self.MovVector[0] = +self.speed #right
         if event == 2:
             self.MovVector[1] = -self.speed #up
         if event == 3:
             self.MovVector[1] = self.speed  #down
         self.check_pos(screen)
         
    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        screen.blit(self.name,((self.x-self.radius),(self.y + self.radius +10)))
    def is_collision(self, ball):
        distance = ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5
        if distance <= self.radius + ball.radius:
            return True
        return False

class person(Ball):#is a ball for now
    def __init__(self,coords, radius, speed, name, color ,ammo ,health,lives,screen):
        super().__init__(coords, radius, speed, name, color,)
        self.maxhp = health
        self.currenthp = health
        self.lives = lives
        self.weaponry = [pistol()]
        self.currgun = 0
        self.gun = self.weaponry[self.currgun]
        self.bullets = []
        self.prev = 0
        self.MovVector = [0,0]
        self.movelimit = 60 * 1
        self.decayRate = self.speed/self.movelimit
        
    def resetMov(self):
        self.MovVector = [0,0]
        
    def decayVector(self):
        print(self.MovVector)
        if self.MovVector[0] > 0:
            self.MovVector[0] -= self.decayRate
        if self.MovVector[1] > 0:
            self.MovVector[1] -= self.decayRate
        if self.MovVector[0] < 0:
            self.MovVector[0] += self.decayRate
        if self.MovVector[1] < 0:
            self.MovVector[1] += self.decayRate
        
    def move(self,event,screen,client = None):
         self.x += self.MovVector[0]
         self.y += self.MovVector[1]
         self.decayVector()
         if event == pygame.K_LEFT:
             self.MovVector[0] = -self.speed
         if event == pygame.K_RIGHT:
             self.MovVector[0] = +self.speed
         if event == pygame.K_UP:
             self.MovVector[1] = -self.speed
         if event== pygame.K_DOWN:
             self.MovVector[1] = self.speed
         self.check_pos(screen)
         
        
    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        screen.blit(self.name,((self.x-self.radius),(self.y + self.radius +10)))
        barwidth = 40
        barheight = 6
        healthpercent = self.currenthp/self.maxhp
        reed = 0
        green = 255
        if healthpercent < 0.4:
            reed = min(((reed + 5),255))
            green = max(((green - 5),0))
        else:
            green = 255
            reed = 0
        barcolor = (reed,green,0)
        currentfullhealthbarwidth =  healthpercent* barwidth
        o = 10
        currentfullhealthbarheight = barheight - 2
        bgrect = pygame.Rect((self.x - self.radius),(self.y-(self.radius + o+1)),barwidth,barheight)
        pygame.draw.rect(screen,(230,230,230),bgrect)      
        currbgrect = pygame.Rect((self.x - self.radius),(self.y-(self.radius + o)),currentfullhealthbarwidth,currentfullhealthbarheight)
        pygame.draw.rect(screen,barcolor,currbgrect)
    
    
    def decision(self,key,screen,ti):
        
        if key == pygame.K_SPACE and (ti - self.prev)>= self.gun.guncooldown:
            self.prev = ti
            logging.info("Ammo = "+str(self.gun.ammo))
            self.trigger()
      
        else:
            self.move(key,screen)

    def trigger(self):
            m = pygame.mouse.get_pos()
            if self.gun.ammo >0:
                logging.info("One Bullet Created")
                bull = self.gun.shoot(self.x,self.y,m[0],m[1])
                for a in bull:
                       self.bullets.append(a)
                logging.info("Totalbullets: " + str(len(self.bullets)))
            else:
                logging.info("Totalbullets: shot" + str(len(self.bullets)))
                return  
    
    def changeWeapon(self):
        self.currgun += 1
        if self.currgun >= len(self.weaponry):
            self.currgun = 0
        self.gun = self.weaponry[self.currgun]

         
class enemy(Ball):#is a ball for now
    def __init__(self,coords, radius, speed, name, color ,health):
        super().__init__(coords, radius, speed, name, color)
        self.maxhp = health
        self.currenthp = health
        self.speed = speed
        self.target = []
        self.movVector = [0,0]
        self.frame  = 60
        self.timetoReach = 3
    def move1(self,screen,px,py):
        self.target = [px,py]
        self.x += self.movVector[0]
        self.y += self.movVector[1]
        
        diff_vec = [self.target[0] - self.x,self.target[1] - self.y]
        distance = sqrt(pow(diff_vec[0],2) + pow(diff_vec[1],2))
        direction = [diff_vec[0]/distance,diff_vec[1]/distance]
        
        self.movVector[0] = direction[0] * self.speed
        self.movVector[1] = direction[1] * self.speed
        
            
    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        screen.blit(self.name,((self.x-self.radius),(self.y + self.radius +10)))
        
    def draw_withbar(self,screen):
            pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
            screen.blit(self.name,((self.x-self.radius),(self.y + self.radius +10)))
            barwidth = 40
            barheight = 6
            healthpercent = self.currenthp/self.maxhp
            reed = 0
            green = 255
            if healthpercent < 0.4:
                reed = min(((reed + 5),255))
                green = max(((green - 5),0))
            else:
                green = 255
                reed = 0
            barcolor = (reed,green,0)
            currentfullhealthbarwidth =  healthpercent* barwidth
            o = 10
            currentfullhealthbarheight = barheight - 2
            bgrect = pygame.Rect((self.x - self.radius),(self.y-(self.radius + o+1)),barwidth,barheight)
            pygame.draw.rect(screen,(230,230,230),bgrect)      
            currbgrect = pygame.Rect((self.x - self.radius),(self.y-(self.radius + o)),currentfullhealthbarwidth,currentfullhealthbarheight)
            pygame.draw.rect(screen,barcolor,currbgrect)
            
class spawner:
    def __init__(self,screen,target):
        self.maxx = screen.get_width()
        self.maxy = screen.get_height()
        self.speed = 60
        self.limit = 5
        self.enemies = []
        self.target = target #(x,y) of aggro
    
    def reset_spawner(self):
        self.enemies.clear()
        
    def spawn(self,colors):
        ax = r.randint(-50,self.maxx + 50)
        ay = r.randint(-50,self.maxy + 50)
        ra = 20
        col = colors
        if len(self.enemies) == self.limit:
            return
        en = enemy((ax,ay),ra,3,"bob",col,100)
        self.enemies.append(en)    