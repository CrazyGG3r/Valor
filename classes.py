from re import A
import pygame
import random
import colors as c

font = ['assets\\fonts\\f1.ttf','assets\\fonts\\f2.ttf','assets\\fonts\\f3.ttf']

class Text:
    def __init__(self, coords, font_size, color, text, fonts=0):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.color2 = color
        self.x = coords[0]
        self.y = coords[1]
        self.font = pygame.font.Font(font[fonts], font_size)
        self.surface = self.font.render(text, True, color)
        #credits special
        self.angle = random.randint(0,50)
        self.vectorr = (random.randint(-2,2)/random.randint(10,100),random.randint(-2,2)/random.randint(10,100))
        
    def update_text(self, new_text):
        self.text = new_text
        self.surface = self.font.render(new_text, True, self.color)
        
    def update_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        
    def draw2(self,screen):
        rotated_surface = pygame.transform.rotate(self.surface, self.angle)
        rotated_rect = rotated_surface.get_rect(center=(self.x, self.y))
        screen.blit(rotated_surface, rotated_rect.topleft)
        self.angle+=random.randint(0,10)/100
        self.x += self.vectorr[0]
        self.y += self.vectorr[1]
        
        if self.x <= -10:
            self.vectorr = (self.vectorr[0]*-1,self.vectorr[1])
        if self.x >= screen.get_width():
            self.vectorr = (self.vectorr[0]*-1,self.vectorr[1])
        if self.y <=0:
            self.vectorr = (self.vectorr[0],self.vectorr[1]*-1)
        if self.y >=screen.get_height():
            self.vectorr = (self.vectorr[0],self.vectorr[1]*-1)
            
    def updateColor(self):
        self.changecolor(c.colorlist[12])

    def changecolor(self, color):
        self.surface = self.font.render(self.text, True, color)
        


def dummy(ac = "None"):
    print("Clicked somehting",random.randint(0,10))


class button:
    def __init__(self, coords, w, h, color,padding, butt_text, function = dummy):
        self.x = coords[0]
        self.y = coords[1]
        self.pad_x = self.x + padding[0]
        self.pad_y = self.y + padding[1]
        self.width = w
        self.height = h
        self.NotHovercolor = c.colorlist[9]
        self.Hovercolor = c.colorlist[4]

        
        self.text = None
        self.hover = False
        self.text = butt_text
        self.text.update_coords((self.pad_x,self.pad_y))
        self.action = function
        self.isClicked = False

    def draw(self, screen,):
        self.updateColor()
        self.text.updateColor()
        if self.hover:
            pygame.draw.rect(screen, self.Hovercolor, (self.x, self.y, self.width, self.height))
            self.text.color2 = c.colorlist[12]
            self.text.changecolor(self.text.color2)
            self.text.draw(screen)
        else:
            pygame.draw.rect(screen, self.NotHovercolor, (self.x, self.y, self.width, self.height))
            self.text.changecolor(c.colorlist[2])
            self.text.draw(screen)
            self.text.draw(screen)
    def updateColor(self):
        self.NotHovercolor = c.colorlist[9]
        self.Hovercolor = c.colorlist[4]
class CreateDrone:
    def __init__(self, radius, position, speed, destination, name, color):
        self.radius = radius
        self.position = position
        self.speed = speed
        self.des = destination
        self.name = str(name)
        self.color = color
        self.fontColor = (0,190,190)
    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)
       
        name_surface = pygame.font.SysFont(None, 20).render(self.name, True, self.fontColor)
        window.blit(name_surface, (self.position[0] - self.radius, self.position[1] + self.radius + 10))

    
def limit_value(value, min_value, max_value):
    return max(min_value, min(max_value, value))