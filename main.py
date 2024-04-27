from turtle import Screen
import pygame
import sys
import classes as c
import design as d
import random as r

from settings import *


pygame.init()

window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Drone Coordination")
pygame.mouse.set_visible(False)


squares = []
population = 100
maxsize = 150
choice = [-1,1]
def reset_bg():
    if squares:
        for a in range(population):
            squares.pop()
        print(len(squares))
    for a in range(population):
        neon = r.randint(10,50)
        coo = (r.randint(0,window.get_width()),r.randint(0,window.get_height()))
        coloro = (0,neon,neon)
        raa = r.randint(0,100)/1000
        raa = r.choice(choice) * raa
        squares.append(d.Square(coo,r.randint(10,maxsize),coloro,raa))
reset_bg()        

WHITE = (0,0,0)
offsety = 40
offsetx = 160
butt_h = 40
butt_w = 200
neon  = 150
color_butt = (0,neon,neon)
bf = 1
heading = c.Text((window.get_width() // 3.2, window.get_height() // 3), 40,(200,200,200) ,"Drone Coordination Simulation",1)
sizefont = 30
fcolor = (0,10,10)
t1 = c.Text((0, 0), sizefont, fcolor, "Start",bf)
t2 = c.Text((0, 0), sizefont, fcolor, "Options",bf)
t3 = c.Text((0, 0), sizefont, fcolor, "Credits",bf)
t4 = c.Text((0, 0), sizefont, fcolor, "Exit",bf)
b1 = c.button(((heading.x + offsetx), (heading.y + offsety + 10)), butt_w, butt_h, color_butt, (10, 5), t1,dd.drones)
b2 = c.button((b1.x, (b1.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t2)
b3 = c.button((b2.x, (b2.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t3)
b4 = c.button((b3.x, (b3.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t4)
all_text = [heading]
all_butts = [b1,b2,b3,b4]


##=-=- backgroufn

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
        reset_bg()
        tra.resetTrail()
        a.action(window)
        reset_bg()
        tra.resetTrail()
    window.fill(background_color)
    for a in squares:
        a.move(window)
        a.draw(window)
    for a in all_text:
        a.draw(window)
    for a in all_butts:
        a.draw(window)
    m = pygame.mouse.get_pos()
    tra.update((m[0],m[1]))
    tra.draw(window)
    pygame.display.flip()


pygame.quit()
sys.exit()
