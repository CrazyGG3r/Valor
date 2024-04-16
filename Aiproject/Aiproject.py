  
print("hello")
import pygame
from entities import * 
import random as r 

pygame.init()
i = pygame.display.Info()
width,height = 1280,720
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)

col = (0,200,200)
p1 = person((width//2,height//2),20,5,'test',col,100,100,5,screen)

bg = (0,20,20)
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
spaw = spawner(screen)

while True:
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
        spaw.spawn()
        enemies = spaw.enemies
    
    for e in enemies:
        m = pygame.mouse.get_pos()
        if e :
            if ti%r.randint(1,2) ==0:
                e.move1(screen,p1.x,p1.y)
            e.draw(screen)
    for p in players:
        if p.bullets:
            for b in p.bullets:
                if b == None:
                    continue
                if b.shooting == False:
                    p.bullets.remove(b)
                else:
                    
                    b.move()
                    b.draw(screen)
        p.draw(screen)           
    pygame.display.flip()
