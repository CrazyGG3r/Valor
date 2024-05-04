#this module contains ui settings
background_color = (0,10,10)
from tkinter import Button
import pygame
import design as d
import colors as cccc
import random as r
import colorgentool as genn
from classes import button, Text
pygame.init()

def raand(var=None):
    d = (r.randint(0,40),r.randint(0,40),r.randint(0,40))
    l = (r.randint(50,200),r.randint(50,200),r.randint(50,200))
    return d,l

def settingsaa(window):
    bgg = d.Background(window,40,1)
    tra = d.Trailsquare(20)
    running = True
    dark = cccc.ColorPicker(window,window.get_width()//3,window.get_height()//4,cccc.colorlist[0])
    light = cccc.ColorPicker(window,window.get_width()//3,(window.get_height()//4)+150,cccc.colorlist[13])
    
    t1 = Text((0,0),30,cccc.colorlist[10]," Randomize ",)
    b1 = button((window.get_width()//3,(window.get_height()//4)+150+200),250,40,cccc.colorlist[9],(10,5),t1,raand)
    butts = [b1]
    while running:
        clicked_buttons = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return
                if event.key == pygame.K_SPACE:
                    genn.colonizer(dark.status(),light.status())
                    bgg.reset_bg(window)
                    tra.resetTrail()
                    
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
            dark.handle_event(event)
            light.handle_event(event)
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
            genn.colonizer(b[0],b[1])
            dark.updateSelf(cccc.colorlist[0])
            light.updateSelf(cccc.colorlist[12])
            bgg.reset_bg(window)
            tra.resetTrail()
            
            
        dark.update()
        light.update()
        tra.update(pygame.mouse.get_pos())
        bgg.draw(window)
        dark.draw(window)
        light.draw(window)
        for a in butts:
            a.draw(window)
        tra.draw(window)
        pygame.display.flip()
