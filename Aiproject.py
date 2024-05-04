
print("hello")
import pygame
from entities import * 
import random as r 
import colors as cc
import colorgentool as genn
pygame.init()
i = pygame.display.Info()
width,height = 1280,720
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
 
#settup colors

color1 = cc.colorlist[12]
color2 = (0,0,0)
newcolor = genn.diffuser(color1,color1)

col = r.choice(newcolor)
p1 = person((width//2,height//2),20,1,'test',col,100,100,5,screen)

bg = cc.colorlist[0]
movr = False
keyy = None
clock = pygame.time.Clock()
keys_pressed = set()
bullets= []
btick = 0
fps = 60
ti =  0
players = [p1]
enemies = []
## Ai
valor = Bot([100,100],20,1,"Retardium",cc.colorlist[11])

spaw = spawner(screen,valor) 

botdie = 0
while True:
    
    while botdie ==0 :
        screen.fill(bg)
        clock.tick(fps)
        ti +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                keys_pressed.add(event.key)
            if event.type == pygame.KEYUP:
               keys_pressed.discard(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    print("up")
                    p1.changeWeapon()
        for a in keys_pressed:
            for p in players:
                p.decision(a,screen,ti)
        if ti % spaw.speed*fps == 0:
            spaw.spawn(r.choice(newcolor))
            enemies = spaw.enemies
        
        for e in enemies:
            m = pygame.mouse.get_pos()
            if e :
                if ti%r.randint(1,15) ==0:
                    e.move1(screen,valor.x,valor.y)
                e.draw(screen)
                if (valor.is_collision(e)):
                    botdie = 1
        valor.move(r.randint(0,100),screen)
        
        valor.draw(screen)  
        pygame.display.flip()
    print("Bot dead")
    pygame.display.flip()
