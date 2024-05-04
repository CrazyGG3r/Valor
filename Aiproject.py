
print("hello")
import pygame
from classes import Text
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
#-=-=-=-

bg = cc.colorlist[0]
movr = False
keyy = None
clock = pygame.time.Clock()
keys_pressed = set()
fps = 60
ti =  0

enemies = []
## Setups
valor = Bot([100,100],20,1,"Retardium",cc.colorlist[11])
spaw = spawner(screen,valor)
botdie = 0
Score = 0
scoredisplay = Text(((screen.get_width()//2)-70,10),50,cc.colorlist[12],"Score : 0 ",2)
n = 0
texts = [scoredisplay]
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
                    
        if ti % spaw.speed*fps == 0:
            spaw.spawn(r.choice(newcolor))
            enemies = spaw.enemies
          
        Score+=1
        sc = "Score : " + str(Score)
        scoredisplay.update_text(sc)
        for e in enemies:
            m = pygame.mouse.get_pos()
            if e :
                if ti%r.randint(1,15) ==0:
                    e.move1(screen,valor.x,valor.y)
                e.draw(screen)
                if (valor.is_collision(e)):
                    botdie = 1
        for a in texts:
            a.draw(screen)
        valor.move(r.randint(0,100),screen)
        
        valor.draw(screen)  
        pygame.display.flip()
    print("Bot dead")
    pygame.display.flip()
