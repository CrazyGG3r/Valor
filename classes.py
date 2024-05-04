from re import A
import pygame
import random
import colors as c

font = ['assets\\fonts\\f1.ttf','assets\\fonts\\f2.ttf']

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

    def update_text(self, new_text):
        self.text = new_text
        self.surface = self.font.render(new_text, True, self.color)
    def update_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

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
        # for n, a in enumerate(self.NotHovercolor):
        #     a -= 50 
        #     if a < 0:
        #         a = 0
        #     if a <= -1:
        #         a *= -1
        #     if a>255:
        #        a = a -255
        #     self.Hovercolor.append(a)
        self.Hovercolor = tuple(self.Hovercolor)
        print(self.Hovercolor)
        self.text = None
        self.hover = False
        self.text = butt_text
        self.text.update_coords((self.pad_x,self.pad_y))
        self.action = function
        self.isClicked = False

    def draw(self, screen,):
        if self.hover:
            pygame.draw.rect(screen, self.Hovercolor, (self.x, self.y, self.width, self.height))
            self.text.color2 = c.colorlist[10]
            self.text.changecolor(self.text.color2)
            self.text.draw(screen)
        else:
            pygame.draw.rect(screen, self.NotHovercolor, (self.x, self.y, self.width, self.height))
            self.text.changecolor(self.text.color)
            self.text.draw(screen)
            self.text.draw(screen)
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