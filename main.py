from turtle import Screen
import pygame
import sys
import classes as c
import design as d
import random as r
from settings import background_color,settingsaa
import colors as cc

pygame.init()

window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Valor")
pygame.mouse.set_visible(False)


squares = []
population = 100
maxsize = 150
choice = [-1,1]
WHITE = (0,0,0)
offsety = 40
offsetx = 160
butt_h = 40
butt_w = 200
neon  = 150
color_butt = (0,neon,neon)
bf = 1
textcolor = cc.colorlist[12]
heading = c.Text((window.get_width() // 3.2, window.get_height() // 3), 40,textcolor ,"               Valor",1)
sizefont = 30
#0c0c0c,201310,351b15,4a2319,5f2a1e,743223,893a27,9e422c,b34931,c85135,dd593a,f2613f
fcolor = cc.colorlist[2]
t1 = c.Text((0, 0), sizefont, fcolor, "Start",bf)
t2 = c.Text((0, 0), sizefont, fcolor, "Options",bf)
t3 = c.Text((0, 0), sizefont, fcolor, "Credits",bf)
t4 = c.Text((0, 0), sizefont, fcolor, "Exit",bf)
b1 = c.button(((heading.x + offsetx), (heading.y + offsety + 10)), butt_w, butt_h, color_butt, (10, 5), t1,)
b2 = c.button((b1.x, (b1.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t2,settingsaa)
b3 = c.button((b2.x, (b2.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t3,)
b4 = c.button((b3.x, (b3.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t4,exit)
all_text = [heading]
all_butts = [b1,b2,b3,b4]


##=-=- backgroufn

bgg = d.Background(window,70,1)
tra = d.Trailsquare(7)
   

running = True
while running:
    clicked_buttons = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for a in all_butts:
                if a.hover:
                    if not a.isClicked:
                        a.isClicked = True
                        clicked_buttons.append(a)
        if event.type == pygame.MOUSEBUTTONUP:
            for a in all_butts:
                if a.hover:
                    a.isClicked = False
    m = pygame.mouse.get_pos()
    for a in all_butts:
        if m[0] > a.x and m[1] > a.y:
            if m[0] < (a.x + a.width) and m[1] < (a.y + a.height):
                a.hover = True
            else:
                a.hover = False
        else:
            a.hover = False
    for a in clicked_buttons:
        a.action(window)
        bgg.reset_bg(window)
        tra.resetTrail()
     
        

    bgg.draw(window)
    for a in squares:
        a.move(window)
        a.draw(window)
    for a in all_text:
        a.updateColor()
        a.draw(window)
    for a in all_butts:
        a.updateColor()
        a.draw(window)
    
    m = pygame.mouse.get_pos()
    tra.update((m[0],m[1]))
    tra.draw(window)
    pygame.display.flip()


pygame.quit()
sys.exit()
