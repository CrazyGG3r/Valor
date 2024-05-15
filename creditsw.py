import pygame
import design as d
import colors as cccc
import random as r
import colorgentool as genn
from classes import button, Text
pygame.init()



def creditss(window):
    bgg = d.Background(window,100,4)
    tra = d.Trailsquare(100)
    running = True
    
    
    butts = []
    while running:
        clicked_buttons = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return
                if event.key == pygame.K_SPACE:
                    pass
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                for a in butts:
                    if a.hover:
                        if not a.isClicked:
                            a.isClicked = True
                            clicked_buttons.append(a)
                
            if event.type == pygame.MOUSEBUTTONUP:
                for a in butts:
                    if a.hover:
                        a.isClicked = False
           
        m = pygame.mouse.get_pos()
        for a in butts:
            if m[0] > a.x and m[1] > a.y:
                if m[0] < (a.x + a.width) and m[1] < (a.y + a.height):
                    a.hover = True
                else:
                    a.hover = False
            else:
                a.hover = False
        for a in clicked_buttons:
            b  = a.action(window)
            
            
            
       
        tra.update(pygame.mouse.get_pos())
        bgg.special_draw(pygame.mouse.get_pos(),window)
        
        for a in butts:
            a.draw(window)
        tra.draw(window)
        pygame.display.flip()
