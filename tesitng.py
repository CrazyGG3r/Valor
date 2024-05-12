import pygame 
from Noob import Environment,Agent
import design as d
import colorgentool as genn
import colors as cc
import random as r

pygame.init()

i = pygame.display.Info()
width,height = 1280,720
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)

color1 = cc.colorlist[12]
color2 = cc.colorlist[10]
newcolor = genn.diffuser(color1,color1)
col = r.choice(newcolor)

bg = cc.colorlist[0]
movr = False
keyy = None
clock = pygame.time.Clock()
keys_pressed = set()
fps = 60
ti =  0

bgg = d.Background(screen,12,1)
tra = d.Trailsquare(5)
Env = Environment(screen)

ISIagent = Agent(100,5)

while True:
    screen.fill(bg)
    clock.tick(fps)
    ti +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    bgg.draw(screen)
    tra.update(pygame.mouse.get_pos())
    Env.step(screen,ISIagent.act(Env.get_state()))

    Env.render(screen)
    tra.draw(screen)
    
    pygame.display.flip()