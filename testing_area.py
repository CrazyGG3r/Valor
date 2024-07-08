import pygame 
from Noob import Environment,Agent
import design as d
import colorgentool as genn
import colors as cc
import random as r




pygame.init()

window_width = 1280
window_height = 720
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Valor")
pygame.mouse.set_visible(False)


pygame.init()

i = pygame.display.Info()


color1 = cc.colorlist[12]

newcolor = genn.diffuser(color1,color1)


bg = cc.colorlist[0]
movr = False
keyy = None
clock = pygame.time.Clock()
keys_pressed = set()
fps = 60
ti =  0

bgg = d.Background(screen,12,1)
tra = d.Trailsquare(5)



running = True
episode = 0
clock = pygame.time.Clock()

env = Environment(screen)

while running:
    clock.tick(fps)

    tra.update(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                running = False

    # Get current state
   
    # Render the environment
    env.render(screen)

    # Update display
    pygame.display.update()
    
    bgg.draw(screen)
    tra.draw(screen)
    
        



