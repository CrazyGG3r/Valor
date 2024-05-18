import pygame
import design as d
import colors as cccc
import random as r
import colorgentool as genn
from classes import button, Text
pygame.init()



def creditss(window):
    bgg = d.Background(window,40,4)
    tra = d.Trailsquare(100)
    running = True
    
    t1 = Text((r.randint(100,800),100),40,cccc.colorlist[11],"Made BY:",1)
    t2 = Text((r.randint(10,900),200),40,cccc.colorlist[11],"Shaheer Ul Islam",1)
    t3 = Text((r.randint(10,900),300),40,cccc.colorlist[11],"Zarah Hasan",1)
    t4 = Text((r.randint(10,900),500),40,cccc.colorlist[11],"Trained by: ",1)
    t5 = Text((r.randint(10,900),600),40,cccc.colorlist[11],"Maaz Khan ",1)
    
    all_text = [t1,t2,t3,t4,t5]
    
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
        for a in all_text:
            a.draw2(window)
        for a in butts:
            a.draw(window)
        tra.draw(window)
        pygame.display.flip()
