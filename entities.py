

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
        self.w,self.h = 10,5
        self.x = x
        self.y = y
        self.cx = self.x
        self.cy = self.y
        self.size = size                                        
        self.colorb = color
        self.shooting = False
        self.duration = Duration * 60  #duration defines speed
        self.speed = None #the unitvector.
        self.startvec = (self.x,self.y)
        self.currentvec = (self.cx,self.cy)
        self.destvector = (0,0)
        self.unitvector = (0,0)# speed
        self.tick = 0
        #display
        self.sprite = pygame.image.load("b1.png")
        
    def draw(self,screen):
        
        angle = degrees(atan2(self.unitvector[1],self.unitvector[0]))
        rotated_sprite = pygame.transform.rotate(self.sprite, -angle)  # Negative angle for correct rotation direction
        new_rect = rotated_sprite.get_rect(center=self.currentvec)
        screen.blit(rotated_sprite, new_rect.topleft)
        
    
    def shot(self,charx,chary,mousex,mousey):
        self.x  = charx
        self.y  = chary
        self.cx = charx
        self.cy = chary
        self.xd = mousex
        self.yd = mousey
        self.currentvec = (self.cx,self.cy)
        self.destvector = (float(self.xd),float(self.yd))
        self.unitvector = ((self.destvector[0] - self.currentvec[0])/self.duration,(self.destvector[1] - self.currentvec[1])/self.duration)
        self.shooting = True
        logging.info("Bullet Shot. Unit Vector created")
      
    def move(self):
        self.tick+=1
        if self.tick == self.duration:
            self.shooting = False
        if self.shooting == True:
            if self.currentvec == self.destvector:
                self.shooting = False
            else:
                self.currentvec = (float(self.currentvec[0]+ self.unitvector[0]),float(self.currentvec[1]+self.unitvector[1]))
class gun:
    def __init__(self,ammo = 1000,cooldown = 30):
        self.ammo = ammo
        self.guncooldown = cooldown         
class pistol(gun):
    def __init__(self,ammo = 15, cd = 50):
        super().__init__(ammo,cd)
        
    def shoot(self,px,py,mx,my):
        if self.ammo < 1:
            return
        else:
            b = bullet()
            b.shot(px,py,mx,my)
            self.ammo -=1 
            c =[b]
            return c
class miniGun(gun):
    def __init__(self,ammo = 1500, cd = 5):
        super().__init__(ammo,cd)
        
    def shoot(self,px,py,mx,my):
        accuracy = 1
        mx = mx + r.randint(accuracy-100,100-accuracy)
        my = my + r.randint(accuracy-100,100-accuracy)
        if self.ammo < 1:
            return
        else:
            b = bullet()
            b.shot(px,py,mx,my)
            self.ammo -=1 
            c = [b]
            return c
class shotGun(gun):
    def __init__(self,ammo = 1000, cd = 100,radius = 200):
        super().__init__(ammo,cd)
        self.radius = radius

    def shoot(self,px,py,mx,my):
        accuracy = 1
        mx = mx + r.randint(accuracy-100,100-accuracy)
        my = my + r.randint(accuracy-100,100-accuracy)
        if self.ammo < 1:
            return
        else:
            b = bullet()
            b.shot(px,py,mx,my)
            mx = mx + r.randint(accuracy-100,100-accuracy)
            my = my + r.randint(accuracy-100,100-accuracy)
            b1 = bullet()
            b1.shot(px,py,mx,my)
            mx = mx + r.randint(accuracy-100,100-accuracy)
            my = my + r.randint(accuracy-100,100-accuracy)
            b2 = bullet()
            b2.shot(px,py,mx,my)
            mx = mx + r.randint(accuracy-100,100-accuracy)
            my = my + r.randint(accuracy-100,100-accuracy)
            b3 = bullet()
            b3.shot(px,py,mx,my)
            mx = mx + r.randint(accuracy-100,100-accuracy)
            my = my + r.randint(accuracy-100,100-accuracy)
            b4 = bullet()
            b4.shot(px,py,mx,my)
            mx = mx + r.randint(accuracy-100,100-accuracy)
            my = my + r.randint(accuracy-100,100-accuracy)
            b5 = bullet()
            b5.shot(px,py,mx,my)
            mx = mx + r.randint(accuracy-100,100-accuracy)
            my = my + r.randint(accuracy-100,100-accuracy)
            self.ammo -=1 
            c = [b,b1,b2,b3,b4,b5]
            return c
        
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
        self.weaponry = [miniGun(),pistol(),shotGun()]
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