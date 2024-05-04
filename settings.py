#this module contains ui settings
background_color = (0,10,10)
import pygame
import design as d
import colors as cccc
import colorgentool as genn
pygame.init()



def settingsaa(window):
    bgg = d.Background(window,40,1)
    tra = d.Trailsquare(20)
    running = True
    dark = cccc.ColorPicker(window,window.get_width()//3,window.get_height()//4,cccc.colorlist[0])
    light = cccc.ColorPicker(window,window.get_width()//3,(window.get_height()//4)+150,cccc.colorlist[13])
    
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
                print("Hi")
                
            if event.type == pygame.MOUSEBUTTONUP:
                print("Heo")
            dark.handle_event(event)
            light.handle_event(event)
       
        dark.update()
        light.update()
        tra.update(pygame.mouse.get_pos())
        bgg.draw(window)
        dark.draw(window)
        light.draw(window)
        tra.draw(window)
        pygame.display.flip()
