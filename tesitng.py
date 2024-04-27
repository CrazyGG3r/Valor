import pygame
import time
import random
from pygame.locals import *

pygame.init()

display_width = 1002
display_height = 720

black = (0,0,0)
white = (255,255,255)
red = (220,0,0)
blue = (53,155,255)
green = (0,190,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
dark_blue = (0,102,204)
yellow = (255, 255, 0)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #creates surface/ display
pygame.display.set_caption('Blob Arena') #name of project
clock = pygame.time.Clock() #sets a clock

#________________________________________________________________________________________

blobImage = pygame.image.load('blob2.png')
blobIcon = pygame.image.load('blob_img.png')
bulletpicture = pygame.image.load("bullet.png")
pygame.display.set_icon(blobIcon)
pause = True
blob_width = 51
blob_height = 51
bullet_width = 12
bullet_height = 5

bullets=[]
bullets2=[]

def blob(x,y):
    gameDisplay.blit(blobImage,(x,y)) #drawing to background

def bullets_hit(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,20))

def player_lives(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Lives Left: "+str(count), True, bright_red)
    gameDisplay.blit(text,(0,0))

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(dark_blue)
        largeText = pygame.font.Font('freesansbold.ttf', 110)
        TextSurf, TextRect = text_objects("Blob Arena", largeText)  # Returns text surface and rectangle
        TextRect.center = ((display_width / 2), (display_height / 2.5))
        gameDisplay.blit(TextSurf, TextRect)
        button("Training 1", 200, 430, 140, 53, green, bright_green, game_loop)
        button("Training 2", 431, 430, 140, 53, green, bright_green, game_loop)
        button("Training 3", 662, 430, 140, 53, green, bright_green, game_loop)
        button("Human vs AI", 315.5, 550, 140, 53, green, bright_green, game_loop)
        button("Quit", 546.5, 550, 140, 53, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() #collects mouse left, right and middle button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action!= None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():
    largeText = pygame.font.Font('freesansbold.ttf', 110)
    TextSurf, TextRect = text_objects("Paused", largeText)  # Returns text surface and rectangle
    TextRect.center = ((display_width / 2), (display_height / 2.5))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 315.5, 450, 140, 53, green, bright_green, unpause)
        button("Quit", 546.5, 450, 140, 53, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quit_game():
    pygame.quit()
    quit()

def game_over():
    largeText = pygame.font.Font('freesansbold.ttf', 110)
    TextSurf, TextRect = text_objects("Game Over", largeText)  # Returns text surface and rectangle
    TextRect.center = ((display_width / 2), (display_height / 2.5))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 280.5, 450, 140, 53, green, bright_green,game_loop)
        button("Quit", 581.5, 450, 140, 53, red, bright_red,quit_game)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    x = (display_width * 0.08)
    y = (display_height * 0.2)

    x_change = 0
    y_change = 0

    blob_speed = 2

    velocity = [2, 2]

    score = 0
    lives = 3

    pos_x = display_width/1.2
    pos_y = display_height/1.2

    previous_time = pygame.time.get_ticks()
    previous_time2 = pygame.time.get_ticks()

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():#monitors hardware movement/ clicks
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos_x += velocity[0]
        pos_y += velocity[1]

        if pos_x + blob_width > display_width or pos_x < 601:
            velocity[0] = -velocity[0]

        if pos_y + blob_height > display_height or pos_y < 0:
            velocity[1] = -velocity[1]

        for b in range(len(bullets2)):
            bullets2[b][0] -= 6

        for bullet in bullets2:
            if bullet[0] < 0:
                bullets2.remove(bullet)


        current_time2 = pygame.time.get_ticks()
        #ready to fire when 500 ms have passed.
        if current_time2 - previous_time2 > 500:
            previous_time2 = current_time2
            bullets2.append([pos_x+25, pos_y+24])

# Checks to see if any keys are held down and remembers them with the variable keys.
        keys = pygame.key.get_pressed()

        for b in range(len(bullets)):
            bullets[b][0] += 6

        for bullet in bullets:
            if bullet[0] > 1005:
                bullets.remove(bullet)

        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            #ready to fire when 500 ms have passed.
            if current_time - previous_time > 500:
                previous_time = current_time
                bullets.append([x+25, y+24])

# If the player is holding down one key or the other the blob moves in that direction
        if x < 0:
            x = 0
        if keys[pygame.K_a]:
            x_change = -blob_speed
        if x > 401 - blob_width:
            x = 401 - blob_width
        if keys[pygame.K_d]:
            x_change = blob_speed
        if keys[pygame.K_p]:
            pause = True
            paused()


# If the player is holding down both or neither of the keys the blob stops
        if keys[pygame.K_a] and keys[pygame.K_d]:
            x_change = 0
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            x_change = 0

        if y < 0:
            y = 0
        if keys[pygame.K_w]:
            y_change = -blob_speed
        if y > display_height - blob_height:
            y = display_height - blob_height
        if keys[pygame.K_s]:
            y_change = blob_speed


        if keys[pygame.K_w] and keys[pygame.K_s]:
            y_change = 0
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            y_change = 0


        #print(event)
        # Reset x and y to new position
        x += x_change
        y += y_change

        gameDisplay.fill(blue)  #changes background surface
        bullets_hit(score)
        player_lives(lives)
        pygame.draw.line(gameDisplay, black, (601, display_height), (601, 0), 3)
        pygame.draw.line(gameDisplay, black, (401, display_height), (401, 0), 3)
        blob(pos_x, pos_y)
        blob(x, y)

        for bullet in bullets:
            gameDisplay.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
            if bullet[0] > pos_x and bullet[0] < pos_x + blob_width:
                if bullet[1] > pos_y and bullet[1] < pos_y + blob_height or bullet[1] + bullet_height > pos_y and bullet[1] + bullet_height < pos_y + blob_height:
                    bullets.remove(bullet)
                    score+=1

        for bullet in bullets2:
            gameDisplay.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))
            if bullet[0] + bullet_width < x + blob_width and bullet[0] > x:
                if bullet[1] > y and bullet[1] < y + blob_height or bullet[1] + bullet_height > y and bullet[1] + bullet_height < y + blob_height:
                    bullets2.remove(bullet)
                    lives-=1

        if lives == 0:
            game_over()


        pygame.display.update() #update screen
        clock.tick(120)#moves frame on (fps in parameters)

game_intro()
game_loop()
pygame.quit()
quit()